1. Integer (int)
Description: Whole numbers, both positive and negative.
Examples: -10, 0, 42
Common Operations:
Arithmetic: +, -, *, // (floor division), % (modulus), ** (exponentiation)
Comparison: <, >, <=, >=, ==, !=
python
Copy code
a = 5
b = 2
print(a + b)  # 7
print(a // b) # 2
print(a ** b) # 25
2. Float (float)
Description: Numbers with decimal points.
Examples: 3.14, -0.001, 2.0
Common Operations:
Arithmetic: Same as integers, but division / always returns a float.
Methods: .is_integer() checks if it’s equivalent to an integer.
python
Copy code
x = 3.5
y = 1.2
print(x - y)         # 2.3
print(x / y)         # 2.9166666666666665
print((5.0).is_integer())  # True
3. String (str)
Description: Sequence of characters, enclosed in single, double, or triple quotes.
Examples: 'hello', "world", '''multi-line'''
Common Operations:
Concatenation: +
Repetition: *
Indexing/Slicing: str[0], str[1:5]
Methods: .upper(), .lower(), .strip(), .replace(), .find(), .split(), .join()
python
Copy code
s = "Python"
print(s[0])        # 'P'
print(s[2:5])      # 'tho'
print(s.upper())   # 'PYTHON'
print(s + " Rocks") # 'Python Rocks'
print("Hi! " * 3)  # 'Hi! Hi! Hi! '
4. Boolean (bool)
Description: Represents True or False.
Examples: True, False
Common Operations:
Logical: and, or, not
Comparison: ==, !=, <, >
Casting: bool(0) is False, bool(1) is True
python
Copy code
is_raining = True
is_sunny = False
print(is_raining and is_sunny)  # False
print(not is_raining)          # False
print(5 > 3)                   # True
5. Other Notes on Operations:
Type Conversion:

int(), float(), str(), bool()
Examples:
python
Copy code
print(int(3.7))    # 3
print(float(10))   # 10.0
print(bool(""))    # False
Type Checking:

Use type() to determine the type of a variable.
Example:
python
Copy code
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type(True))     # <class 'bool'>


1. Characteristics of int
Python's int type is unbounded (limited only by system memory). This means you can work with arbitrarily large integers, unlike many languages where integers have fixed sizes (e.g., 32-bit or 64-bit).
Default base is decimal (base 10), but integers can also be defined in other bases:
Binary: 0b101 → 5
Octal: 0o12 → 10
Hexadecimal: 0xA → 10
2. Basic Arithmetic Operations
Addition (+), subtraction (-), multiplication (*), division (/), floor division (//), modulus (%), exponentiation (**).
Example:
python
Copy code
a = 7
b = 3
print(a + b)  # 10
print(a // b) # 2 (floor division)
print(a % b)  # 1 (remainder)
print(a ** b) # 343 (7^3)
3. Bitwise Operations
Operate directly on the binary representation of integers.
AND (&): Performs a bitwise AND.
OR (|): Performs a bitwise OR.
XOR (^): Performs a bitwise exclusive OR.
NOT (~): Performs a bitwise NOT.
Shift left (<<): Shifts bits to the left.
Shift right (>>): Shifts bits to the right.
Example:
python
Copy code
x = 5       # Binary: 0101
y = 3       # Binary: 0011

print(x & y)  # 1 (Binary: 0001)
print(x | y)  # 7 (Binary: 0111)
print(x ^ y)  # 6 (Binary: 0110)
print(~x)     # -6 (2's complement)
print(x << 1) # 10 (Binary: 1010)
print(x >> 1) # 2 (Binary: 0010)
4. Numeric Base Conversion
Convert integers between different bases using the built-in functions:
bin(): Converts to binary string.
oct(): Converts to octal string.
hex(): Converts to hexadecimal string.
Example:
python
Copy code
n = 42
print(bin(n))  # '0b101010'
print(oct(n))  # '0o52'
print(hex(n))  # '0x2a'
5. Advanced Math Operations
Power and Modulus Together (pow()):

Efficiently compute (x ** y) % z using pow(base, exp, mod).
Example:
python
Copy code
print(pow(2, 10, 1000))  # 24 (equivalent to (2^10) % 1000)
Absolute Value:

Use abs() to get the absolute value of an integer.
Example:
python
Copy code
print(abs(-42))  # 42
Divmod:

Simultaneously get quotient and remainder using divmod(a, b).
Example:
python
Copy code
print(divmod(10, 3))  # (3, 1)
6. Integer Overflow
Python's int type does not overflow, as it dynamically allocates more memory when necessary:
python
Copy code
large_number = 10**100  # 1 followed by 100 zeros
print(large_number)
7. Performance Optimizations
Caching for Small Integers:

Python caches integers in the range -5 to 256 to optimize performance. These are reused rather than creating new objects.
Example:
python
Copy code
a = 100
b = 100
print(a is b)  # True (same memory reference)
Custom Integers with __int__:

You can define your own objects that behave like integers by overriding __int__ or __index__ methods.
8. Useful Libraries
math Module:

Provides advanced mathematical operations for integers.
Examples:
python
Copy code
import math
print(math.gcd(42, 56))   # 14 (greatest common divisor)
print(math.factorial(5)) # 120
print(math.isqrt(16))    # 4 (integer square root)
random Module:

Generate random integers.
Example:
python
Copy code
import random
print(random.randint(1, 10))  # Random integer between 1 and 10 (inclusive)
9. Practical Use Cases
Data Processing:
Use integers for IDs, counters, and indexes in loops.
Cryptography:
Integer arithmetic (e.g., modular exponentiation) is foundational for cryptographic algorithms.
Bit Manipulation:
Useful for optimizing performance, especially in low-level programming and encoding schemes.