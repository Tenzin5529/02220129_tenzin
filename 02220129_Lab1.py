
class CustomList:
    def __init__(self):
        self.capacity = 10
        self.array = [None] * self.capacity  
        self.size = 0
        print(f"Created new CustomList with capacity: {self.capacity}")
        print(f"Current size: {self.size}")

    def append(self, element):
        if self.size >= self.capacity:
            self.capacity *= 2
            new_array = [None] * self.capacity
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array
        self.array[self.size] = element
        self.size += 1
        print(f"Appended {element} to the list")

    def get(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of range")

    def set(self, index, element):
        if 0 <= index < self.size:
            self.array[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            raise IndexError("Index out of range")

    def size(self):
        return self.size

if __name__ == "__main__":
    custom_list = CustomList()
    custom_list.append(5)
    print(f"Element at index 0: {custom_list.get(0)}")
    custom_list.set(0, 10)
    print(f"Element at index 0: {custom_list.get(0)}")
    print(f"Current size: {custom_list.size}")
