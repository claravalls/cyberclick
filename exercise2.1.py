#
import sys


class Policy:
    def __init__(self, max_times, min_times, letter, password):
        self.times = [max_times, min_times]
        self.target = letter
        self.password = password

    def check_password(self):
        counter = 0
        for letter in self.password:
            if letter == self.target:
                counter += 1

        return self.times[0] >= counter and counter <= self.times[1]


def main(args):
    print(args)


if __name__ == '__main__':
    main(sys.argv)
