import random

uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letter = uppercase_letter.lower()
digit_letter = "123456789"
symbols = "[]{}+=-_()*&^%$#@!~||\\//.,;"

upper, lower, digit, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letter
if lower:
    all += lowercase_letter
if digit:
    all += digit_letter
if syms:
    all += symbols

length = 20
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
