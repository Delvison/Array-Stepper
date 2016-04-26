# Array Stepper #

Construct an algorithm to traverse an array of integers in the shortest number
of steps starting at index 0. The integer contained in the current index
indicates the amount of steps available to be take. At any point, the algorithm
can step forward an amount of indices that is no greater than the integer value
contained in the current index. During each step, the algorithm should print how
many steps it has taken. The algorithm is considered done/succesful when you can
legally step beyond the last array element. Once completed, the algorithm should
print the term 'out'.

In addition, this program should accept a text file from standard in(command
line). This text file will be populated with one integer on every line. The
program should parse this text file and construct an array out of the integers
to be fed into the algorithm. An error message should be printed in the absence
of a textfile given as input via standard in.

There are no restrictions and any language of choice may be used.

# Example #

Given the following sequence of integers [ints.txt](download):

		5 6 0 4 2 4 1 0 0 4

The program should output:

		0, 5, 9, out.

## Explanation ##
Since the algorithm starts at the 0th index, the first value printed is 0 since
0 steps have been taken. The integer value contained here is 5 indicating that
the algorithm can step forward 5 steps. The algorithm sees that the 5th index
contains the most optimal value and chooses to step forward 5 spaces. 5 is then
printed out indicating that the algorithm has taken 5 total steps. The integer
value contained at the 5th index is 4 indicating that the algorithm can step
forward upto 4 spots. The algorithm sees that the value at the 9th index would
be most optimal and chooses to step forward to it. 9 is printed out to indicate
that the algorithm has taken a total of 9 steps. Since the value contained at
index 9 allows the algorithm to step an amount the exceeds the end of the array,
it simply prints 'out' indicating that it has completed its traversal.
