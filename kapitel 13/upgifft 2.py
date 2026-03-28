



def countdown(value):
    new_value = int(value)
    for i in range(0,value):
        if (new_value / 2).is_integer():
            print("1")
        else:
            print("0")
        new_value -= 1

countdown(25)

