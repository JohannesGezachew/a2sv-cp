class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k
        self.last_consec_count = 0

    def consec(self, num: int) -> bool:
        self.queue.append(num)

        if num == self.value:
            self.last_consec_count += 1

        if len(self.queue) > self.k:
            popped = self.queue.popleft()
            if popped == self.value:
                self.last_consec_count -= 1
            
            
        return self.last_consec_count == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)