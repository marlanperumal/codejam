# Pancake flippling theory
# - The order in which you make flips does not matter
# - Doing the same flip twice is the same as not making the flip at all
# - We can then apply a greedy algorithm
#   - work from left to right
#   - if the leftmost pancake is on the wrong side make the flip
#   - if you get to the end and all the pancakes are not right then impossible

# Get in the total number of cases in the file
T = int(input())

# Loop through each of the cases
# Using range(1, T+1) instead of range(T) to output case numbers starting at 1
for t in range(1, T+1):
    # Read in the case numbers, split by whitespace - k needs to be an int
    s, k = read_str().split()
    k = int(k)

    # Convert the pancake string to a list of bools
    # Strings are immutable and bools are easier to work with
    sb = [si == "+" for si in s]

    # Initialise the counter of flips
    f = 0

    # Test each pancake going from left to right
    # We can only get up to the flipper length from the end (k-1)
    for i in range(len(sb) - k + 1):
        # If that pancake is not in the correct position
        if not sb[i]:
            # Increment the flip counter
            f += 1
            # Flip all the pancakes covered by the flipper
            sb[i:i+k] = [not b for b in sb[i:i+k]]

    # Check if all of the pancakes are on the correct side
    ans = f if all(sb) else "IMPOSSIBLE"
    # Output the case result
    print("Case #{}: {}".format(t, ans))
