# Hint:  use Google to find python function

import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

date_start = datetime.datetime.strptime(date_start, '%m-%d-%Y')
date_stop = datetime.datetime.strptime(date_stop, '%m-%d-%Y')
print(date_stop - date_start) # 937 days, 0:00:00

# confirm result:
diff = datetime.timedelta(days = 937)
print(date_start + diff) # 2015-07-28 00:00:00

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_start = datetime.datetime.strptime(date_start, '%m%d%Y')
date_stop = datetime.datetime.strptime(date_stop, '%m%d%Y')
print(date_stop - date_start) # 513 days, 0:00:00

# confirm result:
diff = datetime.timedelta(days = 513)
print(date_start + diff) # 2015-05-28 00:00:00

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_start = datetime.datetime.strptime(date_start, '%d-%b-%Y')
date_stop = datetime.datetime.strptime(date_stop, '%d-%b-%Y')
print(date_stop - date_start) # 7850 days, 0:00:00

# confirm result:
diff = datetime.timedelta(days = 7850)
print(date_start + diff) # 2015-07-14 00:00:00
