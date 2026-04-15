# Gör en funktion som utför multiplikation av heltal rekursivt som upprepade additioner
# kalla funktionen mul() och använde följande rekrusiva definition:

#                           a om b = 1
#       mul(a,b) =´
#                           a + mul(a,b-1) i övriga fall

def mul(a):
    print(a)
    mul(a + 4)
mul(5)