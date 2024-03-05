class CircularBuffer:
    def __init__(self, maximum_size):
        self.__maximum_size = maximum_size
        self.__items = []

    def add(self, item):
        self.__items.append(item)
        if len(self.__items) > self.__maximum_size:
            del self.__items[0]

    def __getitem__(self, index):
        return self.__items[index]
    
    def __len__(self):
        return len(self.__items)