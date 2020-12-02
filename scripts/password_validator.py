class PasswordValidator:
    def __init__(self, password_object_string, policy='range'):
        password_object = password_object_string.split()
        self.password_string = password_object[2].strip()
        self.policy_first_number = 0
        self.policy_second_number = 0
        self.policy_character = ''
        self.process_policy(password_object[0], password_object[1])
        self.policy = policy

    def process_policy(self, unprocessed_character_limits, unprocessed_policy_character):
        processed_limits = unprocessed_character_limits.split('-')
        self.policy_first_number = int(processed_limits[0])
        self.policy_second_number = int(processed_limits[1])
        self.policy_character = unprocessed_policy_character[0]

    def validate_password(self):
        password_validation_selector = {
            'range': self.validate_password_range_policy,
            'position': self.validate_password_position_policy
        }
        return password_validation_selector[self.policy]()

    def validate_password_range_policy(self):
        number_of_occurances = self.password_string.count(self.policy_character)
        return self.policy_first_number <= number_of_occurances <= self.policy_second_number

    def validate_password_position_policy(self):
        characters_in_positions = [self.password_string[self.policy_first_number-1],
                                   self.password_string[self.policy_second_number-1]]
        return characters_in_positions.count(self.policy_character) == 1
