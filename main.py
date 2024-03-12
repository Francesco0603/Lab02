import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary('dictionary.txt')

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txtIn = input()
        t.handleAdd(txtIn.split(" "))
        print("Aggiunta con successo!")
    if int(txtIn) == 2:
        print("Ok, quale parola devo tradurre?")
        txtIn = input()
        print(t.handleTranslate(txtIn))
    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare?")
        pass
    if int(txtIn) == 4:
        break
