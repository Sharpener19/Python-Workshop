# Simple Python program which keeps track of 

from datetime import date

def days_passed_since(year, month, day):
    start_date = date(year, month, day)
    today = date.today()
    difference = today - start_date
    return difference.days

# consumes user input and outputs days passed since reference point
start_year, start_month, start_day = input("Enter the starting year, month, date in numerical format separated by a space: ").split()
start_year, start_month, start_day = int(start_year), int(start_month), int(start_day)
print(days_passed_since(start_year, start_month, start_day))

# Keep track of days passed from custom markers {T1 ... T6} in dict
curr_dawn_tiers_dict = {"T1": days_passed_since(2025, 7, 8),
                        "T2": days_passed_since(2025, 7, 13),
                        "T3": days_passed_since(2025, 7, 31),
                        "T4": days_passed_since(2025, 8, 7),
                        "T5": days_passed_since(2025, 10, 12),
                        "T6": days_passed_since(2025, 10, 14)}

#print(curr_dawn_tiers_dict)