import tools.common
from scripts.customs_processor import CustomsProcessor


def load_input_overwrite(file):
    with open(file) as f:
        output = f.read().split('\n\n')
    return output


def execute_part(part):
    tools.common.load_input = load_input_overwrite
    input_text = tools.common.get_input(6, 1)
    if part == 1:
        total_answers = 0
        for customs_group in input_text:
            customs_processor = CustomsProcessor(customs_group)
            total_answers += customs_processor.count_total_group_answers()
        return total_answers
    if part == 2:
        total_answers = 0
        for customs_group in input_text:
            customs_processor = CustomsProcessor(customs_group)
            total_answers += customs_processor.count_shared_group_answers()
        return total_answers
