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
                transl += tr + ","
            stampa += word + " significa: " + transl[:len(transl) - 1] + "\n"
        return stampa

    def loadDictionary(self, dict):
        if len(self.dizionario) == 0:
            with (open(dict, 'r') as file):
                for line in file:
                    parole = line.split(" ")
                    chiave = parole[0]
                    parole.remove(chiave)
                    self.dizionario[chiave] = [trad for trad in parole]
        else:
            with open(dict, 'w') as file:
                for chiave in self.dizionario:
                    transl = ""
                    for tr in self.dizionario[chiave]:
                        transl += tr + " "
                    stampa = chiave + " " + transl[:len(transl) - 1]
                    file.write(stampa)

    def handleAdd(self, entry):
        traduzioniNuove = []
        n = 1
        # salvo tutte le traduzioni inserite in input
        while n < len(entry):
            traduzioniNuove.append(entry[n])
            n += 1
        # gestisco eventuali duplicazioni di parole
        if self.dizionario.__contains__(entry[0]):
            if self.dizionario[entry[0]] == (traduzioniNuove):
                raise ValueError("TRADUZIONI PRESENTI")
            for traduzione in self.dizionario[entry[0]]:
                if traduzione not in traduzioniNuove:
                    traduzioniNuove.append(traduzione)
                    n += 1
        traduzioniNuove[n - 2] = traduzioniNuove[n - 2] + "\n"
        # se invece non c'è
        self.dizionario[entry[0]] = traduzioniNuove

    def handleTranslate(self, query):
        for chiave in self.dizionario:
            if chiave == query:
                trad = ""
                for str in self.dizionario[chiave]:
                    trad += str + ", "
                return trad[:len(trad) - 2]
            for transl in self.dizionario[chiave]:
                if transl.strip("\n") == query:
                    return chiave

    def handleWildCard(self, query):
        if "?" in query:
            # Lista delle lettere minuscole accentate e non accentate in Unicode
            lettere_unicode = [chr(i) for i in range(0x0061, 0x007B)]  # Lettere minuscole non accentate
            lettere_unicode += [chr(i) for i in range(0x00E0, 0x00FF + 1)]  # Lettere minuscole accentate
            # Iterazione attraverso tutte le lettere minuscole, incluse quelle accentate e non accentate
            for lettera in lettere_unicode:
                fixedQuery = query.replace('?',lettera)
                if self.handleTranslate(fixedQuery) is not None:
                    return self.handleTranslate(fixedQuery)
        return self.handleTranslate(query)
