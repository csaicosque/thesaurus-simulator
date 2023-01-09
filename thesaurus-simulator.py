
dictionary = {'Carro': 'Car', 'Maçã': 'Apple', 'Rato': 'Mouse'}

def register():
    global dictionary

    print('1 - Register new word;')
    english = input('Enter the word in english: ')
    portuguese = input('Enter the word in portuguese: ')
    dictionary[portuguese] = english


def remove():
    global dictionary

    print('2 - Remove word;')
    clear = input('Type the english word you want to remove: ') #digita o valor, mas em dicionários só pode ser retirado pela chave

    found = False
    for k, v in dictionary.items(): #procura pelas chaves
        if v.upper() == clear.upper(): #quando encontrar a chave que o usuario quer remover
            dictionary.pop(k) #deleta do dicionário :)
            print('Removal successful')
            found = True
            break

    if not found: #se não encontrar da um break só pq eu não sabia o que fazer, mas acho bom dizer "queridx essa chave não tem aqui"
        print('This word doesn\'t exist in this dictionary, please try again')


def show():
    global dictionary

    print('3 - Show dictionary;')
    print('Choose an option:\n[A] See the whole dictionary\n[B] See only the portuquese words\n[C] See only the english words')
    show = input('Enter the chosen letter: ').upper()
    if show == 'A':
        print(f'This is your whole dictionary: {dictionary}')
    elif show == 'B':
        print(f'These are just the Portuguese words in your dictionary: {dictionary.keys()}')
    elif show == 'C':
        print(f'These are just the English words in your dictionary: {dictionary.values()}')
    else:
        print(f'Sorry, I didn\'t undertend your choice, please try again')


def translate(): # Essa parte eu AINDA não sei como fazer usando o objeto dicionário
    global dictionary

    print('4 - Translate;')

    inverted_dictionary = {v.upper(): k for k, v in dictionary.items()}

    phrase_usr = input('Enter the phrase you want to translate: ')
    phrase = phrase_usr.split(' ')
    translated = ''
    for word in phrase:
        user_fmt = format_word(word)
        translated += user_fmt(inverted_dictionary[word.upper()]) + ' '
    print(f'This is your translated phrase: {translated}')


def format_word(word):
    if word.isupper():
        user_fmt = str.upper
    elif word.islower():
        user_fmt = str.lower
    elif word.istitle():
        user_fmt = str.title
    else:
        user_fmt = lambda s: s
    return user_fmt


def quit():
    print('5 - Exit;')


while True:
    print('Choose an option:')
    print('[1] Register\n[2] Remove\n[3] Show\n[4] Translate\n[5] Exit')
    choice = input('Enter the chosen number: ')
    if choice == '1':
        register()
    elif choice == '2':
        remove()
    elif choice == '3':
        show()
    elif choice == '4':
        translate()
    elif choice == '5':
        break
    else:
        print('Invalid option. Please, choose again')
