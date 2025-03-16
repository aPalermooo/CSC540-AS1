Files are organized by Problem number and contain the problem writen in the Prompt.txt located witin
the directory.

The main solution for the problems are as followed:
Problem 1: Simulation.py
Problem 2: PlayAgainstComputer.py
Problem 3: HillClimber.py (part 1 and part 2)

Answer to Problem 1 part 3:
3. Is it a good idea to check for repeated states? (2 points)

It is not advisable to check for repeated states since these states are already computed in
another location within the state tree.

This can also prove that the paths that are generated off of this revisited state cannot be optimal.
This is because since the tree is generated top to bottom, if we encounter a revisited state, it will be
deeper in the tree with a higher cost to get to the same state. These nodes in the tree are not worth exploring if you are only
looking to find the optimal solution

In summary, it would be a waste to redo the calculations that are already done.
The solution I had to make sure that I do not recalculate already visited states was to use a hashmap of visited states, so that I know that 
if the encoding of the state I just generated is in the hashmap, I know that the subsequent actions that can performed off of that state are already in the tree