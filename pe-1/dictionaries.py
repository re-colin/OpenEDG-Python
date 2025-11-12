dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['two']

for k in range(len(dictionary)):
    v = dictionary[v]
    print(v)

print(v)

# In Python 3.6x, dictionaries become ordered collections by default.
# Otherwise, they don't preserve the order of their items.
# Calling print() on a dictionary may show a different ordering.
# Keys are case-sensitive. dictionary['key'] is not the same as dictionary['Key']

# Hanging indents for dictionaries are more readable.
dictionary = {
            "cat": "chat",
            "dog": "chien",
            "horse": "cheval"
}

# For loops don't work the same way with dictionaries; they are not lists or tuples, and they are not sequenced.

for key in dictionary.keys():
    print(key, "->", dictionary[key])

# keys() will return an iterable list for all keys within the dictionary.
# Use sorted() to print your dictionary keys in order.

# items() will return the dictionary's key->value items as a tuple.
for key in dictionary.items():
    print(key)


# values() will return an iterable of each dictionary key's values.
for val in dictionary.values():
    print(val)


# Replacing a key's value
dictionary['cat'] = 'minou'


# Adding a new key
dictionary.update({"duck": "canard"})
# Alternatively
dictionary['swan'] = 'cygne'
print(dictionary)


# Values cannot exist without their keys.
# Deleting a key
del dictionary['dog']


# Delete the last item
dictionary.popitem()