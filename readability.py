from cs50 import get_string


text = get_string("Text: ")

letters = 0
words = 1
sentences = 0
length = len(text)

for _ in range(length):
    if text[_].isalpha():
        letters += 1
    elif text[_] == " ":
        words += 1
    elif text[_] in [".","!","?"]:
        sentences += 1

l = (letters/words) * 100
s = (sentences/words) * 100
index = 0.0588 * l - 0.296 * s - 15.8
grade = round(index)
if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")

