def get_initials(fullname):
    names = fullname.split()
    inits = ""
    for name in names:
        inits = inits + name[0].upper()
    return inits

def main():
    fullname = input("What is your full name?\n")
    print(get_initials(fullname))

if __name__ == '__main__':
    main()
