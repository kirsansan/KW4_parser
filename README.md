# KW4_parser
kw4 parser
written by Mr.K (aka Kirill.S)

This parser works with API HeadHunter and SuperJob 
It pull data from servers through the API
write data to files
have little ability for sort and filter data before display

this app have two parts
1. console version      (./main/main)
2. html-flask version   (./app.py)

for console version you can use next commands:
                setparam - dialog for setting major parameters for calling API
                info - print actual parameters for calling API
                callhh - request API HeadHunter, write raw_data and write json data for searching
                calljs - request API SuperJob, write raw_data and write json data for searching
                callboth - request API HeadHunter and SuperJob, write raw_data and write json data
                readraw - reread raw data (without calling API)
                readjson - reread json data (without calling API)
                viewlist - print list of vacancies (no more than MAX_COUNT... in config file)
                select - set filters to select vacancies and printing filtered data

for html version please set directory ./src as working dir for app.py