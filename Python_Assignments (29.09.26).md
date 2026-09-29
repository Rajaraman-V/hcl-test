# Python Assignments

## 1. Print All Prime Numbers Between Input Range

```python
start = int(input("Enter lower limit: "))
end = int(input("Enter upper limit: "))

print("Prime numbers:")

for number in range(start, end + 1):
    if number < 2:
        continue

    is_prime = True

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")

print()
```

## 2. Factorial Using Recursion

```python
def find_factorial(value):
    if value <= 1:
        return 1
    return value * find_factorial(value - 1)


number = int(input("Enter a number: "))
result = find_factorial(number)

print("Factorial:", result)
```

## 3. Square of Numbers Using Lambda

```python
values = [2, 4, 6, 8, 10]

get_square = lambda n: n ** 2

result = list(map(get_square, values))

print("Numbers:", values)
print("Squares:", result)
```

## 4. Find the Second Largest Element in a List

```python
numbers = [15, 28, 9, 47, 35, 22]

distinct = sorted(set(numbers), reverse=True)

second_largest = distinct[1]

print("Given list:", numbers)
print("Second largest:", second_largest)
```

## 5. Count Frequency of Characters in a String

```python
text = input("Enter a string: ")

count = {}

for letter in text:
    count[letter] = count.get(letter, 0) + 1

print("Character frequency:")

for letter in count:
    print(letter, ":", count[letter])
```

## 6. Calculate Area of a Circle Using Math Library

```python
import math

r = float(input("Enter the radius: "))

circle_area = math.pi * (r ** 2)

print("Circle area:", circle_area)
```

## 7. Reverse a String Without Using Built-in Reverse

```python
text = input("Enter a string: ")

result = ""

for index in range(len(text) - 1, -1, -1):
    result += text[index]

print("Original:", text)
print("Reverse:", result)
```

## 8. Remove Duplicates from a List

```python
numbers = [12, 25, 12, 35, 25, 48, 35, 60]

result = []

for value in numbers:
    if value not in result:
        result.append(value)

print("Original list:", numbers)
print("Unique list:", result)
```

## 9. Merge Two Dictionaries

```python
student = {
    "name": "Rahul",
    "age": 20
}

details = {
    "branch": "CSE",
    "college": "Engineering College"
}

combined = student.copy()
combined.update(details)

print("Dictionary 1:", student)
print("Dictionary 2:", details)
print("Combined dictionary:", combined)
```

## 10. Fibonacci Series Using Recursion

```python
def fib(number):
    if number < 2:
        return number
    return fib(number - 1) + fib(number - 2)


count = int(input("Enter number of terms: "))

series = []

for position in range(count):
    series.append(fib(position))

print("Fibonacci series:", *series)
```
