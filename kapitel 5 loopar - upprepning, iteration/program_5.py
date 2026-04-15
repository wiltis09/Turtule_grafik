# program_5.py
# Kapitel: automatisk organisering


summa = 0
try:
    for i in range(0, 50):
        summa += i
finally:
    print("Summan är:", summa)