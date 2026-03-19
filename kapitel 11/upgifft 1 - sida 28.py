def check_type(value):
    try:
        int(value)
        return "Integer"
    except ValueError:
        try:
            float(value)
            return "Float"
        except ValueError:
            return "String"

user_input = input("Enter something: ")
print(check_type(user_input))