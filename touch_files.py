# Create fake backup files to test cleanup
import datetime
import os

days = 30
db_name = 'myproject'
today = datetime.datetime.now()

for day in range(0, days):
    date = today - datetime.timedelta(days=day)
    prefix = date.strftime("%Y-%m-%d_%H.%M.%S_")
    filename_sql = prefix + db_name + '.sql.gz'
    filename_media = prefix + db_name + '.media.tar.gz'
    print(filename_sql)
    os.system('touch %s' % filename_sql)
    print(filename_media)
    os.system('touch %s' % filename_media)
