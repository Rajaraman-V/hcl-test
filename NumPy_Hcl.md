# NUMPY ASSIGNMENT

**Course:** Python Programming
**Topic:** NumPy – Basics to Advanced

# Question 1 – Student Scores Array

**Problem:**
Create a NumPy array containing five student scores and display its basic properties.

```python
import numpy as np

scores = np.array([81, 67, 94, 59, 88])

print("Scores:", scores)
print("Dimensions:", scores.ndim)
print("Shape:", scores.shape)
print("Total elements:", scores.size)
print("Data type:", scores.dtype)
```

# Question 2 – Student Scores Access

**Problem:**
Use NumPy indexing and slicing to access selected student scores.

```python
import numpy as np

scores = np.array([74, 89, 61, 95, 78])

print("Scores:", scores)
print("First student:", scores[0])
print("Third student:", scores[2])
print("Last student:", scores[-1])
print("First three:", scores[:3])
print("Last two:", scores[-2:])
print("Students 2 to 4:", scores[1:4])
```

# Question 3 – Subject-wise Score Matrix

**Problem:**
Create scores for five students in three subjects and reshape them into a 5 × 3 matrix.

```python
import numpy as np

scores = np.array([
    81, 76, 92,
    68, 73, 85,
    90, 87, 79,
    61, 66, 72,
    96, 91, 88
])

score_table = scores.reshape(5, 3)

print("Score Matrix:")
print(score_table)
print("Matrix shape:", score_table.shape)
```

# Question 4 – Internal and External Scores

**Problem:**
Combine internal and external marks to calculate the total score for each student.

```python
import numpy as np

internal_marks = np.array([18, 21, 19, 23, 20])
external_marks = np.array([67, 64, 71, 62, 75])

total_marks = np.add(internal_marks, external_marks)

print("Internal:", internal_marks)
print("External:", external_marks)
print("Total:", total_marks)
```

# Question 5 – Passing Score Analysis

**Problem:**
Use Boolean indexing to find students who scored at least 50 marks.

```python
import numpy as np

scores = np.array([42, 67, 58, 49, 86])

passed = scores[scores >= 50]

print("Scores:", scores)
print("Passing scores:", passed)
```

# Question 6 – Average Score Analysis

**Problem:**
Calculate the average score of every student across three subjects.

```python
import numpy as np

scores = np.array([
    [81, 76, 92],
    [68, 73, 85],
    [90, 87, 79],
    [61, 66, 72],
    [96, 91, 88]
])

student_average = np.mean(scores, axis=1)

print("Scores:")
print(scores)
print("Average for each student:")
print(student_average)
```

# Question 7 – Class Statistics

**Problem:**
Calculate the total, average, maximum, minimum, and standard deviation of a set of scores.

```python
import numpy as np

scores = np.array([71, 84, 93, 69, 57])

stats = {
    "total": np.sum(scores),
    "average": np.mean(scores),
    "maximum": np.max(scores),
    "minimum": np.min(scores),
    "std": np.std(scores)
}

print("Scores:", scores)
print("Total:", stats["total"])
print("Average:", stats["average"])
print("Maximum:", stats["maximum"])
print("Minimum:", stats["minimum"])
print("Standard deviation:", stats["std"])
```

# Question 8 – Subject-wise Score Totals

**Problem:**
Use an axis operation to calculate the total score for every subject.

```python
import numpy as np

scores = np.array([
    [81, 76, 92],
    [68, 73, 85],
    [90, 87, 79],
    [61, 66, 72],
    [96, 91, 88]
])

subject_totals = scores.sum(axis=0)

print("Scores:")
print(scores)
print("Subject totals:", subject_totals)
```

# Question 9 – Student-wise Score Totals

**Problem:**
Use an axis operation to calculate the total score for every student.

```python
import numpy as np

scores = np.array([
    [81, 76, 92],
    [68, 73, 85],
    [90, 87, 79],
    [61, 66, 72],
    [96, 91, 88]
])

student_totals = scores.sum(axis=1)

print("Scores:")
print(scores)
print("Student totals:", student_totals)
```

# Question 10 – Student Ranking

**Problem:**
Sort student totals in descending order and display their ranks.

```python
import numpy as np

totals = np.array([258, 271, 224, 293, 249])

order = np.argsort(totals)[::-1]

print("Total marks:", totals)

for position, student_index in enumerate(order, 1):
    print(position, student_index + 1, totals[student_index])
```

# Question 11 – Unique Score Analysis

**Problem:**
Find the distinct scores from an array that contains repeated values.

```python
import numpy as np

scores = np.array([88, 75, 88, 69, 94, 75])

different_scores = np.unique(scores)

print("Scores:", scores)
print("Different scores:", different_scores)
```

# Question 12 – Missing Score Analysis

**Problem:**
Calculate the average of an array while ignoring a missing value represented by np.nan.

```python
import numpy as np

scores = np.array([81, 74, np.nan, 89, 66])

valid_average = np.nanmean(scores)

print("Scores:", scores)
print("Average of available scores:", valid_average)
```

# Question 13 – Grade Classification

**Problem:**
Assign grades to students based on their scores using NumPy conditions.

```python
import numpy as np

scores = np.array([93, 86, 77, 64, 48])

grades = np.select(
    [
        scores >= 90,
        scores >= 80,
        scores >= 70,
        scores >= 60
    ],
    [
        "A",
        "B",
        "C",
        "D"
    ],
    default="F"
)

print("Scores:", scores)
print("Grades:", grades)
```

# Question 14 – Random Score Generation

**Problem:**
Generate random scores using NumPy and calculate basic statistics.

```python
import numpy as np

np.random.seed(15)

scores = np.random.randint(1, 101, 6)

print("Generated scores:", scores)
print("Total:", scores.sum())
print("Average:", scores.mean())
print("Highest:", scores.max())
print("Lowest:", scores.min())
print("Standard deviation:", scores.std())
```

# Question 15 – Student Performance Analysis

**Problem:**
Perform a complete analysis of five students across three subjects.

```python
import numpy as np

scores = np.array([
    [81, 76, 92],
    [68, 73, 85],
    [90, 87, 79],
    [61, 66, 72],
    [96, 91, 88]
])

totals = scores.sum(axis=1)
averages = scores.mean(axis=1)
highest = scores.max(axis=1)
lowest = scores.min(axis=1)

overall_average = totals.mean()
above_average = np.flatnonzero(totals > overall_average) + 1

print("Scores:")
print(scores)
print("Student totals:", totals)
print("Student averages:", averages)
print("Highest per student:", highest)
print("Lowest per student:", lowest)
print("Overall average total:", overall_average)
print("Students above overall average:", above_average)
```
