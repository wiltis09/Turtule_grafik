# En så kallad snöflingekurva eller Koch-kurva (uppkallad efter den svenska matematikern
# Helge von Koch) kan bekrivas genom att man först utgår från en liksidig triangel. Sedan
# knycklar man till eller "bygger på" varje sida med en "utvikning". Detta upprepas sedan för
# varje linjesegment tills man uppnått önskad nivå av "tillknykling". Nedanstående figur visar
# principen:

# Det matematiskt intressanta med denna konstruktion är att om man låter
# "tillknycklingsgrade" gå mot oändligheten så närmar sig kurvan funktion som
# visserligen är kontinuerlig men som överallt saknar derivata. Dess längd är oändlig men 
# samtidigt innesluter den bara en begränsad area. Kochs kurva var av de så
# kallad fraktaler som beskrivits i matematiken.

# Om man försått principen för rekursiva funktioner är det inte så svårt att rita en sådan
# kurva medd viss "tillknycklingsgrad" i sköldpaddsgrafik.


def fib(value):
    if value > 2:
        return fib(value - 1) + fib(value - 2)
    else:
        return 1
    
x = fib(30)
print(x)