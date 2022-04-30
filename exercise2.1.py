# Code that checks the number of passwords in a file that comply the specified policy
# Each line has the following structure:
#          <min_times>-<max_times> <letter>: <password>

import sys


class Policy:
    def __init__(self, min_times, max_times, target, password):
        """
        Constructor class

        :param min_times: minimum number of times the letter has to appear
        :param max_times: maximum numner of times the letter has to appear
        :param target: letter to check in the password
        :param password: password to check
        """
        # add 1 value to max_times to include it in range
        self.times = range(min_times, max_times + 1)
        self.target = target
        self.password = password

    def check_password(self):
        """
        Check if the password follows the specified policy
        """
        counter = 0
        for letter in self.password:
            if letter == self.target:
                counter += 1

        # check if the target letter appears the specified number of times
        return counter in self.times


def main(args):
    """
    Main function

    Arguments:
    :param args: path of the input file
    """
    correct_counter = 0

    if len(args) < 1:
        print("Missing input file argument")
        return 1

    # read the input file line by line
    with open(args[0], "r") as file:
        for line in file:
            # remove \n character
            line = line.strip()

            [max_min, target, password] = line.split(" ")
            [min, max] = max_min.split("-")

            # create a policy with the line info
            policy = Policy(int(min), int(max), target[0], password)

            # check if the password complies with the policy
            if policy.check_password():
                correct_counter += 1

    print("{} correct passwords.".format(correct_counter))


if __name__ == '__main__':
    main(sys.argv[1:])
