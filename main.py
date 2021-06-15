from string import printable
from random import randint

printable = list(printable)

MEMORY_SIZE = 500
POINTER = 0
STEP = 0
stop = 0
labels = {}

raw_file = open("input.txt", encoding="utf-8").read()
nicer_file = raw_file.split("\n")
print("1. done")
memory = []

for x in nicer_file:
    args = nicer_file[STEP].split(" ")
    if args[0] == ':':
        labels[args[1]] = STEP
    STEP = STEP + 1
STEP = 0
print("2. done")

for x in range(MEMORY_SIZE):
    memory.append(0)
print("3. done")

while not stop:
    if not STEP == len(nicer_file):
        args = nicer_file[STEP].split(" ")
    else:
        stop = 1
        continue
    if args[0] == "point":
        POINTER = int(args[1])
    elif args[0] == "set":
        memory[POINTER] = int(args[1])
    elif args[0] == "stop":
        stop = 1
    elif args[0] == "pass":
        pass
    elif args[0] == "print":
        try:
            print(printable[memory[POINTER]], end="")
        except IndexError:
            pass
    elif args[0].startswith(":"):
        pass
    elif args[0] == 'jump':
        if args[1].isnumeric():
            STEP = int(args[1])
        elif args[1] in labels.keys():
            STEP = labels[args[1]]
        else:
            stop = 1
            print("this ain't a real address lmao %s" % args[1])
    elif args[0] == "inc":
        memory[POINTER] = memory[POINTER] + 1
    elif args[0] == "dec":
        memory[POINTER] = memory[POINTER] - 1
    elif args[0] == "rand":
        if randint(0, 1):
            memory[POINTER] = memory[POINTER] + 1
        else:
            memory[POINTER] = memory[POINTER] - 1
    elif args[0] == "if":
        if not memory[int(args[1])]:
            STEP = STEP + 1
    elif args[0] == "ifequal":
        if memory[int(args[1])] == int(args[1]):
            STEP = STEP + 1
    elif args[0] == "notifequal":
        if not memory[int(args[1])] == int(args[2]):
            STEP = STEP + 1
    elif args[0] == "notif":
        if memory[int(args[1])]:
            STEP = STEP + 1
    elif args[0] == "input":
        memory[POINTER] = int(input())
    elif args[0].strip() == '':
        STEP = STEP + 1
        continue
    else:
        stop = 1
        print("what is this instruction lol %s" % nicer_file[STEP])
    STEP = STEP + 1
print("programme ended i guess")
