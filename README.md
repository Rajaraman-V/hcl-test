# hcl-test

# Python Programming (25.09.26)
## Q1. Student Attendance Analysis

A college maintains a list of student IDs. Some students may appear multiple times. Find the **longest continuous sequence in which no student ID is repeated**.

```python
arr = list(map(int, input().split()))

longest = 0

for i in range(len(arr)):
    seen = set()

    for j in range(i, len(arr)):
        if arr[j] in seen:
            break

        seen.add(arr[j])
        longest = max(longest, j - i + 1)

print(longest)
```

## Q2. Online Shopping Price Analysis

Given a list of discount values, find the **continuous range having the maximum total discount value**.

```python
arr = list(map(int, input().split()))

current = arr[0]
maximum = arr[0]

for i in range(1, len(arr)):
    current = max(arr[i], current + arr[i])
    maximum = max(maximum, current)

print(maximum)
```

## Q3. Rainwater Collection System

Given the heights of buildings, calculate the **total amount of rainwater that can be trapped between the buildings**.

```python
arr = list(map(int, input().split()))

water = 0

for i in range(len(arr)):
    left = max(arr[:i + 1])
    right = max(arr[i:])

    water += min(left, right) - arr[i]

print(water)
```

## Q4. Employee Performance Analysis

Given monthly performance scores containing positive and negative values, find the **continuous period having the highest total performance score**.

```python
arr = list(map(int, input().split()))

current = arr[0]
maximum = arr[0]

for i in range(1, len(arr)):
    current = max(arr[i], current + arr[i])
    maximum = max(maximum, current)

print(maximum)
```

## Q5. Product Sales Analysis

Given a list of sales-related values, find the **continuous range having the maximum product**.

```python
arr = list(map(int, input().split()))

maximum = arr[0]
minimum = arr[0]
answer = arr[0]

for i in range(1, len(arr)):
    if arr[i] < 0:
        maximum, minimum = minimum, maximum

    maximum = max(arr[i], maximum * arr[i])
    minimum = min(arr[i], minimum * arr[i])

    answer = max(answer, maximum)

print(answer)
```

## Q6. Customer Purchase History

Given product IDs purchased in chronological order, find the **longest continuous sequence in which every product ID is unique**.

```python
arr = list(map(int, input().split()))

longest = 0

for i in range(len(arr)):
    seen = set()

    for j in range(i, len(arr)):
        if arr[j] in seen:
            break

        seen.add(arr[j])
        longest = max(longest, j - i + 1)

print(longest)
```

## Q7. Bank Transaction Analysis

Given transaction amounts and a target amount, count the **number of continuous groups of transactions whose sum is exactly equal to the target**.

```python
arr = list(map(int, input().split()))
target = int(input())

count = 0

for i in range(len(arr)):
    total = 0

    for j in range(i, len(arr)):
        total += arr[j]

        if total == target:
            count += 1

print(count)
```

## Q8. Employee Skill Grouping

Given a list of strings, group the strings that contain the **same characters in a different order**.

```python
words = input().split()

groups = {}

for word in words:
    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

for group in groups.values():
    print(group)
```

## Q9. Network Packet Analysis

Given packet identifiers, find the **longest sequence of consecutive numbers**, regardless of their original order.

```python
arr = list(map(int, input().split()))

numbers = set(arr)
longest = 0

for num in numbers:
    if num - 1 not in numbers:
        current = num
        length = 1

        while current + 1 in numbers:
            current += 1
            length += 1

        longest = max(longest, length)

print(longest)
```

## Q10. Hospital Appointment Scheduling

Given appointment start and end times, **merge all overlapping appointment ranges** so that the final schedule contains only non-overlapping ranges.

```python
n = int(input())

intervals = []

for i in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

intervals.sort()

merged = []

for interval in intervals:
    if not merged or interval[0] > merged[-1][1]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])

for interval in merged:
    print(interval[0], interval[1])
```







# Python programming

# PROGRAM 1
```
nums = input().split(',')
for n in nums:
    if int(n, 2) % 5 == 0:
        print(n)
```


# PROGRAM 2
```
s = input()
letters = 0
digits = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
print("LETTERS", letters)
print("DIGITS", digits)
```


# PROGRAM 3
```
def fact(n):
    if n == 0 or n == 1:
      return 1
    return n * fact(n - 1)

n = int(input())
print(fact(n))
```
