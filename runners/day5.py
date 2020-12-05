import tools.common
import scripts.basic
from scripts.boarding_pass_scanner import BoardingPassScanner


def execute_part(part):
    input_text = tools.common.get_input(5, 1)
    input_text.sort(key=lambda entry: entry.replace('F', 'A'))
    if part == 1:
        boarding_pass = BoardingPassScanner(input_text[-1])
        return boarding_pass.get_seat_id()
    if part == 2:
        boarding_pass = BoardingPassScanner(input_text[0])
        lowest_id = boarding_pass.get_seat_id()

        def compare_ids(curent_index):
            current_boarding_pass = BoardingPassScanner(input_text[curent_index])
            return (curent_index + lowest_id) - current_boarding_pass.get_seat_id()

        return scripts.basic.binary_search(0, len(input_text), compare_ids) + lowest_id + 1
