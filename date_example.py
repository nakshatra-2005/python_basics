#birthday
import datetime
today = datetime.date.today()
print("today's date:", today)
birthday = datetime.date(2006, 1, 26)
print("You are born on :", birthday)
days_since_birthday = (today - birthday).days
print("here are the days you have been alive:", days_since_birthday)

#mail identifying
import re
text = "'My mail ID is nakshatrafrint@gmail.com or Lidvijanelaveni@gmail.com or nakshatra@mail.com'"
pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
emails = re.findall(pattern, text)
print(emails)

#Adding days to the today's date
from datetime import date, timedelta
today = date.today()
future_date = today + timedelta(days=980)
print("100 days from today:", future_date)

#  Get day, month, and year from a specific date
from datetime import date
d = date(2025, 5, 26)
print("Day:", d.day)
print("Month:",d.month)
print("Year:", d.year)

# Format the current date and time
from datetime import datetime
now = datetime.now()
formatted = now.strftime("%A, %d %B %Y %I:%M %p")
print("formatted date and time:", formatted)

# Find the difference between two dates
from datetime import date
date1 = date(2025, 5, 26)
date2 = date(2023, 7, 28)
diff = date1 - date2
print("difference in days:",diff.days)

# Given your birthdate (April 5, 2005), calculate your exact age in years, months, and days (approximate).
from datetime import date

from datetime import date

# Your birthdate
birth_date = date(2005, 4, 5)

# Today's date
today = date.today()

# Calculate difference
years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

# Adjust for negative months/days
if days < 0:
    months -= 1
    # Get days in previous month
    from calendar import monthrange
    prev_month_days = monthrange(today.year, today.month - 1)[1]
    days += prev_month_days

if months < 0:
    years -= 1
    months += 12

# Output
print(f"Your age is {years} years, {months} months, and {days} days.")


