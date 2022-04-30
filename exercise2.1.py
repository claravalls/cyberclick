# Code that checks the number of passwords in a file that comply the specified policy
# Each line has the following structure:
#          <min_times>-<max_times> <letter>: <password>

import sys
import policy


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
            rules = policy.Policy(int(min), int(max), target[0], password)

            # check if the password complies with the policy
            if rules.check_password_1():
                correct_counter += 1

    print("{} correct passwords.".format(correct_counter))


if __name__ == '__main__':
    main(sys.argv[1:])
