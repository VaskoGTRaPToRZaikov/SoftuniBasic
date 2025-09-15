import math

word_score = 0
most_pow_score = 0
most_pow_word = ""

while True:
    word = input()

    if word == "End of words":
        break

    for char in word:
        word_score += ord(char)

    if word[0] in "aeiouyAEIOUY":
        word_score *= len(word)

    else:
        word_score = math.ceil(word_score / len(word))

    if most_pow_score < word_score:
        most_pow_score = word_score
        most_pow_word = word

    word_score = 0

print(f"The most powerful word is {most_pow_word} - {most_pow_score}")