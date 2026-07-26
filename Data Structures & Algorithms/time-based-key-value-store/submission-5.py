from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(dict) # { key -> hashMap{ timestamp -> value } }

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.timeMap[key]:
            return self.timeMap[key][timestamp]
        elif not self.timeMap[key]:
            return ""

        timestamps = list(self.timeMap[key].keys())
        l, r = 0, len(timestamps) - 1
        while l < r:
            m = l + (r - l + 1) // 2
            if timestamps[m] <= timestamp:
                l = m
            else:
                r = m - 1
        return "" if timestamps[l] > timestamp else self.timeMap[key][timestamps[l]]
