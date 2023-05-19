from src.model import *
from src.savers import *
from src.router import Router

class Controller_HH:

    def __init__(self, model_sender, model_receiver=None, view=None):
        self.model_sender = model_sender
        self.model_receiver = model_receiver
        self.view = view


    def read_big_apiHH(self):
        #m1 = Model_HH({"text": "python", "area": 2})
        self.model_sender.get_big_data_step_by_step(files_write_flag=False)
        self.model_sender.write_to_file(FILE_FOR_WRITE_RAW_DATA)

        if self.model_receiver:
            vl = self.model_sender.get_parsed_data()
            self.model_receiver.all = vl
        # saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
        # saver.write()

class Controller_SJ:

    def __init__(self, model, view=None):
        self.model = model
        self.view = view
    def read_big_apiSJ(self):
        #m4 = Model_SuperJob({"text": "python", "area": 0})
        # m4.connect_to_API(0, 100)
        self.model.get_big_data_step_by_step(files_write_flag=True)
        # m4.print_content()
        # m4.write_to_file(FILE_FOR_WRITE_RAW_DATA_SJ)
        # m1.get_big_data_step_by_step(files_write_flag=True)
        #vl = m4.get_parsed_data()
        # print(len(vl))
        # [print(v) for v in vl]

        # saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
        # saver.write()

class Controller_Saver:

    def __init__(self, model, model_receiver=None, view=None):
        self.model = model
        self.model_receiver = model_receiver
        self.view = view

    def read(self):
        self.model_receiver.all = self.model.read()
        pass

    def write(self):
        self.model.write()



    def read_both_API(self):
        m1 = Model_HH({"text": "python", "area": 2})
        m1.get_big_data_step_by_step(files_write_flag=True)
        # m1.write_to_file(FILE_FOR_WRITE_RAW_DATA)
        m4 = Model_SuperJob({"text": "python", "area": 2})
        m4.get_big_data_step_by_step(files_write_flag=True)

        vl = m1.get_parsed_data()
        vl.extend(m4.get_parsed_data())

        saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
        saver.write()


    def print_big_apiHH(self):
        m1 = Model_HH({"text": "python", "area": 2})
        m1.get_big_data_step_by_step(files_write_flag=True)
        vl = m1.vacancy_list
        print(len(vl))
        [print(v) for v in vl]


    def read_vacancy_data_file(self):
        saver = JSONSaver(FILE_FOR_VACANCY_JSON)
        vvl: list[Vacancy] = saver.read()
        # print(vvl)
        vvl.sort(reverse=True)
        print("================================================================")
        print(vvl)


    def read_raw_fileHH(self):
        m2 = Model_HH({"text": "python"})
        m2.load_from_file(FILE_FOR_WRITE_RAW_DATA)
        # m2.print_content()
        m2.get_parsed_data()
        print(m2.vacancy_list)


    def read_raw_fileSJ(self):
        m3 = Model_SuperJob({"text": "python"})
        m3.load_from_file(FILE_FOR_WRITE_RAW_DATA_SJ)
        # m2.print_content()
        m3.get_parsed_data()
        print(m3.vacancy_list)
        print(len(m3.vacancy_list))


class Controller_Vac:

    def __init__(self, model, view=None):
        self.model = model
        self.view = view

    def print_all(self):
        return self.view.print_all(self.model.all)
