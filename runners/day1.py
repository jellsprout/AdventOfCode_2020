import tools.common
import scripts.basic


def execute_part(part):
    input_text = tools.common.get_input(1, 1)
    if part == 1:
        input_numbers = tools.common.convert_text_to_list_of_integers(input_text)
        i, j = scripts.basic.find_sum(input_numbers, 2020)
        return i*j
    if part == 2:
        input_numbers = tools.common.convert_text_to_list_of_integers(input_text)
        output_numbers = scripts.basic.find_sum(input_numbers, 2020, 3)
        return scripts.basic.get_product(output_numbers)
