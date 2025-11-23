from heapq import heappush, heappop
import itertools

class PriorityQueue:
    def __init__(self):
        self.pq = []                   # heap
        self.entry_finder = {}         # mapeia task -> entry
        self.counter = itertools.count()

    def __len__(self):
        return len(self.pq)

    def add_task(self, priority, task):
        if task in self.entry_finder:
            self.update_priority(priority, task)
            return

        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)    

    def update_priority(self, priority, task):
        entry = self.entry_finder[task]
        count = next(self.counter)
        entry[0], entry[1] = priority, count


    def pop_task(self):
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task in self.entry_finder:
                del self.entry_finder[task]
                return priority, task

        raise KeyError('pop from an empty priority queue')
