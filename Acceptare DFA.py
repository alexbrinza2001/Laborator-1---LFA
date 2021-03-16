d = {}
d["values"] = set()
d["states"] = set()
d["transitions"] = []
state_type = {}

counter = lines = error = start = final = ok = 0

def dfs(word, pos, current_state):
    global ok
    global state_type
    global d
    if ok == 1:
        return
    if pos == len(word):
        if state_type[current_state] == -1 or state_type[current_state] == 2:
            ok = 1
            return
        else:
            return

    letter = word[pos]
    for transition in d['transitions']:
        if transition[0] == current_state and transition[2] == letter:
            dfs(word, pos + 1, transition[1])

f = open("input", "r")
for line in f:
    lines += 1
    if line != 'End':
        line = line[:-1]
    if line != "" and line[0] != '#' and line != 'End':
        if line == 'Sigma:':
            counter = 1
        elif line == 'States:':
            counter = 2
        elif line == 'Transitions:':
            counter = 3
        elif counter == 1:
            lista = line.strip()
            d['values'].add(lista[0])
        elif counter == 2:
            if ',' not in line:
                lista = line.strip()
                d['states'].add(lista)
                state_type[lista] = 0
            else:
                list = line.split(', ')
                list[0] = list[0].split()
                list[0] = list[0][0]
                if len(list) == 3:
                    d['states'].add(list[0])
                    state_type[list[0]] = 2
                    start += 1
                    final += 1
                elif list[1] == 'F':
                    d['states'].add(list[0])
                    state_type[list[0]] = -1
                    final += 1
                else:
                    d['states'].add(list[0])
                    state_type[list[0]] = 1
                    start += 1
        elif counter == 3:
            list = line.split(', ')
            list[0] = list[0].split()
            list[0] = list[0][0]

            state1 = list[0]
            state2 = list[2]
            word = list[1]

            if state1 not in d['states']:
                print("Eroare la linia" , lines , "!" , "Starea" , state1 , "nu exista!")
                error = 1
            if state2 not in d['states']:
                print("Eroare la linia" , lines, "!" , "Starea" , state2 , "nu exista!")
                error = 1
            if word not in d['values']:
                print("Eroare la linia" , lines , "!" , "Cuvantul " , word , " nu exista!")
                error = 1

            if error == 0:
                d['transitions'].append( (state1 , state2 , word) )

if start == 0:
    print("Limbajul nu are nicio stare initiala!")
    error = 1

if start > 1:
    print("Limbajul are mai multe stari initiale!")
    error = 1

if final == 0:
    print("Limbajul nu are stari finale!")
    error = 1

if error == 0:
    for item in state_type.items():
        if item[1] == 1 or item[1] == 2:
            initial = item[0]

    f = open("input_words", "r")
    counter = 1

    for line in f:
        if line[-1] == '\n':
            word = line[:-1]
        else:
            word = line
        ok = 0
        dfs(word, 0, initial)
        if ok == 1:
            print("accept")
        else:
            print("reject")