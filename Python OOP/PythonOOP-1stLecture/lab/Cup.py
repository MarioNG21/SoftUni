class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, new_qnt):
        if self.quantity + new_qnt < self.size:
            self.quantity += new_qnt

    def status(self):
        free_space = self.size - self.quantity
        return free_space


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
