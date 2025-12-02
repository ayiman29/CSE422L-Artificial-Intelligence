# CSE422L Artificial Intelligence

## Labs

- [**LAB 1: A\* Algorithm**](https://github.com/ayiman29/CSE422L-Artificial-Intelligence/tree/main/LAB%201)  
- [**LAB 2: Genetic Algorithm**](https://github.com/ayiman29/CSE422L-Artificial-Intelligence/tree/main/LAB%202)  
- [**LAB 3: Minimax Algorithm**](https://github.com/ayiman29/CSE422L-Artificial-Intelligence/tree/main/LAB%203)


## Analysis of Iterations vs Fitness in LAB2 Genetic Algorithm

An important experiment conducted in [LAB2](https://github.com/ayiman29/CSE422L-Artificial-Intelligence/blob/main/LAB%202/a1_iterationVSfitness.py) where a graph is plotted of the number of iteration against the fitness value. It shows how this algorithm functions and it's probabilistic characteristics.

### Experimental Setup

- **Population and Fitness:** The GA has a fixed-size population representing possible placements for processor components, where fitness is based on minimizing wire distance, overlap, and area.
- **Fitness:** In this context, higher fitness values (less negative) indicate better solutions.
- **Iterations Tested:** The GA was run for increasing numbers of iterations (from 10 up to 500, in steps), each time selecting the best chromosome's fitness.
- **Visualization:** The results were plotted to show the best fitness value versus the number of iterations. See the figure below.

### Observations


<img width="1360" height="726" alt="image" src="https://github.com/user-attachments/assets/a7cb3fbf-4ea6-4a9e-9909-3d5baf0bce86" />


- **General Trend:** The graph is has an upward trend, however there is a lot of flactuation showing a pattern of inconsistency.
- **Fluctuations:** Despite the gradual improvement, there are noticeable fluctuations in fitness. This is typical of stochastic algorithms like GA, where random events such as mutation and crossover can occasionally lead to worse solutions for some generations, before improvements are rediscovered in later iterations. The genetic algorithm does not always guarantee monotonic improvement.
- **Takeaway:** Increasing the number of iterations generally increases the chance of finding a better fitted solution, however given it's probabilistic nature, crossovers and mutations don't **ALWAYS** ensure a better solution.
### Conclusion

idk what to write here
