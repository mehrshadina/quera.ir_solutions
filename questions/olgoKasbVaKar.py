class FibonacciSubsetSum:
    def __init__(self, n, prices, sub_size):
        self.n = n
        self.prices = prices
        self.sub_size = sub_size
        self.fib_sequence = self.generate_fibonacci_sequence(n)
        self.last_number = self.fib_sequence[-1]
        self.combinations = []
        self.maximum_ways = 0
    
    def generate_fibonacci_sequence(self, length):
        fib = [0, 1]
        for i in range(2, length + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib
    
    def generate_combinations(self, start=0, current_combination=[]):
        if len(current_combination) == self.sub_size:
            self.combinations.append(current_combination[:])
            return
        for i in range(start, len(self.prices)):
            current_combination.append(self.prices[i])
            self.generate_combinations(i + 1, current_combination)
            current_combination.pop()
    
    def count_ways(self, subset, target, temp_set):
        if target == 0:
            return 1
        elif target < 0:
            return 0
        if target in temp_set:
            return temp_set[target]
        total_ways = 0
        for price in subset:
            delta = target - price
            total_ways += self.count_ways(subset, delta, temp_set)
        temp_set[target] = total_ways
        return total_ways
    
    def calculate_maximum_ways(self):
        self.generate_combinations()
        for sub in self.combinations:
            temp_set = {}
            ways = self.count_ways(sub, self.last_number, temp_set)
            if ways > self.maximum_ways:
                self.maximum_ways = ways
        return self.maximum_ways if self.maximum_ways > 0 else "can't reach to this number!"
    
    def get_result(self):
        return self.calculate_maximum_ways()

n = int(input())
prices = list(map(int, input().split()))
subset_size = int(input())

fib_subset_sum = FibonacciSubsetSum(n, prices, subset_size)
result = fib_subset_sum.get_result()
print(result)
