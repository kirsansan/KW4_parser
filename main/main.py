from src.model import *
from src.savers import *
from src.router import Router
from controller.controller import *
from models.vacancy_list import VacancyModel
from view.vacancy_list_view import VacancyListView





if __name__ == '__main__':
    # read_big_apiHH()
    # read_raw_fileHH()
    # read_vacancy_data_file()

    # read_big_apiSJ()
    # read_raw_fileSJ()

    # read_both_API()

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

    main_request = {"text": "python", "area": 2}

    model_hh = Model_HH(main_request)
    model_sj = Model_SuperJob(main_request)
    model_vacancy = VacancyModel()
    model_json = JSONSaver(FILE_FOR_VACANCY_JSON, model_vacancy.all)

    vacancy_view = VacancyListView()

    controller_hh = Controller_HH(model_hh, model_vacancy)
    controller_sj = Controller_SJ(model_sj)
    controller_json = Controller_Saver(model_json, model_vacancy)
    controller_vac = Controller_Vac(model_vacancy, vacancy_view)

    # vacancy_list_view = Vacancy_ListView(controller_hh, controller_)

    router = Router({"callHH": controller_hh,
                     "callSJ": controller_sj,
                     "readJSON": controller_json,
                     "ViewVAC": controller_vac})

    while True:
        print("use commands: callHH, callJS, readRAW, readJSON, ViewVAC")
        user_input = input(">")
        if user_input.lower() == 'stop':
            quit(0)
        router.doing(user_input)
