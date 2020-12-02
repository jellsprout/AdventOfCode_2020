from runners import day1, day2

day_switch = {
        1: day1.execute_part,
        2: day2.execute_part
    }


def run(day, part):
    return day_switch[day](part)
