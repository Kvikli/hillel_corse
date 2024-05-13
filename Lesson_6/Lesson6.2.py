def seconds_to_time(seconds):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    time_str = "{:02d}:{:02d}:{:02d}:{:02d}".format(int(days), int(hours), int(minutes), int(seconds))

    if days == 1:
        day_str = "день"
    elif days in range(2, 5):
        day_str = "дні"
    else:
        day_str = "днів"

    return f"{int(days)} {day_str}, {time_str}"


seconds_input = int(input("Введіть кількість секунд: "))
if seconds_input >= 0 and seconds_input < 8640000:
    print("Результат:", seconds_to_time(seconds_input))
else:
    print("Введіть число більше або дорівнює 0 і менше ніж 8640000.")
