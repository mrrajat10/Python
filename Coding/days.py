arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = input("Enter the date in dd-mm-yyyy:")
tokens = date.split("-")
month = int(tokens[1])
if (1 <= month) and (month >= 12):
    print(f"No of days in month have {arr[month-1]}")
