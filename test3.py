import calendar
from datetime import datetime

# 获取当前日期
now = datetime.now()
year = now.year
month = now.month + 1

# 打印当前月份的日历
print(f"{year}年{month}月".center(20))
print(calendar.month(year, month))