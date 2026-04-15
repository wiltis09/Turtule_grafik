# Vi har tidigare gjort funktioner för att bäräkna de så kallade Fibonaccitalen, som består av
# talföljden 1, 1, 2, 3, 5, 8, 13, 21, 34, 55... och så vidare. Men starta med två tal (lämpligen
# 1 och 1), och sedan får varje nytt tal i följden bestå av summan av de två föregående talen.
# Kallar man det n:te talet i talföljden för fib(n), så kna mna uttrycka det så att

#                           1 om n <=2
#           fib(n) =
#                           fib(n-2) + fib(n-1) i övriga fall

# Gör en rekursiv funktion som bärknar och returnerar fibonaccital nr n. Kalla funktionen
# för fib(). Gör ett program som med hjälp av funktionen skriver ut en tabell med
# fibonaccital upp till säg det fyrtionde.

# Det är enkelt att programmera funktionen rekursivt men det blir mycket långsam redan
# fö n-värden som bara är några tiotal. Det är ju dubbelt rekursiv och för att t.ex bäräkna
# fib(30) måste först fib(29) och fib(28) beräknas. Men för att beräkna fib(29) beräknas
# fib(28) och fib(27) och inga bäräkningar sparas, varför de måste utföras om och om igen.

# Det blir allså ett exempel på att det inte är så smart med rekursion i just detta fall, även 
# om det är enkelt att programmera den.

# Att som vi tidigare gjort exempelvis att undan för undan beräkna talen och spara undan i 
# en lista så att de inte behöver beräknas på nytt om och om igen, brukar kallas dynamisk
# programmering.



def fib(value):
    if value > 2:
        return fib(value - 1) + fib(value - 2)
    else:
        return 1
    
x = fib(50)
print(x)