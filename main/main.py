from controllers.hhsj_controller import HHSJController
from src.model import *
from src.savers import *
from models.vacancy_model import VacancyModel
from view.vacancy_list_view import VacancyListView
from view.set_param_view import SetParamView
from controllers.vacancy_controller import VacancyController
from controllers.hh_controller import HHController
from controllers.sj_controller import SJController
from controllers.saver_controller import SaverController
from view.help_view import Helper


def read_big_apiHH():
    m1 = Model_HH({"text": "python", "area": 2})
    m1.get_big_data_step_by_step(files_write_flag=True)
    # m1.write_to_file(FILE_FOR_WRITE_RAW_DATA)
    vl = m1.get_parsed_data()
    saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
    saver.write()


def read_big_apiSJ():
    m4 = Model_SuperJob({"text": "python", "area": 0})
    # m4.connect_to_API(0, 100)
    m4.get_big_data_step_by_step(files_write_flag=True)
    # m4.print_content()
    # m4.write_to_file(FILE_FOR_WRITE_RAW_DATA_SJ)
    # m1.get_big_data_step_by_step(files_write_flag=True)
    vl = m4.get_parsed_data()
    # print(len(vl))
    # [print(v) for v in vl]

    # saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
    # saver.write()


def read_both_API():
    m1 = Model_HH({"text": "python", "area": 2})
    m1.get_big_data_step_by_step(files_write_flag=True)
    # m1.write_to_file(FILE_FOR_WRITE_RAW_DATA)
    m4 = Model_SuperJob({"text": "python", "area": 2})
    m4.get_big_data_step_by_step(files_write_flag=True)

    vl = m1.get_parsed_data()
    vl.extend(m4.get_parsed_data())

    saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
    saver.write()


def print_big_apiHH():
    m1 = Model_HH({"text": "python", "area": 2})
    m1.get_big_data_step_by_step(files_write_flag=True)
    vl = m1.vacancy_list
    print(len(vl))
    [print(v) for v in vl]


def read_vacancy_data_file():
    saver = JSONSaver(FILE_FOR_VACANCY_JSON)
    vvl: list[Vacancy] = saver.read()
    # print(vvl)
    vvl.sort(reverse=True)
    print("================================================================")
    #print(vvl)
    return vvl


def read_raw_fileHH():
    m2 = Model_HH({"text": "python"})
    m2.load_from_file(FILE_FOR_WRITE_RAW_DATA)
    # m2.print_content()
    m2.get_parsed_data()
    print(m2.vacancy_list)


def read_raw_fileSJ():
    m3 = Model_SuperJob({"text": "python"})
    m3.load_from_file(FILE_FOR_WRITE_RAW_DATA_SJ)
    # m2.print_content()
    m3.get_parsed_data()
    print(m3.vacancy_list)
    print(len(m3.vacancy_list))

def router_doing(commands: str):
    """
    You can use commands like
    """

    command_splitted = commands.strip().split()[0]
    #if command_splitted not in self.controllers.keys():
    #    return

    if command_splitted == "setparam":
        global main_request
        main_request = set_main_request_view.dialog()
        model_hh.set_params(main_request)
        model_sj.set_params(main_request)
        return
    elif command_splitted == "info":
        print("parameters for HH:", model_hh.params)
        print("parameters for SJ:", model_sj.params)
        return
    elif command_splitted == "callhh":
        return hh_controller.call()
    elif command_splitted == "callsj":
        return sj_controller.call()
    elif command_splitted == "callboth":
        return hhsj_controller.call()
    # elif command_splitted == "readraw":
    #     return self.controllers["readRAW"]
    elif command_splitted == "readjson":
        return saver_controller.read()
        # saver = JSONSaver(FILE_FOR_VACANCY_JSON)
        # model_vacancy.replace(saver.read())
    elif command_splitted == "select":
        return vacancy_controller.set_and_print_select()
    elif command_splitted == "viewlist":
        saver_controller.read()
        return vacancy_controller.print_ext()
    elif command_splitted == "help":
        return helper.print_help()


if __name__ == '__main__':

    main_request = {"text": "python", "area": 2}

    # init models
    model_hh = Model_HH(main_request)
    model_sj = Model_SuperJob(main_request)
    model_vacancy = VacancyModel()
    model_json = JSONSaver(FILE_FOR_VACANCY_JSON, model_vacancy.all)

    # init views
    vacancy_view = VacancyListView()
    set_main_request_view = SetParamView()

    # init controllers
    vacancy_controller = VacancyController(model_vacancy, vacancy_view)
    hh_controller = HHController(model_hh, model_json)
    sj_controller = SJController(model_sj, model_json)
    hhsj_controller = HHSJController(model_hh, model_sj, model_json)
    saver_controller = SaverController(model_vacancy, model_json)

    # init helper
    helper = Helper()

    # interface
    while True:
        print("use commands: setparam, info, callhh, callsj, callboth, readraw, readjson, viewlist, select, help")
        user_input = input("What do you want? >")
        if user_input.lower() == 'stop':
            quit(0)
        router_doing(user_input)

