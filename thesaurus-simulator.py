# Nomes: Cindi Saicosque; Felippe Carrion; Laura Pinzon
dictionary = [['carro', 'car'], ['maça', 'apple'], ['rato', 'mouse'],]

def registration():
    print('1 - Register new word;')
    english = input('Enter the word in english: ')
    portuguese = input('Enter the word in portuguese: ')
    registration = [portuguese, english]
    dictionary.append(registration)

def remove():
    print('2 - Remove word;')
    clear = input('Type the english word you want remover: ')
    found = False
    for pair in dictionary:
        if clear in pair:
            found = True
            break
    if found:
        dictionary.remove(pair)
    else:
        print('The chosen word is not in the dictionary.')

def show():
    print('3 - Show dictionary;')
    print('Dictionary:', dictionary)

def translate():
    print('4 - Translate;')
    phrase_usr = input('Enter the phrase you want to translate: ')
    phrase = phrase_usr.split(' ')
    translated = ''
    for word in phrase:
        for pair in dictionary:
            if word in pair:
                translated += pair[0]
                translated += ' '
                break
    print(translated)

def exit():
    print('5 - Exit;')


while True:
    print('choose an option:')
    print('[1] Registration\n[2] Remove\n[3] Show \n[4] Translate \n[5] Exit')
    choice = input('Enter the chosen number: ')
    if choice == '1':
        registration()
    elif choice == '2':
        remove()
    elif choice == '3':
        show()
    elif choice == '4':
        translate()
    elif choice == '5':
        break
    else:
        print('Invalid option, choose again:')
        continue
