class MyHashSet:

    def __init__(self):
        self.thing = []

    def add(self, key: int) -> None:
        for n in self.thing:
            if n == key:
                return
        self.thing.append(key)

    def remove(self, key: int) -> None:
        print("remove", key, "from", self.thing)
        for i in range(len(self.thing)):
            if self.thing[i] == key:
                for j in range(i, len(self.thing) - 1):
                    self.thing[j] = self.thing[j+1]
                print(self.thing)
                self.thing = self.thing[:-1]
                print(self.thing)
                break

    def contains(self, key: int) -> bool:
        print("lf", key, "in", self.thing)
        for n in self.thing:
            if n == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)