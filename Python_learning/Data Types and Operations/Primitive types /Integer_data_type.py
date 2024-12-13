"""
Characteristics of int

Python's int type is unbounded (limited only by system memory). This means you can work with arbitrarily large integers, unlike many languages where integers have fixed sizes (e.g., 32-bit or 64-bit).
Default base is decimal (base 10), but integers can also be defined in other bases:

Binary      : 0b101 → 5
Octal       : 0o12 → 10
Hexadecimal : 0xA → 10
"""

#About Integer data type usage
"""
Integer (int)
Description      : Whole numbers, both positive and negative.
Examples         : -10, 0, 42
    Common Operations    :
        Arithmetic       : +, -, *, // (floor division), % (modulus), ** (exponentiation)
        Comparison       : <, >, <=, >=, ==, !=

"""
a = 5
b = 2
print(a + b)  # 7
print(a // b) # 2
print(a ** b) # 25
