N = int(input())
for i in range(N):
    word = list(input())
    for j in range(len(word)):
        if word[j].isalpha():
            word[j] = chr(ord(word[j]) + 3)
    word = word[::-1]
    for j in range((len(word)//2), len(word)):
        word[j] = chr(ord(word[j])-1)
    for letter in word:
        print(letter, end='')
    print()
