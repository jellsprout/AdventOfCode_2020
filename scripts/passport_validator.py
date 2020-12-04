import re


standard_mandatory_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
standard_accepted_eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def validate_value_string_range(value, min_value, max_value):
    if not value.isdigit():
        return False
    else:
        return min_value <= int(value) <= max_value


def run_byr_validation(value):
    return validate_value_string_range(value, 1920, 2002)


def run_iyr_validation(value):
    return validate_value_string_range(value, 2010, 2020)


def run_eyr_validation(value):
    return validate_value_string_range(value, 2020, 2030)


def run_hgt_validation(value):
    unit = re.search(r'\D+', value)
    height = re.search(r'\d+', value)
    if unit and height:
        if unit.group(0) == 'cm':
            return validate_value_string_range(height.group(0), 150, 193)
        elif unit.group(0) == 'in':
            return validate_value_string_range(height.group(0), 59, 76)
    return False


def run_hcl_validation(value):
    return re.fullmatch(r'#[0-9a-f]{6}', value)


def run_ecl_validation(value, accepted_eye_colors=None):
    if accepted_eye_colors is None:
        accepted_eye_colors = standard_accepted_eye_colors
    return value in accepted_eye_colors


def run_pid_validation(value):
    return value.isdigit() and len(value) == 9


def validate_value(field, value):
    check_to_run = {'byr': run_byr_validation,
                    'iyr': run_iyr_validation,
                    'eyr': run_eyr_validation,
                    'hgt': run_hgt_validation,
                    'hcl': run_hcl_validation,
                    'ecl': run_ecl_validation,
                    'pid': run_pid_validation}
    return check_to_run[field](value)


class PassportValidator:
    def __init__(self, passport_string):
        self.passport_raw = passport_string
        passport_split = re.split(r'\s', self.passport_raw)
        self.passport = {}
        for s in passport_split:
            [key, value] = s.split(':')
            self.passport[key] = value
        self.passport_fields = set()
        self.convert_fields_to_set()

    def convert_fields_to_set(self):
        for key in self.passport:
            self.passport_fields.add(key)

    def validate_mandatory_fields(self, mandatory_fields=None):
        if mandatory_fields is None:
            mandatory_fields = standard_mandatory_fields
        return mandatory_fields <= self.passport_fields

    def validate_field_values(self, mandatory_fields=None):
        if mandatory_fields is None:
            mandatory_fields = standard_mandatory_fields
        if not self.validate_mandatory_fields():
            return False
        for field in mandatory_fields:
            if not validate_value(field, self.passport[field]):
                return False
        return True
