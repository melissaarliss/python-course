## Reading Questions

1. What is a nested loop?

A nested loop is a loop within a loop. The inner loop will complete each time the outer loop runs. They have really bad algorithmic efficiency - n^2.

2. Which kind of loop is based on a conditional statement: while loops or for loops?

While loops are based on conditionals; when it runs, they are always checking *if* the condition is still true.

3. When you want to iterate a specific number of times, would you typically use a while loop or a for loop?

For loop, because the number of times they run is based on a pre-set iterator.

4. Is it possible to loop through a string one letter at a time? What is the example given in the article?

Yes, you can iterate through a string and print out each letter. Eg:

```py
name = "Melissa"
for letter in name:
	print(letter)
```

5. Extrapolate from what you learned in the articles: Do you think a for loop be nested inside a while loop? Why or why not?

Yes, as long as there's still an exit condition for the while loop outside of the for loop.


