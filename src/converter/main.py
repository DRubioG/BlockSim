import sys

arg = 'example.bsim'

# Read BSIM file

file = open(arg, 'r')

nets = []
scopes = []
blocks = []

for i in file:
    aux = i.replace("\n", '')
    aux = aux.replace(" ", '')
    aux = aux.replace("\t", '')
    if aux != '' and aux[0] != '#':
        aux = aux.split("->")
        if aux[1][0] == '&':
            scopes.append(aux)
        if aux[1][0] == '*':
            nets.append(aux)


blk_aux = []
for i in nets:
    blk_aux.append(i[0])
    if len(i) > 2:
        if i[2].find(',') != -1:
            i[2] = i[2].split(',')
        blk_aux.append(i[2])

blk = []
for j in blk_aux:
    blk = blk.split('[')


print(blk_aux)


# Write executable 
arg = arg[:-5] + '.py'

file_out = open(arg, 'w')



wr = ''

## from
for i in blocks:
    wr += "from Blocks.Python_blocks." + i + " import *\n"
wr+= "\n"

## init_func()
wr += "\ndef init_func():\n\tglobal "
cont = 0
for j in nets:
    wr += " " + j + "_ant"
    if cont < len(j)-1:
        wr += ','
    cont += 1

for k in nets:
    wr += "\n\t"+k+"_ant = 0"

cont = 0
for j in scopes:
    wr += " " + j + "_ant"
    if cont < len(j)-1:
        wr += ','
    cont += 1

for k in nets:
    wr += "\n\t"+k+" = []"

## update_signal()
wr += "\ndef update_signal():\n\tglobal "
cont = 0
for j in nets:
    wr += " " + j 
    if cont < len(j)-1:
        wr += ','
    cont += 1

for k in nets:
    wr += "\n\t"+k+" = " +k+ "_ant"



print(scopes)
print(nets)