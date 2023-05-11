import logging
import math
from asyncio import sleep
from http.client import HTTPException

from os import path
from threading import Thread

from fastapi import Depends
from sqlalchemy.orm import Session
from yaml import safe_load

from .constants import Definition as cons

from database.model import battery_schema
from database.crud import battery_crud
from database import mysql_db

def find_feat_index(sel_volt, volt_mem, mem_size):
    for idx in range(mem_size - 1, 0, -1):
        if volt_mem[idx] == sel_volt:
            rtn_idx = idx

    return rtn_idx


def read_data_test():
    db_session = mysql_db.SessionLocal()
    print(db_session)

    batter_data = battery_crud.get_datas(db=db_session)

    for row in batter_data:
        print(row.ts, row.bmsid, row.packcurr, row.packvol, row.chgstat)

    if batter_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    return batter_data


class SohService:
    def __init__(self, config_file=None):
        self.stopped = False
        if config_file is None:
            config_file = path.dirname(path.dirname(path.abspath(__file__))) + '/config/soh_sdi.yml'.replace('/',
                                                                                                             path.sep)
        with open(config_file) as general_config:
            self.__config = safe_load(general_config)
        self._config_dir = path.dirname(path.abspath(config_file)) + path.sep

        self._send_thread = Thread(target=self.__read_data(), name="send data to thread")
        self._send_thread.start()

        self.meas_volt = None
        self.meas_curr = None
        self.meas_time = None
        self.meas_num_cnt = None
        self.calc_soh_regn_q = None
        self.ext_feat = None

    def set_valid_data_into_mem(self, inst_data, pst_meastm):
        meas_idx = 0
        prv_meastm = 0
        egnQ = 0.0
        accu_gap_time = 0.0
        rtn = False
        gap_time = 0
        avg_volt = inst_data[0]
        pack_curr = inst_data[1]
        chg_stat = inst_data[2]

        if (chg_stat == 1) and (pack_curr > cons.SEL_PACK_CURR):
            gap_time = pst_meastm - prv_meastm

            if gap_time <= cons.SEL_STD_GAPSEC:
                if avg_volt == cons.BOUND_START_CVOLT:
                    meas_idx = 0
                    self.meas_time[0] = gap_time
                    self.meas_volt = avg_volt
                    self.meas_curr = pack_curr * cons.PACK_CURR_SCALE

                    meas_idx = meas_idx + 1

                else:
                    if meas_idx != 0:
                        if (avg_volt > cons.BOUND_START_CVOLT) and (
                                avg_volt < (cons.BOUND_END_CVOLT + (3 * cons.BOUND_STEP_CVOLT))):
                            if meas_idx < (cons.SOH_MAX_MEAS_NUM - 1):
                                self.meas_time = gap_time
                                self.meas_volt = avg_volt
                                self.meas_curr = pack_curr * cons.PACK_CURR_SCALE
                        else:
                            if avg_volt >= (cons.BOUND_END_CVOLT + (3 * cons.BOUND_STEP_CVOLT)):
                                self.meas_num_cnt = meas_idx
                                meas_idx = 0
                                rtn = True
            else:
                self.meas_num_cnt = 0
                meas_idx = 0

            prv_meastm = pst_meastm

        return rtn

    def extract_feature_soh(self, gap_sec_mem, volt_mem, curr_mem, mem_size):
        rtn = False
        # idx = 0
        find_idx = 0
        count = 0
        start_idx = 0

        accum_sec = 0.0
        prev_q, prst_q = 0.0
        accum_dqv, accum_cap = 0.0

        sel_ref_v = cons.BOUND_START_CVOLT

        for idx in range(0, cons.SOH_VOLT_FEAT_NUM, 1):
            find_idx = find_feat_index(sel_ref_v, volt_mem, mem_size)
            if find_idx != -1:
                sel_ref_v += cons.BOUND_STEP_CVOLT
                if idx == 0:
                    prev_q = 0
                    start_idx = find_idx
                    self.ext_feat[2] = 0.0
                else:
                    accum_sec = 0.0
                    accum_cap = 0.0

                    for count in range(start_idx, find_idx, 1):
                        accum_sec += gap_sec_mem[count]
                        accum_cap += (gap_sec_mem[count] * math.fabs(curr_mem[count]))

                    prst_q = accum_cap
                    accum_dqv += ((prst_q - prev_q) / (0.001 * cons.BOUND_STEP_CVOLT))
                    self.ext_feat[idx + 2] = prst_q  # (float) prst_Q
                    prev_q = prst_q

                rtn = True

            else:
                print("Cannot find the index for " + sel_ref_v + "[V]")
                rtn = False
                break

        if rtn:
            self.ext_feat[0] = accum_dqv / cons.SOH_VOLT_FEAT_NUM
            self.ext_feat[1] = accum_sec / 60

        return rtn

    def __read_data(self):
        read_data_test()

        #
        # while not self.stopped:
        #     try:
        #         pass
        #
        #         # read_data_test()
        #
        #         # sleep(1)
        #         # read data
        #         # print("read data")
        #     except Exception as e:
        #         print("read data exception")
        #         sleep(1)
