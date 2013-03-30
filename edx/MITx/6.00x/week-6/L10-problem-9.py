class Queue(object):

    def __init__(self):
        self.vals = []

    def insert(self, e):
        self.vals.append(e)

    def remove(self):
        try:
            return self.vals.pop(0)
        except:
            raise ValueError()

    def __str__(self):
        return '[' + ','.join([str(e) for e in self.vals]) + ']'

    def __len__(self):
        return len(self.vals)

if __name__ == '__main__':
    queue = Queue()
    queue.insert(5)
    queue.insert(6)
    assert queue.remove() == 5
    queue.insert(7)
    assert queue.remove() == 6
    assert queue.remove() == 7
    try:
        queue.remove()
        assert False
    except:
        assert True