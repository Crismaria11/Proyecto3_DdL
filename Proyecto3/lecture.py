def word_reader(file, current):
    temp = ""
    while current < len(file):
        if(file[current] == " " or file[current] == "\n") and (len(temp) > 0):
            break
        elif file[current] == " " or file[current] == "\n":
            current += 1
        else:
            temp += file[current]
            current += 1

    return temp, current


def readerino(file):
    a = 1
    current = 0
    chars = []
    tokens = []
    keywords = []
    produs = []
    temp = ""
    while True:
        temp, current = word_reader(file, current)
        if temp == "COMPILER":
            title, current = compiler(file, current)
        if temp == "CHARACTERS":
            chars, current = charas(file, current)
        if temp == "KEYWORDS":
            keywords, current = keys(file, current)
        if temp == "TOKENS":
            tokens, current = toks(file, current)
        if temp == "PRODUCTIONS":
            produs, current = prods(file, current)
        if temp == "END":
            endof = endofline(file, current, title)
            if endof:
                break
            else:
                print("no hay final de archivo")
                break

    return title, chars, tokens, keywords, produs


def compiler(file, current):
    current += 1
    title, current = word_reader(file, current)
    return title, current


def charas(file, current):

    current += 1
    charass = {}
    line = ""

    while True:
        temp, current = word_reader(file, current)
        if temp == "KEYWORDS":
            current -= 8
            break
        line += temp
        print("myLine -> ", line)
        if line[-1] == "." and line[-2] != "." and "END":
            if "=" in line:
                alles = line.split("=")
                ids = alles[0]
                vals = alles[1]
                charass[ids] = vals
                line = ""
            else:
                print("'=' no encontrado", line[-1], line[-2]) 
    return charass, current

def keys(file, current):
    current += 1
    temp = ""
    keyes = {}
    ids = ""
    vals = ""
    line = ""
    while True:
        temp, current = word_reader(file, current)
        if temp == "TOKENS":
            current -= 6
            break
        line += temp
        if line[-1] == ".":
            if "=" in line:
                alles = line.split("=")
                ids = alles[0]
                vals = alles[1]
                keyes[ids] = vals
                line = ""
            else:
                print("'=' no encontrado")

    return keyes, current


def toks(file, current):
    current += 1
    temp = ""
    tokis = {}
    ids = ""
    vals = ""
    line = ""
    while True:
        temp, current = word_reader(file, current)
        if temp == "PRODUCTIONS":
            current -= 11
            break
        if temp == "END":
            current -= 3
            break
        line += temp
        if line[-1] == ".":
            if "=" in line:
                alles = line.split("=")
                print("este es alles ver", alles)
                ids = alles[0]
                vals = alles[1]
                # print(alles[1], 'alles 1', alles[0], 'alles 0')
                tokis[ids] = vals
                line = ""
            else:
                print("'=' no encontrado")

    return tokis, current

def prods(file, current):
    current += 1
    temp = ""
    products = {}
    ids = ""
    vals = ""
    line = ""
    flaggerino = False
    while current < len(file):
        temp += file[current]
        if temp[-1] == "." and temp[-2] != "(" and (file[current + 1] == " " or file[current + 1] == "\n"):
            add = '(.return resultado.)'
            alles = temp.split("=", 1)
            ids = alles[0]
            vals = alles[1]
            # print(temp)
            # print(temp.find('print'))
            # if temp.find('EstadoInicial') == 1 or temp.find('Instruccion') == 2:
            if temp.find('EstadoInicial') > 0 or temp.find('Instruccion') > 0:# or temp.find('print') > 0:
                print('salio')
            else:
                vals = vals[:(len(vals) - 1)] + add + vals[(len(vals) - 1):]
            products[ids] = vals
            # print(vals, 'termino el ciclo')
            # print('termino el ciclo')
            # print(type(vals))
            # print(len(vals))
            # print(vals[len(vals) - 1])
            # print(add, vals[len(vals) - 1])
            # print('antes:', vals)
            # print('fin del antes')
            # print('cambio en el vals')
            # vals = vals[:(len(vals) - 1)] + add + vals[(len(vals) - 1):]
            # print(vals)
            # print('Fin del cambio vals')
            # print('termino prueba\n\n\n')
            temp = ""
        if "\nEND" in temp:
            current -= 3
            temp = ""
            break
        current += 1
    return products, current

def endofline(file,current, title):
    current += 1
    enderino, current = word_reader(file,current)
    if enderino == title:
        return True
    return False