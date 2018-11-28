# Simulated_Annealing-
Simulated Annealing Script for quadratic assigment problem
This is the smallest of the QAP test problems of Nugent et al. Five departments are to
be placed in five locations with two in the top row and three in the bottom row.
1 2
3 4 5
The objective is to minimize costs between the placed departments. The cost is (flow*rectilinear
distance), where both flow and distance are symmetric between any given pair of departments.
Below is the flow and distance matrix where distance is the upper half. The optimal solution is 25
(or 50 if you double the flows).
Dept 1 2 3 4 5
1 - 1 1 2 3
2 5 - 2 1 2
3 2 3 - 1 2
4 4 0 0 - 1
5 1 2 0 5 -
