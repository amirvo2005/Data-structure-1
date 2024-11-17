class ArrayManager:
    def __init__(self):
        self.array = []

    def insert(self, index, value):
        if index < 0 or index > len(self.array):
            print("Index out of bounds.")
            return
        self.array.insert(index, value)
        print(f"Inserted {value} at index {index}. Current array: {self.array}")

    def delete_by_value(self, value):
        if value in self.array:
            index = self.array.index(value)
            self.array.remove(value)
            print(f"Deleted {value} from index {index}. Current array: {self.array}")
            return index
        else:
            print(f"Value {value} not found in the array.")
            return -1

    def delete_by_index(self, index):
        if index < 0 or index >= len(self.array):
            print("Index out of bounds.")
            return
        removed_value = self.array.pop(index)
        print(f"Deleted value {removed_value} from index {index}. Current array: {self.array}")

    def display(self):
        print(f"Current array: {self.array}")

    def append(self, value):
        self.array.append(value)
        print(f"Appended {value}. Current array: {self.array}")

    def reverse(self):
        self.array.reverse()
        print(f"Reversed array: {self.array}")

    def search_by_value(self, value):
        if value in self.array:
            index = self.array.index(value)
            print(f"Value {value} found at index {index}.")
            return index
        else:
            print(f"Value {value} not found in the array.")
            return -1
            