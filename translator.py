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
        print("4. Stampa tutto il Dizionariog")
        print("5. Exit")
        print("-----------------------------")
        print()

    def __str__(self):
        stampa = ""
        for word in self.dizionario:
            transl = ""
            for tr in self.dizionario[word]:
                transl += tr+","
            stampa += word+" significa: "+transl[:len(transl)-1]+"\n"
        return stampa
    def loadDictionary(self, dict):
        with open(dict,'r') as file:
            for line in file:
                parole = line.split(" ")
                self.dizionario[parole[0]] = [parole[1]]

    def handleAdd(self, entry):
        traduzioniNuove = []
        n = 1
        # salvo tutte le traduzioni inserite in input
        while n < len(entry):
            traduzioniNuove.append(entry[n])
            n+=1
        # gestisco eventuali duplicazioni di parole
        if self.dizionario.__contains__(entry[0]):
            if self.dizionario[entry[0]] == (traduzioniNuove):
                raise ValueError("TRADUZIONI PRESENTI")
            for traduzione in self.dizionario[entry[0]]:
                if traduzione not in traduzioniNuove:
                    traduzioniNuove.append(traduzione)
            self.dizionario[entry[0]] = traduzioniNuove
        # se invece non c'è
        else:
            self.dizionario[entry[0]]= traduzioniNuove

    def handleTranslate(self, query):
        for coppia in self.dizionario:
            if coppia == query:
                trad = ""
                for str in self.dizionario[coppia]:
                    trad += str+", "
                return trad[:len(trad)-2]

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass