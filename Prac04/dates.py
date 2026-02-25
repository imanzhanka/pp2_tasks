from datetime import datetime, timedelta

# 1 Subtract five days from current date
today = datetime.now()
five_days_ago = today - timedelta(days=5)
print("1. Five days ago:", five_days_ago.strftime("%Y-%m-%d"))

#2 Print yesterday, today, tomorrow

yesterday  = today - timedelta(days=1)
tomorrow   = today + timedelta(days=1)
print("\n2. Yesterday :", yesterday.strftime("%Y-%m-%d"))
print("   Today     :", today.strftime("%Y-%m-%d"))
print("   Tomorrow  :", tomorrow.strftime("%Y-%m-%d"))

#3 Drop microseconds from datetime

now_with_microseconds    = datetime.now()
now_without_microseconds = now_with_microseconds.replace(microsecond=0)
print("\n3. With microseconds   :", now_with_microseconds)
print("   Without microseconds:", now_without_microseconds)

#4
date1 = datetime(2024, 1, 1, 8, 0, 0)
date2 = datetime(2024, 1, 3, 10, 30, 0)
difference_in_seconds = (date2 - date1).total_seconds()
print("\n4. Date 1             :", date1)
print("   Date 2             :", date2)
print("   Difference (secs)  :", difference_in_seconds)