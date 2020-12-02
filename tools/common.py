from pathlib import Path


def get_input(day, part):
    return load_input(get_file_path(day, part))


def load_input(file):
    with open(file) as f:
        output = f.readlines()
    return output


def get_file_path(day, part):
    filename = f'{day}_{part}'
    p = Path('.')
    return p.joinpath('input_files').joinpath(filename)


def convert_text_to_list_of_integers(input_text):
    return list(map(int, input_text))
