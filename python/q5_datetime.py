# Hint:  use Google to find python function
import datetime
def days (start, end, date_format):
    start = datetime.datetime.strptime(start, date_format)
    end = datetime.datetime.strptime(end, date_format)

    return (end - start).days

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

print(days(date_start, date_stop, '%m-%d-%Y'))

####b)
date_start = '12312013'
date_stop = '05282015'

print(days(date_start, date_stop, '%m%d%Y'))


####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

print(days(date_start, date_stop, '%d-%b-%Y'))
