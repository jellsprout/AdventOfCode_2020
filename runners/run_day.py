from runners import day1, day2, day3

day_switch = {
        1: day1.execute_part,
        2: day2.execute_part,
        3: day3.execute_part
    }


def run(day, part):
    return day_switch[day](part)
