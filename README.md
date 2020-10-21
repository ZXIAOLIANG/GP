# Genetic Programming
Genetic Programming is implemented to solve 6-mux, 11-mux and 16-middle-3 problems

## 6-mux
The population size I used is 500, and the maximum iteration is 1000, and the termination
criteria is when the maximum iteration is reached. For crossover/mutation probability I used
0.95, so there is 95% chance to crossover and 5% chance to mutate.


For the offspring selection, 10% of the offspring is directly selected from the previous
population using tournament selection (randomly sample without replacement 7 candidate
from the whole population and select the one with highest fitness).


The maximum tree depth I used is 4 (start from 0). Ideally, the program can accomplish 100%
fitness value with a tree of depth 2, but to provide more variation to the population to
recombine or mutate, I choose the maximum depth to be 4.


In terms of fitness evaluation of each program, I used the full test set (64 tests).
The final program I got and the fitness progress plot are shown below, it is able to achieve 100%
fitness.

```bash
((IF ((IF a1 THEN d3 ELSE d2) AND (a0 OR a1)) THEN (NOT (NOT a0)) ELSE
((IF a1 THEN d3 ELSE d0) AND (NOT a0))) OR ((IF (d1 AND a0) THEN (d3
OR a0) ELSE d1) AND (IF (a1 OR a0) THEN (NOT a0) ELSE (a0 AND a1))))
```

## 11-mux
The population size I used is 200 (so that the running time is not too long), and the maximum
iteration is 1000, and the termination criteria is when the maximum iteration is reached. For
crossover/mutation probability I used 0.95, so there is 95% chance to crossover and 5% chance
to mutate.


For the offspring selection, 10% of the offspring is directly selected from the previous
population using tournament selection (randomly sample without replacement 7 candidate
from the whole population and select the one with highest fitness).


The maximum tree depth I used is 6 (start from 0). Ideally, the program can accomplish 100%
fitness value with a tree of depth 3, but to provide more variation to the population to
recombine or mutate, I choose the maximum depth to be 6.


In terms of fitness evaluation of each program, I used the full test set (2048 tests).
The final program I got and the fitness progress plot are shown below, it is able to achieve
84.375% fitness.

```bash
(((IF (NOT ((a2 OR a0) OR (a0 OR a0))) THEN ((NOT (NOT d2)) AND ((a1
OR a0) OR (NOT d2))) ELSE (IF (NOT (NOT a2)) THEN ((a2 OR a0) OR (a2
OR a0)) ELSE ((a0 OR a0) OR (a0 OR a2)))) AND (IF (NOT ((d3 AND a1) OR
(NOT a2))) THEN (NOT (IF (a0 OR a0) THEN (NOT d5) ELSE (a2 OR a0)))
ELSE (NOT (NOT (IF a1 THEN a1 ELSE d4))))) OR (NOT ((((a0 OR a2) AND
(NOT d1)) AND (IF (a0 OR d1) THEN (NOT d5) ELSE (a2 OR a2))) OR (((a0
OR a0) OR (a1 OR a0)) OR (NOT (IF a1 THEN a2 ELSE d0))))))
```

## 16-middle-3
The population size I used is 100 (so that the running time is not too long), and the maximum
iteration is 500, and the termination criteria is when the maximum iteration is reached. For
crossover/mutation probability I used 0.95, so there is 95% chance to crossover and 5% chance
to mutate.


For the offspring selection, 10% of the offspring is directly selected from the previous
population using tournament selection (randomly sample without replacement 7 candidate
from the whole population and select the one with highest fitness).


The maximum tree depth I used is 8 (start from 0). I think 8 shall be sufficiently deep generate a
good solution.


In terms of fitness evaluation of each program, I sampled without replacement 1000 tests from
the full test set (65536 tests), so that the running time is not too long. However, the sampling
introduces some bias, which cause some fluctuation in the fitness progress plot.


The final program I got and the fitness progress plot are shown below, it is able to achieve
around 64% fitness.

```bash
(NOT (NOT (IF (NOT ((IF ((x1 OR x11) AND (x1 OR x5)) THEN ((x11 OR
x16) OR (IF x3 THEN x13 ELSE x16)) ELSE ((x9 OR x16) OR (x1 OR x1)))
AND (((x14 OR x11) OR x5) AND ((x4 OR x4) OR (IF x13 THEN x13 ELSE
x15))))) THEN (NOT (((NOT (IF x10 THEN x10 ELSE x6)) AND (NOT (x4 OR
x4))) OR (NOT ((x15 OR x1) OR (x14 AND x3))))) ELSE (NOT (((IF (IF x3
THEN x12 ELSE x15) THEN (x12 OR x14) ELSE x5) AND ((x10 OR x6) OR (x4
OR x4))) AND (IF ((x14 AND x3) AND (x1 OR x11)) THEN (IF (NOT x6) THEN
(x15 OR x16) ELSE (x16 OR x1)) ELSE ((x10 AND x6) AND (IF x15 THEN x6
ELSE x1))))))))
```
