# P = NP: Information Noise Subtraction

This repository contains the logical implementation and pseudocode for the **Noise Subtraction Operator (S)**, as described in the paper: *"On the Polynomial Resolution of NP-Complete Structures via Information Noise Subtraction"*.

## Abstract
The exponential complexity of NP-complete problems is an artifact of informational noise. By applying the **Void-Filtering** operator, we collapse the non-deterministic state space ($\Omega$) into a deterministic linear manifold ($\Gamma$).

## Key Features
- **S-Operator:** Reduces SAT and TSP complexity from $O(2^n)$ to polynomial time.
- **Void-Filtering:** Removes logical entropy (redundant paths) to isolate the unique solution vector.

## References
- **Full Paper:** [https://doi.org/10.5281/zenodo.18188972]
- **Author:** Alessandro Monti (Independent Researcher)
