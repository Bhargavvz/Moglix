# Longest Valid Parentheses
 
This is my solution for the Moglix online shortlisting round assignment.
 
## Problem Statement
 
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
 
Example:
```
Input: "(()"
Output: 2
Explanation: "()" is the longest valid substring
 
Input: ")()())"
Output: 4
Explanation: "()()" is the longest valid substring
 
Input: ""
Output: 0
```
 
## My Approach
 
I used a stack to solve this problem.
 
The idea is to store indexes in the stack instead of the actual characters. I start by pushing -1 into the stack (this acts as a base so I have something to calculate length from).
 
Then I go through the string:
- If I see '(', I push its index into the stack.
- If I see ')', I pop from the stack.
  - If the stack becomes empty after popping, it means this ')' doesn't have a match, so I push its index as the new base.
  - If the stack is not empty, that means I found a valid pair, so I calculate the length using current index - stack top, and update max_len if this is bigger.
This way I only need to go through the string once, so the time complexity is O(n).
 
## How to run
 
```
python3 solution.py
```
 
This will print the output for the 3 examples given in the problem.
 
I also added a few test cases in the tests folder, can run them using:
```
pytest tests/
```
 
## Files
 
- solution.py -> main solution
- tests/test_solution.py -> test cases

## Note
 
This was a bit tricky at first, I tried a brute force way first (checking every substring) but that was O(n^2) so I looked into a better way and found the stack approach works in O(n).