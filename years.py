
def years(arg):
    if arg.isdigit(): 
        global age
        age = arg
    else:
        years(input ("Only numbers !! whats ypur age ?\n"))

def name(arg):
    if arg.isalpha():
        global name
        name = arg
    else:
        name(input("Only letters !! what ur name ?\n"))

def main():
    years(input("What is your age ?\n"))
    name(input("What is you name ?\n"))
    print(f"Hi {name} how are your {age} years old are going ?")

main()
