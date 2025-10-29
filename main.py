import string

password = input("Enter your password: ")
R = input("Enter Speed: ")

L = len(password)
has_lower = any(c.islower() for c in password)
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in string.punctuation for c in password)

S = 0
if has_lower:
    S += 26
if has_upper:
    S += 26
if has_digit:
    S += 10
if has_special:
    S += 33

time = (S ** L) / int(R)

print("Time to crack the password:", time, "seconds")
