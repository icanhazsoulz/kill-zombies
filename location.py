def get_data(filename):
    f = open(filename, 'r')
    numbers = map(int, f.readlines())
    f.close()
    return numbers


class Location:
    def __init__(self, filename):
        self.numbers = get_data(filename)

    def get_code(self):
        low = high = 0
        for number in self.numbers:
            if number < 100:
                low += number
            else:
                high += number

        return 2 * low + high
