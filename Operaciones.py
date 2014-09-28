class Operaciones:

    def __init__(self,n1,n2):
        self.num1 = int(n1)
        self.num2 = int(n2)

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        return self.num1 / self.num2
