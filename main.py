import runners.run_day
import argparse


def run_day(day, part=1):
    return runners.run_day.run(day, part)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Enter day and part')
    parser.add_argument('day')
    parser.add_argument('part')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    arguments = parse_arguments()
    print(run_day(day=int(arguments.day), part=int(arguments.part)))
