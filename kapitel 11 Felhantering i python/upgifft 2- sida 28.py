
# För att kontrollera om en sträng består enbart av decimala siffror och alltså kan omvandlas 
# till ett heltal, finns strängmetoden. isdecimal(), men den tillåter inget tecken i början.
# Gör en funktion isint(str), motsvarande den i förra uppgiften och som klarar av att 
# kontrollera i fall en sträng går att omvandla till ett heltal.

def isint(str):
    try:
        int(str)
        print(ValueError, "int")
        return True
    except ValueError:
        try:
            float(str)
            print(ValueError, "float")
            return False
        except ValueError:
            print(ValueError, "str")
            return False

user_input = input("Enter something: ")
print(isint(user_input))