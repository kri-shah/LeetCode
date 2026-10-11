class BusBooking:

    def __init__(self, n: int):
        self.seats = [[0] * 4 for _ in range(n + 1)]
        self.middle_seats = 0
        self.window_seats = 0
        self.map = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3
        }
        self.total = 0

    def toggle(self, seat: str) -> None:
        col, row = self.map[seat[0:1]], int(seat[1:])
        
        if self.seats[row][col] == 0:
            if col == 1 or col == 2:
                self.seats[row][col] = 1
                self.total += 1
                self.middle_seats += 1
            else:
                if col == 0:
                    if self.seats[row][col + 1]:
                        self.seats[row][col] = 3
                        self.total += 3
                    else:
                        self.seats[row][col] = 1
                        self.total += 1
                else:
                    if self.seats[row][col - 1]:
                        self.seats[row][col] = 3
                        self.total += 3
                    else:
                        self.seats[row][col] = 1
                        self.total += 1
                self.window_seats += 1
        else:
            self.total -= self.seats[row][col]
            self.seats[row][col] = 0
            if col == 1 or col == 2:
                self.middle_seats -= 1
            else:
                self.window_seats -= 1

    def getTotalTime(self) -> int:
        return self.total

    def getMinTime(self) -> int:
        return self.window_seats + self.middle_seats

# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()
