class RandomizedSet:

    def __init__(self):
        self.sett = {}
        self.size = 0
        

    def insert(self, val: int) -> bool:
        if val in self.sett:
            return False
        else:
            self.sett[val] = 1
            self.size += 1
            return True
        

    def remove(self, val: int) -> bool:
        if val not in self.sett:
            return False
        else:
            del self.sett[val]
            self.size -= 1
            return True

    def getRandom(self) -> int:
        index = random.randint(0, self.size -1)
        return list(self.sett.keys())[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()