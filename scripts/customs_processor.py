import string


def convert_string_to_set(string):
    output_set = set()
    for letter in string:
        output_set.add(letter)
    return output_set


class CustomsProcessor:
    def __init__(self, input_text):
        self.answer_sheets = input_text.split('\n')
        self.group_answers = set()
        self.shared_answers = set(string.ascii_lowercase)
        self.count_total_answers()

    def count_total_answers(self):
        for sheet in self.answer_sheets:
            letters_set = convert_string_to_set(sheet)
            self.group_answers |= letters_set
            self.shared_answers &= letters_set

    def count_total_group_answers(self):
        return len(self.group_answers)

    def count_shared_group_answers(self):
        return len(self.shared_answers)

