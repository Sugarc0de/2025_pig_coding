#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
from collections import deque

#
# Complete the 'minimumAverage' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY customers as parameter.
#

"""
h = heap()
h.insert((x))

"""

# Idea: store all your available customers for your next cooking decision.
# time sorted, [2, 3, ]


def minimumAverage(customers):
    # sort by arrival time
    num_customers = len(customers)
    customers = deque(sorted(customers))
    end_cook_time = 0
    total_waited_time = 0

    # min-heap by cooking time
    waiting = []

    while len(customers) > 0 or len(waiting) > 0:
        # Case 1: if already cooking, all customers with arrival time <= end cook time are pushed
        if len(waiting) > 0 and (
            len(customers) > 0 and customers[0][0] <= end_cook_time
        ):
            arrival_time, cook_time = customers.popleft()
            heapq.heappush(
                waiting, (cook_time, arrival_time)
            )  # heap use the first item to sort, second item is our arrival time
            # print("case 1 push", arrival_time, cook_time)

        # Case 2: already cooking and no more customers to push, then pop from heap
        elif len(waiting) > 0:
            cook_time, arrival_time = heapq.heappop(waiting)
            end_cook_time = max(arrival_time, end_cook_time) + cook_time
            total_waited_time += end_cook_time - arrival_time
            # print("case 2 pop", arrival_time, end_cook_time)

        # Case 3: nothing cooking, then push next customer
        else:
            arrival_time, cook_time = customers.popleft()
            heapq.heappush(waiting, (cook_time, arrival_time))
            # print("case 3 push", arrival_time, cook_time)

    return int(total_waited_time / num_customers)


# (time arrive, time to cook)
customers = [(1, 3), (100, 9)]
# customers = [(0, 3), (1, 9), (2, 6)]
print(minimumAverage(customers))
