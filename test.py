import pandas as pd
import datetime
import calendar

print("TASK 1")

df = pd.read_excel(r"filename")

dfs = (list(map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S.%f'), df['STARTDATE'])))  # working

for i in dfs:
    my_time = i
    time_con = datetime.datetime.strptime(my_time, '%Y-%m-%d %H:%M:%S.%f')
    microsecs = time_con.microsecond
    final_time = calendar.timegm(time_con.timetuple()) * 1000000 + microsecs
    print(final_time)




