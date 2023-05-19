from src.model import Model_HH
from src.savers import JSONSaver
from config.config import FILE_FOR_WRITE_RAW_DATA


class HHController:

    def __init__(self, model: Model_HH, saver: JSONSaver):
        self.model = model
        self.saver = saver

    def call(self):
        self.model.get_big_data_step_by_step(files_write_flag=False)
        self.model.write_to_file(FILE_FOR_WRITE_RAW_DATA)
        vl = self.model.get_parsed_data()
        self.saver.set_datalist(vl)
        self.saver.write()
        return

