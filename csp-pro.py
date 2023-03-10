#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools
#Domain
domain = {
    "Class 1": ["Professor A", "Professor C"],
    "Class 2": ["Professor A"],
    "Class 3": ["Professor B", "Professor C"],
    "Class 4": ["Professor B", "Professor C"],
    "Class 5": ["Professor A", "Professor B"],
}

# Variables
variables = list(domain.keys())

# Unary Constraints
unary_constraints = {
    "Class 1": [8, 9],
    "Class 2": [8.5, 9.5],
    "Class 3": [9, 10],
    "Class 4": [9, 10],
    "Class 5": [10.5, 11.5],
}

# Binary Constraints
binary_constraints = []

# Find all combinations of variables
combinations = list(itertools.combinations(variables, 2))

# Check binary constraints for each combination of variables
for combination in combinations:
    var1 = combination[0]
    var2 = combination[1]

    # Check if the classes overlap in time
    if (unary_constraints[var1][0] < unary_constraints[var2][1]) and (
        unary_constraints[var1][1] > unary_constraints[var2][0]
    ):
        binary_constraints.append((var1, var2))

# Function to check if the assignment is consistent with constraints
def is_consistent(assignment, variable, value):
    # Check if the value is in the domain of the variable
    if value not in domain[variable]:
        return False

    # Check unary constraints
    time = unary_constraints[variable]
    for var, val in assignment.items():
        if (
            (var != variable)
            and (time[0] < unary_constraints[var][1])
            and (time[1] > unary_constraints[var][0])
        ):
            if val == value:
                return False

    # Check binary constraints
    for (var1, var2) in binary_constraints:
        if (variable == var1) and (var2 in assignment) and (assignment[var2] == value):
            return False
        if (variable == var2) and (var1 in assignment) and (assignment[var1] == value):
            return False

    return True


# Backtracking function to find a solution
def backtracking(assignment, variables):
    # Check if all variables have been assigned
    if len(assignment) == len(variables):
        return assignment

    # Choose an unassigned variable
    var = [var for var in variables if var not in assignment][0]

    # Try each value in the domain
    for value in domain[var]:
        # Check if the assignment is consistent with constraints
        if is_consistent(assignment, var, value):
            assignment[var] = value
            result = backtracking(assignment, variables)
            if result is not None:
                return result
            del assignment[var]

    return None


# Call the backtracking function
result = backtracking({}, variables)

# Print the result
if result is not None:
    print("Solution:", result)
else:
    print("No solution found")


# In[ ]:




