"""
Purpose:
--------
Select maximum number of non-overlapping activities.

Greedy Strategy:
---------------
Always pick the activity that finishes earliest.
"""

def activity_selection(activities):
    # Sort by finish time
    activities.sort(key=lambda x: x[1])

    selected = []
    last_finish = -1

    for start, finish in activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected


# Example
activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (8, 9)]
print(activity_selection(activities))
