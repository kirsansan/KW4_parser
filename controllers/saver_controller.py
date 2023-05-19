from src.savers import JSONSaver
from models.vacancy_model import VacancyModel
from config.config import FILE_FOR_WRITE_RAW_DATA, FILE_FOR_WRITE_RAW_DATA_SJ


class SaverController:

    def __init__(self, model: VacancyModel,  saver: JSONSaver):
        self.model = model
        self.saver = saver

    def read(self):
        return self.model.replace(self.saver.read())

