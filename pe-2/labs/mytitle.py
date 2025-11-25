def mytitle(string):
    t_string = ''
    t_string += string[0].upper()

    for letter in range(len(string)):
        try:
            letter += 1

            if string[letter - 1] == chr(32):
                t_string += string[letter].upper()
                letter += 1
                continue

            t_string += string[letter].lower()

        except IndexError:
            return t_string



s1 = 'pRinGlE sToOp'
s2 = 'sIx sAyVen'
s3 = 'thErE aRe feAtUreS oF tHesE rObOts thAT yOu dOnT uNdeRstaNd'

print(mytitle(s1))
print(mytitle(s2))
print(mytitle(s3))