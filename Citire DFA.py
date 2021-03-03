d = {}
d["values"] = set()
d["states"] = set()
d["transitions"] = []
state_type = {}

counter = 0
lines = 0
error = 0
start = 0
final = 0

f = open("input", "r")
for line in f:
    lines += 1
    if line != 'End':
        line = line[:-1]
    if line[0] != '#' and line != 'End':
        if line == 'Sigma:':
            counter = 1
        elif line == 'States:':
            counter = 2
        elif line == 'Transitions:':
            counter = 3
        elif counter == 1:
            lista = line.split('\t')
            line = lista[1]
            d['values'].add(line)
        elif counter == 2:
            if ',' not in line:
                lista = line.split('\t')
                line = lista[1]
                d['states'].add(line)
                state_type[line] = 0
            else:
                list = line.split(', ')
                lista = list[0].split('\t')
                list[0] = lista[1]
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
            lista = line.split('\t')
            line = lista[1]

            list = line.split(' ')
            list[0] = list[0][:-1]
            list[1] = list[1][:-1]
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
    print(d)
    for item in state_type.items():
        print(item)
