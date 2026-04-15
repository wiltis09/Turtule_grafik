# Gör en funktion is float (str), vilken tar en sträng som parameter och returnerar 
# True om den kan omvandlas till ett flyttal och False annars.

def isfloat(str):
    try:
        int(str)
        print(ValueError, "int")
        return False
    except ValueError:
        try:
            float(str)
            print(ValueError, "float")
            return True
        except ValueError:
            print(ValueError, "str")
            return False

user_input = input("Enter something: ")
print(isfloat(user_input))