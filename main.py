import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary('dictionary.txt')

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        paroleInserite = input()
        t.handleAdd(paroleInserite.split(" "))
        print("Aggiunta con successo!")
    if int(txtIn) == 2:
        print("Ok, quale parola devo tradurre?")
        paroleInserite = input()
        print(t.handleTranslate(paroleInserite))
    if int(txtIn) == 3:
        print("Ok, quale parola devo tradurre?")
        paroleInserite = input()
        print(t.handleWildCard(paroleInserite))
    if int(txtIn) == 4:
        print(t)
    if int(txtIn) == 5:
        break
