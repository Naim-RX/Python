import numpy as np
#Random number generation is a technique used to create random numbers or arrays of random numbers. NumPy provides various functions to generate random numbers, including uniform and normal distributions, as well as random integers.
#Random numbers can be useful in various applications, such as simulations, statistical modeling, and data analysis. They can also be used for testing and debugging purposes, as well as for generating synthetic data for machine learning models.
#NumPy provides a random module that contains functions for generating random numbers. Some of the commonly used functions in the random module include:
#np.random.rand(): Generates random
#  numbers from a uniform distribution over [0, 1).

rng = np.random.default_rng() # Create a random number generator instance
random_numbers = rng.random((1, 5)) # Generate 5 random numbers from a uniform distribution over
print(random_numbers)
print(rng.integers(1,7,2))

np.random.seed(1) # Set the seed for reproducibility
print(np.random.uniform(0, 1, 5)) # Generate 5 random numbers from a uniform distribution over [0, 1)

fruit = ['apple', 'banana', 'cherry', 'date', 'elderberry']
random_fruit = rng.choice(fruit) # Randomly select 3 unique fruits from the list
print(random_fruit) # Output: Randomly selected fruit from the list