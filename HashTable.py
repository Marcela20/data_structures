class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        sum_of_chars = 0
        for char in key:
            sum_of_chars += ord(char)

        return sum_of_chars % self.max

    def __getitem__(self, key):
        for idx, elem in enumerate(self.arr[self.get_hash(key)]):
            if elem[0] == key:
                return elem[1]



    # def __setitem__(self, key, value): #linear search
    #     if self.arr[self.get_hash(key)] == []:
    #         self.arr[self.get_hash(key)].append((key, value))
    #     else:
    #         for i in range(self.get_hash(key)+1, len(self.arr) + 1):
    #             indicator = None
    #             if self.arr[i] == []:
    #
    #                 self.arr[i].append((key, value))
    #                 indicator = True
    #                 break
    #             if not indicator:
    #                 for i in range(len(self.arr) + 1):
    #                     if self.arr[i] == []:
    #                         self.arr[i].append((key, value))
    #                         break

    def __setitem__(self, key, value):  # chaning
        if self.arr[self.get_hash(key)] == []:
            self.arr[self.get_hash(key)].append((key, value))
        elif self.arr[self.get_hash(key)] != []:
            for idx , elem in enumerate(self.arr[self.get_hash(key)]):
                if elem[0] == key:
                    self.arr[self.get_hash(key)][idx] = (key, value)
                    break
                else:
                    self.arr[self.get_hash(key)].append((key, value))




    def __delitem__(self, key):
        self.arr[self.get_hash(key)] = []
        return

    def print(self):
        print(self.arr)


t = HashTable()
t["march 6"] = 140
t["march 7"] = 130
t["march 7"] = 1200
t["march7 "] = 120000
print(t["march7 "])

# print(t.get_hash("march 6"))
# print(t.get_hash("march 7"))
# print(t.get_hash("march7 "))
# t.__delitem__("aa")
t.print()
