text = input("Please enter a string:")
dictionary = {}
for keys in text:
    dictionary[keys] = dictionary.get(keys, 0) + 1
l1 = list(dictionary)
result = []
for key in dictionary:
    result.append((dictionary[key], key))
    result.sort(reverse=True)
for count, letter in result:
    print(letter, count)

