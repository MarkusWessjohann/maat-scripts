## Basic mathematical statistics (yes, I know - NumPy would be better, 
## but I want to make the scripts stand-alone for now).

class DescriptiveStats(object):
    def __init__(self, name, all_values):
        self.name = name
        self._all_values = all_values
        self.total = sum(all_values)
        self.n_revs = len(all_values)
	self.code_lines = self.n_revs 
        self.emty_lines = 0

    def __init__(self, name, empty_lines, all_values):
        self.name = name
        self._all_values = all_values
        self.total = sum(all_values)
        self.n_revs = len(all_values)
	self.empty_lines = empty_lines

    def mean(self):
        return self.total / float(self._protected_n())

    def max_value(self):
        return max(self._all_values)

    def min_value(self):
        return min(self._all_values)

    def code_lines(self):
        return (self.n_revs - self.empty_lines)

    def line_sizeComplexity(self):
        oldsize = 0
        sizeComplexity = 0
        for newsize in self._all_values:
           if oldsize != newsize:
                sizeComplexity = sizeComplexity + 1
        return sizeComplexity


    def sd(self):
        from math import sqrt
        std = 0
        mean = self.mean()
        for a in self._all_values:
            std = std + (a - mean)**2
        std = sqrt(std / float(self._protected_n()))
        return std

    def _protected_n(self):
        n = self.n_revs
        return max(n, 1)
