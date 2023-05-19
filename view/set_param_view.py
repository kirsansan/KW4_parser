class SetParamView:

    def __init__(self, param={"text": "python", "area": 2}):
        """
        param is dict with like-this format: {"text": "python", "area": 2} """
        self.param = param


    def dialog(self):
        """dialog for set parameters by user"""
        print("-----------------------")
        print("Enter keyword for request vacancies from API")
        tmp_input = input(">")
        self.param["text"] = tmp_input.split()[0] if len(tmp_input) > 0 else ""
        print("Enter number of region for request vacancies from API 1 - msc, 2 - st.petersburg ... ")
        tmp_input = input(">")
        if len(tmp_input) > 0 and tmp_input.split()[0].isdigit():
            self.param["area"] = int(tmp_input.split()[0])
        return self.param
