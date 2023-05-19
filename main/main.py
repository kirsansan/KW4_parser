from src.model import *
from src.savers import *
from models.vacancy_model import VacancyModel
from view.vacancy_list_view import VacancyListView
from view.set_param_view import SetParamView
from controllers.vacancy_controller import VacancyController


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

    if command_splitted == "setParam":
        global main_request
        main_request = set_main_request_view.dialog()
        model_hh.set_params(main_request)
        model_sj.set_params(main_request)
        return
    elif command_splitted == "info":
        print("parameters for HH:", model_hh.params)
        print("parameters for SJ:", model_sj.params)
        return
    elif command_splitted == "callHH":
        model_hh.get_big_data_step_by_step(files_write_flag=False)
        model_hh.write_to_file(FILE_FOR_WRITE_RAW_DATA)
        vl = model_hh.get_parsed_data()
        saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
        saver.write()
        return
    elif command_splitted == "callSJ":
        model_sj.get_big_data_step_by_step(files_write_flag=False)
        model_sj.write_to_file(FILE_FOR_WRITE_RAW_DATA_SJ)
        vl = model_sj.get_parsed_data()
        saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
        saver.write()
        return
    elif command_splitted == "callBoth":
        model_hh.get_big_data_step_by_step(files_write_flag=False)
        model_hh.write_to_file(FILE_FOR_WRITE_RAW_DATA_SJ)
        model_sj.get_big_data_step_by_step(files_write_flag=False)
        model_sj.write_to_file(FILE_FOR_WRITE_RAW_DATA_SJ)
        vl = model_hh.get_parsed_data()
        vl.extend(model_sj.get_parsed_data())
        saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
        saver.write()
        return
    # elif command_splitted == "readRAW":
    #     return self.controllers["readRAW"]
    elif command_splitted == "readJSON":
        saver = JSONSaver(FILE_FOR_VACANCY_JSON)
        model_vacancy.replace(saver.read())
        return
    # elif command_splitted == "select":
    #     return self.controllers["select"]
    # elif command_splitted == "setKEY":
    #     return self.controllers["setKEY"]
    elif command_splitted == "setFilter":
        return vacancy_view
    elif command_splitted == "ViewVAC":
        return vacancy_controller.print_all()


if __name__ == '__main__':

    main_request = {"text": "python", "area": 2}

    model_hh = Model_HH(main_request)
    model_sj = Model_SuperJob(main_request)
    model_vacancy = VacancyModel()
    model_json = JSONSaver(FILE_FOR_VACANCY_JSON, model_vacancy.all)

    vacancy_view = VacancyListView()
    set_main_request_view = SetParamView()

    # controller_hh = Controller_HH(model_hh, model_vacancy)
    # controller_sj = Controller_SJ(model_sj)
    # controller_json = Controller_Saver(model_json, model_vacancy)
    # controller_vac = Controller_Vac(model_vacancy, vacancy_view)

    vacancy_controller = VacancyController(model_vacancy, vacancy_view)
    # vacancy_list_view = Vacancy_ListView(controller_hh, controller_)

    while True:
        print("use commands: setParam, callHH, callJS, callBoth, readRAW, readJSON, ViewVAC")
        user_input = input("What do you want? >")
        if user_input.lower() == 'stop':
            quit(0)
        router_doing(user_input)






    # read_big_apiHH()
    # read_raw_fileHH()
    # read_vacancy_data_file()

    # read_big_apiSJ()
    # read_raw_fileSJ()

    #read_both_API()



    # model = VacancyModel()
    # tmp = read_vacancy_data_file()
    # model.all = tmp
    # print(len(tmp))
    # print(len(model.all))
    #
    # view = VacancyListView()
    # #view.print_all(model.all)
    # # view.print_ext_mode(model.all)
    #
    # view.print_ext_mode(model.filter_by_strings("математическое".split()))
    # b = model.filter_by_salary(180_000)
    # view.print_ext_mode(b)
    # с = model.filter_by_strings("shell".split(), b)
    # view.print_ext_mode(с)
    #
    # view_set = SetParamView()
    # parameters = view_set.dialog()
    # print(parameters)



    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # print(filter_words)
    # v1 = Vacancy("asas", "desc1", 1, None, "url")
    # v2 = Vacancy("bsbs", "desc2", None, None, "url")
    # print(v1 > v2)


    # m1.get_data_from_API()
    # # m1.print_content()

    # m1.write_to_file()
    # m1.load_from_file()
    # m1.print_content()
