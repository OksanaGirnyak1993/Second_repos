from datetime import datetime, timedelta
def get_upcoming_birthdays(users_list):
    today = datetime.today().date()
    birthdays = [] 
    for user in users_list:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)
        if birthday < today:
            birthday = birthday.replace(year=today.year+1)
        days_birth = (birthday - today).days
        if 0 <= days_birth <= 7:
            if birthday.weekday() in [5, 6]:
                monday = today + timedelta(days=(7-today.weekday()) + 1)
                cong_day = monday.strftime("%Y.%m.%d")
            else:
                cong_day = birthday.strftime("%Y.%m.%d")
            birthdays.append({
                "name": user["name"], 
                "date": cong_day
            })
    return birthdays  

users = [
    {"name": "John Doe", "birthday": "1985.08.15"},
    {"name": "Jane Smith", "birthday": "1990.03.13"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)     
