class BoardingPassScanner:
    def __init__(self, boarding_pass_string):
        self.boarding_pass_string = boarding_pass_string.lower()
        self.boarding_pass_bin = self.boarding_pass_string.replace('f', '0').replace('b', '1').replace('l', '0')\
            .replace('r', '1')
        self.seat_id = int(self.boarding_pass_bin, 2)

    def get_seat_id(self):
        return self.seat_id
