import random

word = input("Word to find: ").upper()
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

guess = "".join(random.choice(abc) for _ in word)

for step in range(5000):
    print("Step", step, ":", guess)
    if guess == word:
        print("Found 🎉 ->", word)
        break
    new = ""
    for i in range(len(word)):
        new += guess[i] if guess[i] == word[i] else random.choice(abc)
    guess = new