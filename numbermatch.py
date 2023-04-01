import random
class Casella:
    def __init__(self):
        self.value = random.randint(1, 9)
    def getvalue(self):
        return self.value


class Tauler:
    def __init__(self, mida):
        self.mida = mida
        self.tauler = []
        self.afegir_fila()
    def getmida(self):
        return self.mida
    def afegir_fila(self):
        l = []
        for _ in range(self.getmida()):
            a = Casella()
            l.append(a)
        self.tauler.append(l)
    def select(self, i, j):
        return self.tauler[i][j].getvalue()
    def delete(self, i ,j):
        self.tauler[i][j] = None
    def check_end(self):
        return [] == self.tauler
    def delete_empty_row(self):
        emptyrow = [None for _ in range(self.mida)]
        t = []
        for e in self.tauler:
            if e != emptyrow:
                t.append(e)
        self.tauler = t

    def __str__(self):
        self.delete_empty_row()
        s = ""
        for e in self.tauler:
            for i in e:
                if (i != None):
                    l = "| "+str(i.getvalue())+" |"
                else:
                    l = "|   |"
                s += l
            s += "\n"
        return s

class Joc:
    def __init__(self, mida):
        self._score = 0
        self._fi = False
        self.tauler = Tauler(mida)

        self.juga()
        
    def juga(self):
        while (not self._fi):
            self.print_tauler()
            self.torn()
            self._fi = self.tauler.check_end()
        print("Has acabat!")
        print("Has assolit una puntuació de "+ str(self._score))
    def torn(self):
        x = input("Add new lines?")
        if x == "y":
            self.newlines()
        else:
            x = "y"
            while x == "y":
                x = input("Want to select two numbers?")
                if x == "y":
                    i,j = input("First coordinates: ").split(" ")
                    l,m = input("Second coordinates: ").split(" ")
                    i = int(i)
                    j = int(j)
                    l = int(l)
                    m = int(m)
                    if (self.testsum(self.tauler.select(i,j), self.tauler.select(l,m))):
                        self.tauler.delete(i,j)
                        self.tauler.delete(l,m)
                        self._score += 1
                        self._fi = self.tauler.check_end()
                        print("Very good.")
                        self.print_tauler()
                        self.show_score()
                    else:
                        print("Wrong, stupid bitch.")
                        self.print_tauler()

    def newlines(self):
        self.tauler.afegir_fila()
        self.print_tauler()
    def testsum(self, a, b):
        return (a+b) == 10 or a==b
    def show_score(self):
        print("Your score now is: " + str(self._score))
    def print_tauler(self):
        print(self.tauler)


l = Joc(5)
