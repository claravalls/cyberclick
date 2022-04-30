class Policy:
    def __init__(self, min_times, max_times, target, password):
        """
        Constructor class

        :param min_times: minimum number of times the letter has to appear
        :param max_times: maximum numner of times the letter has to appear
        :param target: letter to check in the password
        :param password: password to check
        """
        self.min_times = min_times
        self.max_times = max_times
        self.target = target
        self.password = password

    def check_password_1(self):
        """
        Check if the password follows the specified policy
        """
        counter = 0
        for letter in self.password:
            if letter == self.target:
                counter += 1

        # check if the target letter appears the specified number of times
        times = range(self.min_times, self.max_times + 1)
        return counter in times
