# lab04_prompts.md

This document records the exact prompts used with an AI assistant and the AI's recommendation & reasoning for each problem.

## Problem 1: Finding common items

Prompt (exact):
```
I have two very large lists of product IDs from different suppliers. I need to find which product IDs appear in both lists. The order of the final list does not matter. Which Python data structure should I use and why?
```

AI recommendation & reasoning (summary):
- Recommendation: Use Python sets.
- Reasoning: Sets provide O(1) average-time membership tests and support efficient intersection operations. Converting each list to a set removes duplicates and computing the intersection yields the common elements quickly. Since order does not matter, sets are ideal.

## Problem 2: User profile lookup

Prompt (exact):
```
I have a list of user profiles (each a dict with keys 'name', 'age', 'email') and I need to perform frequent lookups by username. Performance is critical. Which data structure should I use and why?
```

AI recommendation & reasoning (summary):
- Recommendation: Convert the list into a dictionary keyed by username.
- Reasoning: Dictionaries provide O(1) average-time lookups by key. Converting the list into a mapping like `{user['name']: user for user in users}` allows extremely fast profile retrieval by username.

## Problem 3: Listing even numbers in order

Prompt (exact):
```
Given a list of integer sensor readings, extract only the even numbers while preserving their original order. Which data structure or approach should I use and why?
```

AI recommendation & reasoning (summary):
- Recommendation: Use a list and a list comprehension (or iterative filter) to preserve order.
- Reasoning: Lists maintain order. A list comprehension like `[n for n in numbers if n % 2 == 0]` is concise, efficient, and preserves the original order of even numbers.
