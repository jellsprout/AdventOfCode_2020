from runners import day1

day_switch = {
        1: day1.execute_part,
        2: 'test'
    }


def run(day, part):
    return day_switch[day](part)
