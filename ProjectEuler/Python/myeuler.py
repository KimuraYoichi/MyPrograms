class PrimeFactorization:
    def __init__(self, n):
        self.factor = []
        self.n = n

    def primedivisor(self):
        # def __init__(self, n):
        #     self.factor = []
        #     self.n = n
        for i in range(2, self.n):
            while self.n % i == 0:
                self.factor.append(i)
                self.n = int(self.n / i)
        if self.n > 1:
            self.factor.append(self.n)
        return self.factor


class Spam:
    def __init__(self, ham, egg):
        self.ham = ham
        self.egg = egg

    def output(self):
        sum = self.ham + self.egg
        print("{0}".format(sum))


class Alph2num:
    def __init__(self, alph):
        self.alph = alph
    def alph2num(self):
        self.numalph = []
        for ss in self.alph:
            self.numalph.append(ord(ss) - ord('A') + 1)
        return self.numalph
