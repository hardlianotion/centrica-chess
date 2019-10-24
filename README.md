## Centrica Chess Problem
This program calculates the number of ways a set of chess pieces can 
be placed on a board of a given size without threatening each other.  
The pieces can be any quantity of King, Queen, Rook, Bishop, Knight.

The code is a collection of functions and classes, without a command-line
tool to run them.  

But there are fast and slow test suites.  Run these using:
```
python3 ./test_chess.py <suite-name>
```
where `suite-name` is one of `fast, required, slow, all_tests`: 
* fast is a set of small regression-style tests used in construction and validation 
of the solution.
* required is a test case required by 
the exercise rubric, to calculate output for a 6x9 board, 2 kings, 
1 queen, 1 rook, 1 knight, 1 bishop (spoiler - output: 20136752 board configurations).
* slow is for slow-running regression tests.  Currently contains a brute force 8-queens
test case.
* all_tests - runs all of the above tests.

Pypy3 to run `required, slow, all_tests`, as these are all very slow.  
```
pypy3 ./test_chess.py <suite-name>
```
I have not run `slow` or `all_tests` in Python3.


## Implementation Remarks
chess.py contains a somewhat heavy OO solution.  

The solution is driven by the recursive function
```
no_coverage_impl(board, unfixed, fixed)
```
with inputs board (length x width), a list `unfixed` of chess pieces 
(types `King, Queen, Rook, Bishop, Knight`) that have not been placed yet, 
and a list of pieces `fixed` that have been placed - initially empty.

The work is unsatisfying in some respects:

* the `no_coverage_impl` interface is clumsy and largely responsible for the 
way in which the algorithm is implemented to count multiplicities.
* the solution explores the entire board for each piece placed.  For 
each piece type that appears more than once, we count the multiplicity,
then divide out repetitions.  Cutting out this repetition provides 
a significant optimization, which is out of scope for this exercise.
* chess piece types are implemented to move some complexity from the main 
thread.  Some of the method implementations are slightly odd and redundant.

Tests in `test_chess.py` are more regression than classic unit tests.  

Moderately size problems run very slowly.  On my 12" Macbook with 1.1 GHz 
Intel Core M processor and 8Gb RAM, the `required` test suite has a Pypy3 run
 of 170 s, and a Python 3 run of 3621 s.  

The `slow` test suite is essentially a brute-force calculation of 
8-queens problem.  This runs in 610 s when run with Pypy3.  I am scared 
to perform a Python 3 run on this.
