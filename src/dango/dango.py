class Dango:
    """
    高速な添字アクセスが可能な Deque
    """

    stack1: list
    stack2: list

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def __getitem__(self, idx):
        if idx < len(self.stack1):
            return self.stack1[len(self.stack1) - 1 - idx]
        else:
            return self.stack2[idx - len(self.stack1)]

    def appendleft(self, x):
        self.stack1.append(x)

    def append(self, x):
        self.stack2.append(x)

    def pop(self):
        if self.stack2 == []:
            mid = (len(self.stack1) + 1) // 2
            self.stack1, self.stack2 = (
                self.stack1[mid:],
                self.stack1[:mid][::-1],
            )

        return self.stack2.pop()

    def popleft(self):
        if self.stack1 == []:
            mid = (len(self.stack2) + 1) // 2

            self.stack1, self.stack2 = (
                self.stack2[:mid][::-1],
                self.stack2[mid:],
            )

        return self.stack1.pop()
