from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    if not users:
        return {}

    today = date.today()
    this_week = {}
    current_day_of_week = today.weekday()

    
    day_of_week_names = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    for user in users:
        user_name = user['name']
        birthday = user['birthday']
        next_birthday = birthday.replace(year=today.year)
        if next_birthday < today:
            next_birthday = birthday.replace(year=today.year + 1)
        day_of_week = birthday.weekday()

        if today <= next_birthday <= (today + timedelta(days=7)):
            if today <= next_birthday < (today + timedelta(days=5)):  # Від понеділка до п'ятниці
                day_name = day_of_week_names[day_of_week]  # Отримайте назву дня тижня
                if day_name in this_week:
                    this_week[day_name].append(user_name)
                else:
                    this_week[day_name] = [user_name]
            elif (today + timedelta(days=5)) <= next_birthday <= (today + timedelta(days=6)):  # Субота
                if 'Monday' in this_week:
                    this_week['Monday'].append(user_name)  # Перенесіть на понеділок наступного тижня
                else:
                    this_week['Monday'] = [user_name]
            elif (today + timedelta(days=6)) <= next_birthday:  # Неділя
                if 'Monday' in this_week:
                    this_week['Monday'].append(user_name)  # Перенесіть на понеділок наступного тижня
                else:
                    this_week['Monday'] = [user_name]

    print(this_week)
    return this_week

if __name__ == "__main":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)

    for day_of_week, names in result.items():
        print(f"{day_of_week}: {', '.join(names)}")