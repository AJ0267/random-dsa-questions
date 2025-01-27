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

**Example**:  
For `n = 4`, the distinct ways are:  
1. 1+1+1+1  
2. 1+1+2  
3. 1+2+1  
4. 2+1+1  
5. 2+2 

---

