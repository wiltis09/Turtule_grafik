
# Gör en egen funktion som rekursivt omvandlar ett decimaltal till en sträng med binär
#representation. Utnyttja att om ett tal är jämnt delbart med två så slutar det på en nolla i
# binär representation och annars slutar det på etta.


# Funktion som rekursivt omvandlar ett decimaltal till en binär sträng
def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2 ) + str(n % 2)

print(to_binary(13))

