class Policy:
    def __init__(self, first_num, second_num, target, password):
        """
        Constructor class

        :param first_num: minimum number of times the letter has to appear or position of the target letter
        :param second_num: maximum number of times the letter has to appear or position of the target letter
        :param target: letter to check in the password
        :param password: password to check
        """
        self.first_num = first_num
        self.second_num = second_num
        self.target = target
        self.password = password

    def check_password(self, policy):
        """
        Check if the password follows the specified policy

        Arguments
        :param policy: policy type (1 or 2) to apply
        """
        counter = 0

        if policy == 1:
            for letter in self.password:
                if letter == self.target:
                    counter += 1

            # check if the target letter appears the specified number of times
            times = range(self.first_num, self.second_num + 1)
            return counter in times

        else:
            # check if the letter appears in the position1 specified or in the position2, but not in both
            return (self.password[self.first_num - 1] == self.target) != (self.password[self.second_num - 1] == self.target)
