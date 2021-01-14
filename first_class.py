class Calculator:
    def __init__(self, ):
        self.pusta_lista = []

    def add(self, num1, num2):
        self.pusta_lista += [f'Added {num1} to {num2} got result {num1 + num2}']
        return self.pusta_lista

    def multiply(self,num1,num2):
        self.pusta_lista += [f'Multiplied {num1} to {num2} got result {num1 * num2}']
        return self.pusta_lista
    def print_operations(self):
        for x in self.pusta_lista:
            print(f"{x}")



small = Calculator()
small.add(2,3)
small.add(3,4)
small.multiply(12,2)
small.multiply(32,1)
small.multiply(3,8)
small.print_operations()
big = Calculator()
big.multiply(1,32)
big.multiply(3,22)
big.multiply(14,32)


