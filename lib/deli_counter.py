def line(katz_deli = 0):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line = []
        for i in range(len(katz_deli)):
            line.append(str(i+1) + ". " + katz_deli[i])
        print("The line is currently: " + " ".join(line))

def take_a_number(current_line, name):
    current_line.append(name)
    print(f"Welcome, {name}. You are number {len(current_line)} in line.")
    pass

def now_serving(line):
    if len(line) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {line[0]}.")
        line.pop(0)
    pass

