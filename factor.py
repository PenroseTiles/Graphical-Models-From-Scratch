import numpy as np

class Factor():
    def __init__(self, vars, card, val, name):
        self.var = vars
        self.card = np.array(card)
        self.val = np.array(val)
        self.name = name

    def setVar(self, var):
        self.var = var
        return

    def getVar(self):
        return self.var

    def setCard(self, card):
        self.card = card
        return

    def getCard(self):
        return self.card

    def setVal(self, val):
        self.val=val
        return

    def getVal(self):
        return self.val

    def __str__(self):
        return ""