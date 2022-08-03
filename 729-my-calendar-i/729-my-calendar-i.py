class MyCalendar:
    def __init__(self):
        self.schedules = []

    def book(self, start: int, end: int) -> bool:
        # print("*"*20)
        # print("aaaa  ", [start, end], "  aaaa")
        if len(self.schedules) == 0:
            self.schedules.append([start, end])
            # print(self.schedules)
            return True
        
        if end <= self.schedules[0][0]:
                self.schedules.insert(0, [start, end])
                # print(self.schedules)
                return True
    
        start_idx = 0
        for i in range(len(self.schedules)):
            schedule = self.schedules[i]
            # print(schedule, [start])
            if schedule[1] <= start:
                start_idx = i + 1
            else:
                break
        print(start_idx)

        if start_idx == 0:
            return False
        elif len(self.schedules) == start_idx:
            self.schedules.append([start, end])
            # print(self.schedules)
            return True
        elif end <= self.schedules[start_idx][0]:
            self.schedules.insert(start_idx, [start, end])
            # print(self.schedules)
            return True
        else:
            # print(self.schedules)
            return False
        
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)