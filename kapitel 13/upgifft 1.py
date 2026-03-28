#Rekursiva nedräkning

def countdown(value):
    new_value = value
    print(new_value)
    for i in range(0,(value)):
        new_value -= 1
        print(new_value)
countdown(500)