class Helper:

    def print_help(self):
        print("use commands: setparam, info, callhh, callsj, callboth, readraw, readjson, viewlist, select, help")
        print("""
                setparam - dialog for setting major parameters for calling API
                info - print actual parameters for calling API
                callhh - request API HeadHunter, write raw_data and write json data for searching
                calljs - request API SuperJob, write raw_data and write json data for searching
                callboth - request API HeadHunter and SuperJob, write raw_data and write json data
                readraw - reread raw data (without calling API)
                readjson - reread json data (without calling API)
                viewlist - print list of vacancies (no more than MAX_COUNT... in config file)
                select - set filters to select vacancies and printing filtered data
                """)