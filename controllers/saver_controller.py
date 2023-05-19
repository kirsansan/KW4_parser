from src.savers import JSONSaver
from models.vacancy_model import VacancyModel
from config.config import FILE_FOR_WRITE_RAW_DATA, FILE_FOR_WRITE_RAW_DATA_SJ


class SaverController:

    def __init__(self, model: VacancyModel,  saver: JSONSaver):
        self.model = model
        self.saver = saver

    def read(self):
        """Read the information from my json-format file
        writing lives in models and don't need to use in handmade inferface controller"""
        return self.model.replace(self.saver.read())

