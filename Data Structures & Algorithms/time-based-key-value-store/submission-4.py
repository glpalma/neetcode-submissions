class TimeMap:

    def __init__(self):
        self.memory = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.memory.get(key):
            self.memory[key] = []

        self.memory[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.memory.get(key):
            return ""

        values = self.memory.get(key)
        res = ""
        l = 0
        r = len(values) - 1

        while l <= r:
            m = (l+r)//2
            currTime = values[m][0]

            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1

        return res
        
