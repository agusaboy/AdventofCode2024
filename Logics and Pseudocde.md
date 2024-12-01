# Logics and Pseudocde

## Day 1

**Difference**
Input= two list of numbers
Output= the addition of differences

- First, I have to sort two list from smallest to largest
- Get the difference (rest) of the number of same index in both lists
    - If List B item is smaller than List A, i'll need to multiply by -1
- Add all differences


**Similarities score**
Input= two list of numbers
Output= similarity score between list

- Get multiplier: count how many times an element of listA appears on list B (For each number in listA multiply the number by the times it appears on list B)
- Multiply by elements on listA
- Add multiplication results 