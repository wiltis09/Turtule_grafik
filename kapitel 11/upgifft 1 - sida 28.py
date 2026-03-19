


def isfloat(string):
    try:
        if type(string) is str:
            print("str")
        elif type(string) is float:
            print("float")
        elif type(string) is int:
            print("int")
    except:
        print("fel")
isfloat(input("str: "))
