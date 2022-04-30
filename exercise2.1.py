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
    correct_counter = 0

    if len(args) < 1:
        print("Missing input file argument")
        return 1

    with open(args[0], "r") as file:
        for line in file:
            # remove \n character
            line = line.strip()

            [max_min, target, password] = line.split(" ")
            [max, min] = max_min.split("-")

            policy = Policy(int(max), int(min), target[0], password)
            if policy.check_password():
                correct_counter += 1

    print("{} correct passwords.".format(correct_counter))


if __name__ == '__main__':
    main(sys.argv[1:])
