def calculate_unique_shapes(n):
    if n <= 0:
        return 0

    # Create a memoization table to store the number of unique shapes
    memo = [0] * (n + 1)

    # Base cases
    memo[0] = 0
    memo[1] = 1

    for i in range(2, n + 1):
        # Initialize the total number of unique shapes for i cubes
        total_shapes = 0

        # Consider all possible rotations and orientations for i cubes
        for j in range(1, i + 1):
            # Calculate the number of unique shapes by connecting the jth cube
            # to the remaining (i - j) cubes
            shapes_with_j = memo[j] * calculate_unique_shapes(i - j)

            # Add the number of unique shapes to the total count
            total_shapes += shapes_with_j

        # Store the result in the memoization table
        memo[i] = total_shapes

    return memo[n]

# Example usage
n = 20


unique_shapes = calculate_unique_shapes(n)
print(f"The number of unique shapes with {n} cubes is: {unique_shapes}")
