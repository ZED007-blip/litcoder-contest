import sys
import heapq

def last_stone_weight(stones):
    # Convert stones to a max heap
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)

    # Perform the operation until only one stone is left
    while len(max_heap) > 1:
        # Get the two heaviest stones
        stone1 = -heapq.heappop(max_heap)
        stone2 = -heapq.heappop(max_heap)

        # Calculate the new stone weight and push it back to the heap
        new_stone = abs(stone1 - stone2)
        heapq.heappush(max_heap, -new_stone)

    # Return the remaining stone weight (or 0 if no stones are left)
    return -max_heap[0] if max_heap else 0

# User input for stones
stones_input = input("Enter the list of stones separated by spaces: ")
stones = list(map(int, stones_input.split()))

# Calculate and print the result
result = last_stone_weight(stones)
print("Output:", result)

                                                                                                                            
