class List:

    def __init__(self, arr):
        self.arr = arr

    def __repr__(self):
        return repr(self.arr)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    l = List(arr)
    print(f'arr: {arr}, l: {l}')
    arr.append(0)
    print(f'arr: {arr}, l: {l}')
