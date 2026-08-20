RED = "RED"
BLACK = "BLACK"


class Foglia:
    def __init__(self):
        self.Valore = None
        self.altezza = 0
        self.FiglioSinistro = self
        self.FiglioDestro = self
        self.padre = self
        self.colore = BLACK


class Nodo_ABR:
    def __init__(self, valore):
        self.Valore = valore
        self.FiglioSinistro = None
        self.FiglioDestro = None
        self.padre = None


class Nodo_AVL:
    def __init__(self, valore):
        self.Valore = valore
        self.FiglioSinistro = None
        self.FiglioDestro = None
        self.padre = None
        self.altezza = 1


class Nodo_RB:
    def __init__(self, valore):
        self.Valore = valore
        self.FiglioSinistro = None
        self.FiglioDestro = None
        self.padre = None
        self.colore = None


class AlberoABR:
    def __init__(self):
        self.Radice = None

    def ABR_Tree_Insert(self, z):
        y = None
        x = self.Radice

        while x is not None:
            y = x
            if z.Valore < x.Valore:
                x = x.FiglioSinistro
            else:
                x = x.FiglioDestro

        z.padre = y

        if y is None:
            self.Radice = z
        elif z.Valore < y.Valore:
            y.FiglioSinistro = z
        else:
            y.FiglioDestro = z



class AlberoAVL:
    def __init__(self):
        self.NIL = Foglia()
        self.Radice = self.NIL

    def AVL_Tree_Insert(self, z):
        y = self.NIL
        x = self.Radice

        while x != self.NIL:
            y = x
            if z.Valore < x.Valore:
                x = x.FiglioSinistro
            else:
                x = x.FiglioDestro

        z.padre = y
        z.FiglioSinistro = self.NIL
        z.FiglioDestro = self.NIL
        z.altezza = 1

        if y is self.NIL:
            self.Radice = z
        elif z.Valore < y.Valore:
            y.FiglioSinistro = z
        else:
            y.FiglioDestro = z

        self.AVL_Insert_Fixup(y)

    def AVL_Insert_Fixup(self, z):
        while z != self.NIL:
            self.Update_Height(z)

            bf = z.FiglioSinistro.altezza - z.FiglioDestro.altezza

            if bf > 1:
                if (z.FiglioSinistro.FiglioSinistro.altezza <
                        z.FiglioSinistro.FiglioDestro.altezza):
                    self.AVL_Left_Rotate(z.FiglioSinistro)

                self.AVL_Right_Rotate(z)

            elif bf < -1:
                if (z.FiglioDestro.FiglioDestro.altezza <
                        z.FiglioDestro.FiglioSinistro.altezza):
                    self.AVL_Right_Rotate(z.FiglioDestro)

                self.AVL_Left_Rotate(z)

            z = z.padre

    def Update_Height(self, x):
        x.altezza = 1 + max(
            x.FiglioSinistro.altezza,
            x.FiglioDestro.altezza
        )

    def AVL_Left_Rotate(self, x):
        y = x.FiglioDestro
        x.FiglioDestro = y.FiglioSinistro
        self.Update_Height(x)

        if y.FiglioSinistro != self.NIL:
            y.FiglioSinistro.padre = x

        y.padre = x.padre

        if x.padre == self.NIL:
            self.Radice = y
        elif x == x.padre.FiglioSinistro:
            x.padre.FiglioSinistro = y
        else:
            x.padre.FiglioDestro = y

        y.FiglioSinistro = x
        self.Update_Height(y)
        x.padre = y

    def AVL_Right_Rotate(self, x):
        y = x.FiglioSinistro
        x.FiglioSinistro = y.FiglioDestro
        self.Update_Height(x)

        if y.FiglioDestro != self.NIL:
            y.FiglioDestro.padre = x

        y.padre = x.padre

        if x.padre == self.NIL:
            self.Radice = y
        elif x == x.padre.FiglioDestro:
            x.padre.FiglioDestro = y
        else:
            x.padre.FiglioSinistro = y

        y.FiglioDestro = x
        self.Update_Height(y)
        x.padre = y


class AlberoRB:
    def __init__(self):
        self.NIL = Foglia()
        self.Radice = self.NIL

    def RB_Tree_Insert(self, z):
        y = self.NIL
        x = self.Radice

        while x != self.NIL:
            y = x
            if z.Valore < x.Valore:
                x = x.FiglioSinistro
            else:
                x = x.FiglioDestro

        z.padre = y

        if y == self.NIL:
            self.Radice = z
        elif z.Valore < y.Valore:
            y.FiglioSinistro = z
        else:
            y.FiglioDestro = z

        z.FiglioSinistro = self.NIL
        z.FiglioDestro = self.NIL
        z.colore = RED

        self.RB_Insert_Fixup(z)

    def RB_Insert_Fixup(self, z):
        while z.padre.colore == RED:
            if z.padre == z.padre.padre.FiglioSinistro:
                y = z.padre.padre.FiglioDestro

                if y.colore == RED:
                    z.padre.colore = BLACK
                    y.colore = BLACK
                    z.padre.padre.colore = RED
                    z = z.padre.padre

                else:
                    if z == z.padre.FiglioDestro:
                        z = z.padre
                        self.RB_Left_Rotate(z)

                    z.padre.colore = BLACK
                    z.padre.padre.colore = RED
                    self.RB_Right_Rotate(z.padre.padre)

            else:
                y = z.padre.padre.FiglioSinistro

                if y.colore == RED:
                    z.padre.colore = BLACK
                    y.colore = BLACK
                    z.padre.padre.colore = RED
                    z = z.padre.padre

                else:
                    if z == z.padre.FiglioSinistro:
                        z = z.padre
                        self.RB_Right_Rotate(z)

                    z.padre.colore = BLACK
                    z.padre.padre.colore = RED
                    self.RB_Left_Rotate(z.padre.padre)

        self.Radice.colore = BLACK

    def RB_Left_Rotate(self, x):
        y = x.FiglioDestro
        x.FiglioDestro = y.FiglioSinistro

        if y.FiglioSinistro != self.NIL:
            y.FiglioSinistro.padre = x

        y.padre = x.padre

        if x.padre == self.NIL:
            self.Radice = y
        elif x == x.padre.FiglioSinistro:
            x.padre.FiglioSinistro = y
        else:
            x.padre.FiglioDestro = y

        y.FiglioSinistro = x
        x.padre = y

    def RB_Right_Rotate(self, x):
        y = x.FiglioSinistro
        x.FiglioSinistro = y.FiglioDestro

        if y.FiglioDestro != self.NIL:
            y.FiglioDestro.padre = x

        y.padre = x.padre

        if x.padre == self.NIL:
            self.Radice = y
        elif x == x.padre.FiglioDestro:
            x.padre.FiglioDestro = y
        else:
            x.padre.FiglioSinistro = y

        y.FiglioDestro = x
        x.padre = y