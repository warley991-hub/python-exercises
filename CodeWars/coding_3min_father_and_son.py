'''
This is the simple version of Shortest Code series. If you need some challenges, please try the challenge version

Task:
Every uppercase letter is a father, the corresponding lowercase letters are its sons.

Given a string:

if father and son both exist, keep them both
if one exists but not the other, delete them
one father can have multiple sons. keep it if it has at least one.
one son can have multiple fathers. keep it if it has at least one.
return the filtered string.
Examples (input --> output)
"Aab" --> "Aa"
"AabBc" -->  "AabB"
"AaaaAaab" --> "AaaaAaa"
"aAAAaAAb" --> "aAAAaAA"

def sc(s: str) -> str:
    return ''
'''

def sc(s: str) -> str:
    letras_existentes = set(s)
    
    resultado = ""
    for char in s:
        if char.lower() in letras_existentes and char.upper() in letras_existentes:
            resultado += char
            
    return resultado