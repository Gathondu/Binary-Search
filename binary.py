class BinarySearch(list):

    def __init__(self, length, step):
        super(BinarySearch, self).__init__(list(range(step, (step*length)+1, step)))
        self.length = length

    def search(self, value):
        # initialize variables to use with binary search algo
        first, last = 0, self.length - 1
        countIter = 0  # counts the number of iterations
        ind = -1  # stores the index of the number if found
        midPoint = int(last/2)

        # the binary search algo
        while first < midPoint:
            if (first == midPoint) and (self[first] > value):
                break
            elif self[first] == value:
                ind = self.index(value)
                break
            elif self[last] == value:
                ind = self.index(value)
                break
            elif self[midPoint] == value:
                ind = self.index(value)
                break
            else:
                if self[midPoint] > value:
                    last = midPoint - 1
                    first += 1
                    midPoint = (first + last) // 2
                else:
                    first = midPoint + 1
                    last -= 1
                    midPoint = ((first + last) // 2) + 1
            countIter += 1

        # return a dictionary of count and index
        return {'count': countIter, 'index': ind}


if __name__ == '__main__':
    b = BinarySearch(20, 2)
    d = b.search(33)
