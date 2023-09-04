from datetime import date, datetime, timedelta


days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def get_birthdays_per_week(users):
    return_dict = {}
    current_date = date.today()
    date_start_week = current_date - timedelta(days=1)
    date_end_week = current_date + timedelta(days=7)
    if len(users) == 0:
        return return_dict
    for user in users:
        date_of_birthday = user['birthday']
        birthday_in_current_year = date(year=current_date.year, month=date_of_birthday.month, day=date_of_birthday.day)
        if date_of_birthday.month == 1:
            birthday_in_current_year = date(year=current_date.year + 1,
                                            month=date_of_birthday.month, day=date_of_birthday.day)
        if date_start_week < birthday_in_current_year < date_end_week:
            weekday_birthday = birthday_in_current_year.weekday()
            if weekday_birthday == 5 or weekday_birthday == 6:
                if days_name.get(0) in return_dict:
                    return_dict[days_name.get(0)].append(user['name'])
                else:
                    return_dict[days_name.get(0)] = [user['name']]
            else:
                if days_name.get(weekday_birthday) in return_dict:
                    return_dict[days_name.get(weekday_birthday)].append(user['name'])
                else:
                    return_dict[days_name.get(weekday_birthday)] = [user['name']]
    return return_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # 'Виводимо результат'
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
