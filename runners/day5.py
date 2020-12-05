import tools.common
from scripts.boarding_pass_scanner import BoardingPassScanner


def execute_part(part):
    input_text = tools.common.get_input(5, 1)
    input_text.sort(key=lambda entry: entry.replace('F', 'A'))
    if part == 1:
        boarding_pass = BoardingPassScanner(input_text[-1])
        return boarding_pass.get_seat_id()
    if part == 2:
        boarding_pass = BoardingPassScanner(input_text[0])
        current_id = 0
        for boarding_pass_string in input_text:
            boarding_pass = BoardingPassScanner(boarding_pass_string)
            old_id, current_id = current_id, boarding_pass.get_seat_id()
            if current_id-old_id == 2:
                return old_id + 1
