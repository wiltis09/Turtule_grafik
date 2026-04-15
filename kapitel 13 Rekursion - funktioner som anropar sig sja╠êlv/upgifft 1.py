# Gör en funktion countdown(), som rekursiv räknar ner från ett visst heltalsargument
# ner till noll.

def countdown(value):
    print(value)
    if not value == 0:
        countdown(value - 1)
countdown(5)


