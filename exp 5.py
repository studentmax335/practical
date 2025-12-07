def count_chars(filename):
    vowels = "aeiouAEIOU"
    v = c = s = 0

    with open(filename, "r") as file:
        text = file.read()

    for ch in text:
        if ch in vowels:
            v += 1
        elif ch.isalpha():
            c += 1
        elif ch.isspace():
            s += 1

    print(f"Vowels: {v}")
    print(f"Consonants: {c}")
    print(f"Spaces: {s}")

fname = input("Enter file name: ")
count_chars(fname)
