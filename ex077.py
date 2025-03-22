palavras = ("Mochila", "Lapis", "Caderno")
for p in palavras:
    print(f"\nNa palavra {p} temos")
    for letra in p:
        if letra.lower() in "aeiou":
           print(letra, end=' ') 