# Code that checks the number of passwords in a file that comply the specified policy
# Each line has the following structure:
#   POLICY 1   =   <min_times>-<max_times> <letter>: <password>
#   POLICY 2   =   <position1>-<position2> <letter>: <password>

import sys
import policy


def main(args):
    """
    Main function

    Arguments:
    :param args: 
        1 - path of the input file
        2 - type of password check
    """
    correct_counter = 0

    if len(args) < 2:
        print("Missing arguments")
        return 1

    input_file = args[0]
    policy_type = int(args[1])

    # read the input file line by line
    with open(input_file, "r") as file:
        for line in file:
            # remove \n character
            line = line.strip()

            [max_min, target, password] = line.split(" ")
            [min, max] = max_min.split("-")

            # create a policy with the line info
            rules = policy.Policy(int(min), int(max), target[0], password)

            # check if the password complies with the policy
            if rules.check_password(policy_type):
                correct_counter += 1

    print("{} correct passwords.".format(correct_counter))


if __name__ == '__main__':
    main(sys.argv[1:])
