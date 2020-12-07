from runners import day1, day2, day3, day4, day5, day6, day7

day_switch = {
        1: day1.execute_part,
        2: day2.execute_part,
        3: day3.execute_part,
        4: day4.execute_part,
        5: day5.execute_part,
        6: day6.execute_part,
        7: day7.execute_part
    }


def run(day, part):
    return day_switch[day](part)
