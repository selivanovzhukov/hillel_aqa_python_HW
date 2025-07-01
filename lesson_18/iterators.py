from lesson_18.generator import generate_even_nums


class ReverseList:

    def __init__(self, some_list: list):
        self._list = some_list
        self._index = len(some_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= 0:
            value = self._list[self._index]
            self._index -= 1
            return value
        else:
            raise StopIteration


my_list = list(generate_even_nums(10))
for item in ReverseList(my_list):
    print(item)

reversed_list = list(ReverseList(my_list))
print(reversed_list)


class EvenNumIter:

    def __init__ (self, n: int):
        self._n = n
        self._start_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self._start_num <= self._n:
            if self._start_num % 2 == 0:
                value = self._start_num
                self._start_num += 1
                return value
            self._start_num += 1
        raise StopIteration


if __name__ == "__main__":
    my_list = list(generate_even_nums(10))
    for item in ReverseList(my_list):
        print(item)

    reversed_list = list(ReverseList(my_list))
    print(reversed_list)

    for num in EvenNumIter(10):
        print(num)
