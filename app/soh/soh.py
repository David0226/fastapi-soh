from threading import Thread
import soh_service as service

class RunSoh(Thread):

    def __init__(self):
        super().__init__()
        self.start()


    def start(self):
        try:
            print("start")
        except Exception as e:
            print(e)


    def run(self) -> None:
        while True:
            self.proccess()

    def proccess(self):
        try:
            print("proccess")
        except Exception as e:
            print(e)
            #
            # g_u64SohTimeStamp = g_stSohMsg.measTimeStamp
            # memcpy(g_s16SohMeasInst, g_stSohMsg.meas, sizeof(g_stSohMsg.meas))
            #
            # if (true == setValidDataIntoMem(g_s16SohMeasInst, g_u64SohTimeStamp)) {
            #
            # if (true == extractFeatureSOH(g_f32SohMeasDetaT, g_u16SohMeasCVolt, g_u16SohMeasPackCurr, g_u16MeasNumCount)) {
            # soh_pred = runXgboostToPredSOH(g_f32ExtrFeat)
            # writeSohCsvFile(g_f32ExtrFeat, soh_pred, g_u64SohTimeStamp)
            #
            # composeFeatJsonObjs( & g_stSohJsonObj, g_f32ExtrFeat, soh_pred, g_u64SohTimeStamp * 1000)
            # obj_len = strlen( json_object_to_json_string(g_stSohJsonObj.obj))
            # memcpy(g_u8FeatSohBuf, json_object_to_json_string(g_stSohJsonObj.obj), obj_len)
            #
            # soh_file_path = writeSohJsonFile(g_u8FeatSohBuf, obj_len, g_u64SohTimeStamp)
            # if (soh_file_path != NULL) {
            # g_stSohInfo.sMlSoh = soh_pred
            # }
            # }
            # / * initialize global variables * /
            # g_u16SohMeasCount = 0
            # memset(g_u16SohMeasCVolt, 0x00, sizeof(g_u16SohMeasCVolt))
            # memset(g_f32SohMeasDetaT, 0x00, sizeof(g_f32SohMeasDetaT))
            # memset(g_u16SohMeasPackCurr, 0x00, sizeof(g_u16SohMeasPackCurr))
            # memset(g_f32SohCalcRegnQ, 0x00, sizeof(g_f32SohCalcRegnQ))
            # memset(g_f32ExtrFeat, 0x00, sizeof(g_f32ExtrFeat))
            # }