def check_type(value):
    try:
        int(value)
        print(ValueError, "int")
        return "Integer"
    except ValueError:
        try:
            float(value)
            print(ValueError, "float")
            return "Float"
        except ValueError:
            print(ValueError, "str")
            return "String"

user_input = input("Enter something: ")
print(check_type(user_input))