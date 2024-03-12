class Translator:

    def __init__(self):
        self.dizionario = {}

    def printMenu(self):
        print("-----------------------------")
        print(" Traduttore Italiano-Alieno  ")
        print("-----------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit")
        print("-----------------------------")
        print()

    def loadDictionary(self, dict):
        with open(dict,'r') as file:
            for line in file:
                parole = line.split(" ")
                self.dizionario[parole[0]] = [parole[1]]


    def handleAdd(self, entry):
        traduzioniNuove = []
        n = 1
        # salvo tutte le traduzioni inserite in input
        while n <= len(entry):
            traduzioniNuove.append(entry[n])
            n+=1
        # gestisco eventuali duplicazioni di parole
        if self.dizionario[entry[0]].__eq__(traduzioniNuove):
            raise ValueError("TRADUZIONI PRESENTI")
        for traduzione in traduzioniNuove:
            if traduzione not in self.dizionario[entry[0]]:
                self.dizionario[entry[0]]



        self.dizionario[entry[2]] = [entry[1]]

    def handleTranslate(self, query):
        traduzione = []
        for coppia in self.dizionario:
            if coppia[0] == query:
                traduzione.append(coppia[1])
        return traduzione


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass