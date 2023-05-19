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


def router_doing(commands: str):
    """
    You can use commands like
    setparam, info, callhh, callsj, callboth, readraw, readjson, viewlist, select, help

    example usage: setparam, info, callboth, readjson, viewlist, select

    """

    command_splitted = commands.strip().split()[0]

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
    #     return hhsj_controllers.readraw
    elif command_splitted == "readjson":
        return saver_controller.read()
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
