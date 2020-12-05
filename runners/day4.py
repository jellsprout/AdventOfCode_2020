import tools.common
from scripts.passport_validator import PassportValidator


def load_input_overwrite(file):
    with open(file) as f:
        output = f.read().split('\n\n')
    return output


def execute_part(part):
    tools.common.load_input = load_input_overwrite
    input_text = tools.common.get_input(4, 1)
    if part == 1:
        total_valid_passports = 0
        for passport in input_text:
            validator = PassportValidator(passport)
            total_valid_passports += validator.validate_mandatory_fields()
        return total_valid_passports
    if part == 2:
        total_valid_passports = 0
        for passport in input_text:
            validator = PassportValidator(passport)
            total_valid_passports += validator.validate_field_values()
        return total_valid_passports
