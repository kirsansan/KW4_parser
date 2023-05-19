from src.model import Model_HH
from src.model import Model_SuperJob
from src.savers import JSONSaver
from config.config import FILE_FOR_WRITE_RAW_DATA, FILE_FOR_WRITE_RAW_DATA_SJ


class HHSJController:

    def __init__(self, model1: Model_HH, model2: Model_SuperJob, saver: JSONSaver):
        self.model1 = model1
        self.model2 = model2
        self.saver = saver

    def call(self):
        self.model1.get_big_data_step_by_step(files_write_flag=False)
        self.model1.write_to_file(FILE_FOR_WRITE_RAW_DATA)
        self.model2.get_big_data_step_by_step(files_write_flag=False)
        self.model2.write_to_file(FILE_FOR_WRITE_RAW_DATA_SJ)
        vl = self.model1.get_parsed_data()
        vl.extend(self.model2.get_parsed_data())
        self.saver.set_datalist(vl)
        self.saver.write()
        return

