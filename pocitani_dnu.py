day = input("Insert a day of the week (Mon, Tue, Wen, Thu, Fri, Sat, Sun): ")
number = int(input("Insert a number to be added to the day: "))
week = {"Mon":1, "Tue":2, "Wed":3, "Thu":4, "Fri":5, "Sat":6, "Sun":7}
if day not in week:
    print("Day doesnt exist")
else:
    today = week[day]
    result = (today + number -1) % 7 + 1
    for k, value in week.items():
        if value == result: 
            print(f"The following day after {number} day is going to be {k}")
        
