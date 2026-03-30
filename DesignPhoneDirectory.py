class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.not_assigned = {num for num in range(maxNumbers)}

    def get(self) -> int:
        if not self.not_assigned:
            return -1
        
        return self.not_assigned.pop()


    def check(self, number: int) -> bool:
        return number in self.not_assigned
            

    def release(self, number: int) -> None:
        self.not_assigned.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
