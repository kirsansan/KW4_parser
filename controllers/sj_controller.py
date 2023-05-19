from src.model import Model_SuperJob
from src.savers import JSONSaver
from config.config import FILE_FOR_WRITE_RAW_DATA_SJ


class SJController:

    def __init__(self, model: Model_SuperJob, saver: JSONSaver):
        self.model = model
        self.saver = saver

    def call(self):
        """ call API method for the given data
             this method use model.param when call API-request"""
        self.model.get_big_data_step_by_step(files_write_flag=False)
        self.model.write_to_file(FILE_FOR_WRITE_RAW_DATA_SJ)
        vl = self.model.get_parsed_data()
        self.saver.set_datalist(vl)
        self.saver.write()
        return
