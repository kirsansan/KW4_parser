class Router:

    def __init__(self, controllers):
        self.controllers = controllers

    def doing(self, commands: str):
        """
        You can use commands like


        """

        command_splitted = commands.strip().split()[0]
        if command_splitted not in self.controllers.keys():
            return

        if command_splitted == "callHH":
            return self.controllers["callHH"].read_big_apiHH()
        elif command_splitted == "callSJ":
            return self.controllers["callSJ"].read_big_apiSJ()
        elif command_splitted == "readRAW":
            return self.controllers["readRAW"]
        elif command_splitted == "readJSON":
            return self.controllers["readJSON"].read()
        elif command_splitted == "select":
            return self.controllers["select"]
        elif command_splitted == "setKEY":
            return self.controllers["setKEY"]
        elif command_splitted == "setFilter":
            return self.controllers["setFilter"]
        elif command_splitted == "ViewVAC":
            return self.controllers["ViewVAC"].print_all()

