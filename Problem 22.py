f = open("p022_names.txt", "r")
names = sorted(f.read().replace('"', "").split(","))
name_scores = 0

def char_to_int(name):
    value = 0
    for letter in name:
        value += ord(letter) - 64
    return value

for name in names:
    name_scores += (names.index(name)+1) * char_to_int(name)

print(name_scores)
