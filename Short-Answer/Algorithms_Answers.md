#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) As we have a while loop we will begin by looking inside the loop for the complexity of the interior operation, which is a constant operation with O(1) complexity.  However, when considering the math that is going on, we are evaluating essentially the case of adding the square of an inputted number to zero until that increasing number is greater than the cube of the inputted number.  By my estimations, this should take approximately two runs of the while loop to complete the case, with any value of n > 1.  The runtime complexity of the code snippet is O(1), as the runtime does not substantively change with an increase in n.


b) As we have a nested while loop inside the for loop, we burrow down to our deepest loop and begin to analyze the complexity.  We are increasing our counter by 1 which is a constant runtime, then multiplying j by two then saving that value to j, another constant operation, while j is less than n.  Since J is starting from 1, as n increases, it would take a longer time to reach the number.  But as J is doubling in value each time, it will take less steps to reach higher numbers and higher numbers (exponential/logarithmic relationship).  As it will take little time to reach the large numbers, we can expect log(n) complexity from the nested while loop.  For i in range(n) means we will be running the nested loop n times, so overall for this function the complexity would be the products of the complexities of the nested while and for loop, meaning the overall complexity of the function is O(n*log(n)).


c) The recursive function bunnyEars, as bunnies increases, will run with runtime complexity O(n), because the function will be called once per bunny entered, or once for every n, so the runtime complexity is linear, O(n).

## Exercise II

So, as the floors are in order, a 'binary search' solution would be theoretically the best for fewest eggs dropped. Split in half the height of the building (n//2) and set f to this. The first egg-drop floor is the middle floor of the building.
    If the egg drops, and breaks, go to the middle floor between the current floor and the ground, and repeat the drop. Until you have found the break point of where the egg breaks/doesn't break (within one floor precision)
    If the egg drops from f and does not break, go to the middle floor between the current floor and the top floor and repeat the drop (within one floor precision).
The runtime complexity of this search will be O(log(n)), as we will not need to drop eggs off each floor, but as the building's height increases, it will take more eggs to drop to find the exact point where the egg does/does not break.  