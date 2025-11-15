# MODULE 2 part 2
# =====================================================================

# PRACTICE LABS:
# https://edube.org/learn/pe-2/lab-improving-the-caesar-cipher-3
# https://edube.org/learn/pe-2/lab-palindromes-4
# https://edube.org/learn/pe-2/lab-anagrams-3
# https://edube.org/learn/pe-2/lab-the-digit-of-life-3
# https://edube.org/learn/pe-2/lab-find-a-word-3
# https://edube.org/learn/pe-2/lab-sudoku-4

# =====================================================================
# STRING ENCODING

# ASCII - american standard code for information interchange
# I18N (Internationalization)
# code point: a number which makes a character
# higher half of the 128 code points is stored in a code page - a standard for specific national characters. e.g different code pages exist for western and eastern euripe, cryrillic, greek, arabic, hewbrew etc. Meaning not all code points within code pages are made equal.

# Code pages arent a permanent solution. 
# Unicode ended up solving it.
# Unicode assigns unique characters to more than a million code points.
# The first 128 UC code points are identical to ASCII.
# Every point after it takes into account every single other standard.

# UC standard names all available characters and assigns them to planes.
# UCS-4 (Universal Character Set 4) uses 32 bits to store each character.
# Some utilities require a BOM (byte order mark) announcing nature of file contents.

# UTF-8 (Unicode Transformation Format) is more common, saving more space - only using as many bits for each code point as it needs to represent them.
# latin chars occupy 8 bits, non-latin 16 bits, CJK 24 bits.

# Python fully supports UTF-8.Meaning Python is fully I18Ned.

# =====================================================================
# STRINGS
# Python strings are immutable sequences but cant always be treated like lists.
# e.g, *del* and append() operations dont work on strings.

# Escape characters (\) arent included in the calculated length of a string.
i_am = "I\'m"
print(len(i_am)) # 3

# Escape *Codes* *are* - counted as 1 character.
multiline = """Line #1
Line #2"""
print(len(multiline))

# Operators that work differently based on data type is called *overloading*.
str1 = 'a'
int1 = 3
print(str1 * 6)
print(int1 * 7)

# Ordinal (ord)/unicode/ascii code point value access. Reverse is chr().
char = "C"
print(ord(char))

# Strings can be treated like lists sometimes.
string = "silly walks"
for s in range(len(string)):
    print(string[s], end="")

for s in string:
    print(s, end="")

# Slicing (Uninclusive range)
string = "Springs"
print("")
print(string[1:3])
print(string[2:4])
print(string[0:5])

# is, is not - boolean
print("F" in string)
print("r" in string)

# min() and max() - minimum and maximum ASCII code points
print(min(string))
print(max(string))

# index() - get first occurence of character
print(string.index("r"))

# list() creates list out of string characters
print(list(string))

# counts all occurances of specified element 
print(string.count("s"))

# Capitalize - first char is uppercase, rest is lowercase
string = "sPrInGs".capitalize()
print(string.capitalize())

# center() - uses a space by default
print('[' + string.center(20, "*") + ']')

# endswith()
print(string.endswith("ings"))

# find() - safer than index(). non-existent strings return -1, works with strings only. returns first occurance (index) of pattern
print(string.find("ri"))
# extra argument - specifies *where* to start the search
string2 = "bbabbaabba"
print(string2.find("bba", 3))
# A third argument specifies first index which wont be taken into consideration during search.

# isalnum() (bool) - checks if string contains only digits or alphabetical chars
print("$prings".isalnum())
print("$".isalnum())
print("2223".isalnum())

# isalpha() (bool) - interested in letters only. if string contains digits, returns False.
# if string contains alphabetical letters, returns True.
print(string.isalpha())
print("Mooo".isalpha())
print("mooo".isalpha())
print("2234".isalpha())

# isdigit() (bool) is the inverse, only paying attention to numbers.
print("2234".isdigit())
print(string.isdigit())

# islower() (bool) accepts lower-case letters only. Anything else and it returns False.
print("Springs".islower()) # False
print("springs".islower()) # True
print("2234".islower())    # False

# isupper() (bool) - antithesis to islower(). 
print("SPRINGS".isupper()) # True
print("Springs".isupper()) # False
print("springs".isupper()) # False

# isspace() (bool) - Identifies whitespace only.
print("".isspace())   # False
print(" ".isspace())  # True
print("\n".isspace()) # True
print("Sink tap".isspace()) # False

# join() - Joins a list of strings together by a separator. Returns the new string.
print(" ".join(["Sink", "tap"]))
print("-".join(["Sink", "tap"]))

# lower() - Returns an all lowercase copy of the original string 
print("Springs".lower())
print("springs".lower())
print("SPRINGS".lower())

# lstrip() - Returns copy of string with removed whitespaces
# Single parameter version can remove all characters enlisted in its argument - not just whitespace.
string2 = "Spgonle.com"
print(string2.lstrip("c"))
print("\nSprings ".lstrip())
print("\nSprings.com".lstrip(".com"))
print("Sink tap".lstrip("tap"))

# replace() - Returns a copy where all occurrences of the first argument are replaced by the second argument.
# Third parameter limits the number of replacements.
print("Spoing".replace("oing", "ringle"))
print("Spoing poingle".replace("oing", "ringle", 1))
print("Spoing poingle".replace("oing", "ringle", 2))

# rfind() - Like find(), but starts searching from the end of the string, not the beginning.
print("spingle pingle doop doopple".rfind("oop"))
print("spingle pingle doop doopple".rfind("oop", 2))
# print("spingle pingle doop doopple oop".rfind("oop", 2, 1))

# rstrip() looks at the opposite side of the string.
print("[ " + "epsilon" + " ]")
print("[ " + "epsilon" + " ]".rstrip())

# split() - Splits string, returning list of all detected substrings
# Assumes strings are limited by whitespaces - these are stripped in the list.
print("phi chi psi".split())
print("phi-chi-psi".split('-'))

# startswith() - Antithesis to endswith()
print("Spring".startswith("Spr"))

# swapcase() - Reverses cases for a string. 
print("MICHAEL!!!!!!!!!!".swapcase())
print("MICHAEL!!!!!!!!!!".swapcase().swapcase())

# title() - Changes every words first letter to uppercase, turning the rest to lowercase.
print("i know that i know nothing".title())

# =====================================================================
# STRING OPERATIONS
# Python and coding languages in general dont pick up on linguistics.
# It only sees code points.
# Operations are case sensitive.

# when comparing two strings of different lengths, and the shorter one is identical to the start of the longer one, the longer string is considered greater.
print('alpha' < 'alphabet')  # True
print('alpha' == 'Alpha')    # False
print('Alpha' != 'alphabet') #  True

# Upper-case letters are taken as lesser than lowercase.
print('alpha' > 'Alpha') # 

# Sorting
# a really sophisticated case of comparing.
# sorted() creates a sorted copy of the list.
# sort() modifies the list itself, and doesnt return anything.
firstg = ['omega', 'alpha', 'pi', 'gamma', 'delta']
secg = ['omega', 'alpha', 'pi', 'gamma', 'delta']
print(sorted(firstg))

secg.sort()
print(secg)

# Certain operations on string has to do with their code points.
# This is not necessarily sorted alphabetically, but by the order of each characters code points.
s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3)
print(s3[1])


s2 = '12.8' 
i = float(s2) # s2 must be converted to a float first
i = int(i)
print(i)

# *Fuzzy* string comparison algorithms have been created in response to Python's unsatisfactory way of allowing for strict comparisons with its built-in methods.
# e.g, Hamming distance determines the similarity of two strings. 
# Another way of comparing strings is finding their *acoustic* similarity. e.g Soundex. (invented in 1918)


# Because of limited native float and integer data precision, sometimes it makes sense to store and process huge numeric values as strings. 

# 