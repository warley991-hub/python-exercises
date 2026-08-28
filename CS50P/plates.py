def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    checklist=[]
    ja_achou_numero= False
    for i, character in enumerate(s):
        if s[i].isdigit():
            if i < len(s) -1 and s[i+1].isalpha():
                checklist.append('Invalid')
        elif s.isspace():
            checklist.append('Invalid')
        elif s.endswith(' '):
            checklist.append('Invalid')
        elif character in "'.,;:?!\"":
            checklist.append('Invalid')
        else:
            checklist.append('Valid')
        if character.isdigit():
            if character == '0' and ja_achou_numero == False:
                checklist.append('Invalid')
            ja_achou_numero = True

    if not s[:2].isalpha():
        checklist.append('Invalid')
    if ' ' in s:
        checklist.append('Invalid')
    if len(s) > 6 or len(s) <2:
        checklist.append('Invalid')
    if not s:
        checklist.append('Invalid')
    if 'Invalid' in checklist:
        return False
    else:
        return True

main()
