## Notes

---

### 1. **Two Sum**
- **Notes**:  
Using "Diff" in Two Sum

For each number num, we calculate:
- diff=target−num
- diff=target−num

If diff is already in our hash map, we return the indices. This avoids nested loops and makes the solution efficient (O(n) time). 

---

### 2. **Climbing stairs**
- **Notes**:  
The number of ways to reach step `n` is the sum of the ways to reach step `n-1` and `n-2`.
Use two variables to track the number of ways to the last two steps.

- **Example**:  
For `n = 4`, the distinct ways are:  
  1+1+1+1  
  1+1+2  
  1+2+1  
  2+1+1  
  2+2 

---

### 3. **Valid Parentheses**
- **Notes**:  
  - Use a stack to track opening brackets.
  - For each closing bracket, check if it matches the top element of the stack.
  - If the stack is empty at the end, the sequence is valid.

- **Example**:  
  1. Initially, the stack is empty: [].
  2. Push ( onto the stack: ['('] — now ( is the top element.
  3. Push { onto the stack: ['(', '{'] — now { is the top element.
  4. Pop the top element: stack.pop() removes { — the stack becomes ['('].
  5. Pop the top element again: stack.pop() removes ( — the stack becomes empty [].

---

