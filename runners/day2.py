import tools.common
from scripts.password_validator import PasswordValidator


def execute_part(part):
    input_text = tools.common.get_input(2, 1)
    if part == 1:
        return [PasswordValidator(entry).validate_password() for entry in input_text].count(True)
    if part == 2:
        return [PasswordValidator(entry, policy='position').validate_password() for entry in input_text].count(True)
