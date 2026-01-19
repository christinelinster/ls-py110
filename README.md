# PY110: Programming Foundations with Python (Intermediate)

**Repository:** [https://github.com/christinelinster/ls-py110](https://github.com/christinelinster/ls-py110)

This course builds upon the foundations of programming by diving deep into **Python Collections** and **Problem Solving Methodologies**. It transitions from writing "working code" to writing "efficient and idiomatic code." The curriculum focuses on mastering the manipulation of complex, nested data structures and applying a rigorous, step-by-step process (PEDAC) to solve algorithmic challenges.

## Core Concepts Mastered

### Python Collections & Sequences
* **Advanced Structures:** Deep dive into `lists`, `tuples`, `sets`, and `dictionaries`.
* **Nested Collections:** Strategies for accessing and modifying multi-dimensional data (e.g., a list of dictionaries).
* **Iterable Unpacking:** Using `*` and `**` operators to unpack sequences into function arguments or other variables.
* **Sorting:** Understanding stability and implementing custom sort keys (e.g., sorting a list of strings by the number of vowels).


### Iteration & Transformation
* **Comprehensions:** Replacing loops with idiomatic List, Dictionary, and Set comprehensions for cleaner syntax.
* **Selection & Transformation:** Functional patterns to filter data (`select`) or modify it (`transform`) without side effects.
* **Generators:** Understanding lazy evaluation and memory efficiency with generator expressions.

### Problem Solving Framework (PEDAC)
* **P**roblem: Understanding the requirements and edge cases.
* **E**xamples: creating test cases to verify logic.
* **D**ata Structure: Selecting the right tool (e.g., Set vs. List) for the job.
* **A**lgorithm: Writing plain-English steps before coding.
* **C**ode: Translating the algorithm into Python.


### Debugging
* **pdb (Python Debugger):** Moving beyond `print()` debugging.
* **Techniques:** Setting breakpoints, stepping through execution (`step`, `next`), and inspecting the call stack to isolate logical errors.


## Projects

### [Tic Tac Toe](./lesson_3/tictactoe.py)
An implementation of the classic game that separates the display logic from the game engine.
* **Key Concept:** Managing a complex "Game State" using nested data structures.
* **Features:** A smart AI opponent that can detect threats and winning moves.

### [Twenty-One (Blackjack)](./lesson_3/twenty_one.py)
A complex card game requiring the management of a deck, dealing logic, and variable Ace values.
* **Key Concept:** Game Loop architecture and state evaluation.
* **Features:** Robust handling of user input and precise implementation of "dealer rules."

## Repository Structure

```text
ls-py110/
├── lesson_1/              # Collections, Sorting, and Sequence fundamentals
├── lesson_3/              # Larger Programs: Tic Tac Toe & Twenty-One
└── practice-problems/     # Algorithm practice (Easy, Medium, Hard)
```

## Key Takeaways

* Ability to choose the most efficient data structure for a given problem.
* Proficiency in reading and writing nested loops and comprehensions.
* Discipline to apply the PEDAC process to ambiguous or complex problems.
* Skill in debugging code systematically using pdb.

## License
MIT
