# Python Function Assignments

## 1. Calculator Function

```python
def calculate(x, y, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return "Cannot divide by zero" if y == 0 else x / y
    else:
        return "Invalid operation"


x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /): ")

print("Result:", calculate(x, y, operator))
```

## 2. Sum Numbers Using `*args`

```python
def calculate_sum(*values):
    total = 0

    for value in values:
        total += value

    return total


numbers = (15, 25, 35, 45, 55)

print("Sum:", calculate_sum(*numbers))
```

## 3. Employee Information Using `**kwargs`

```python
def show_employee(**details):
    print("Employee Details")

    for field, value in details.items():
        print(field.title(), ":", value)


show_employee(
    name="Rahul",
    employee_id="EMP205",
    department="IT",
    salary=35000
)
```

## 4. Remove Duplicates While Preserving Order

```python
def get_unique_items(items):
    result = []

    for value in items:
        if value not in result:
            result.append(value)

    return result


values = [15, 25, 15, 35, 25, 45, 35, 55]

print("Original:", values)
print("After removing duplicates:", get_unique_items(values))
```

## 5. Sort List of Tuples Using Lambda

```python
records = [(3, 7), (1, 4), (5, 2), (2, 6)]

result = sorted(records, key=lambda item: item[1])

print("Before sorting:", records)
print("After sorting:", result)
```
