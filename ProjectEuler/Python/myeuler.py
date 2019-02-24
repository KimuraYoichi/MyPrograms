class PrimeFactorization:
    def __init__(self, n):
        self.factor = []
        self.n = n

    def primedivisor(self):
        for i in range(2, self.n):
            while self.n % i == 0:
                self.factor.append(i)
                self.n = int(self.n / i)
        if self.n > 1:
            self.factor.append(self.n)
        return self.factor
