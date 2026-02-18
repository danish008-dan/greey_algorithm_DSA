"""
Purpose:
--------
Schedule jobs to maximize profit.

Each job has:
- deadline
- profit

Greedy Strategy:
---------------
Sort jobs by descending profit.
Try to schedule each job in latest available slot.
"""

def job_sequencing(jobs):
    # jobs = [(id, deadline, profit)]
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * (max_deadline + 1)

    total_profit = 0

    for job_id, deadline, profit in jobs:
        for slot in range(deadline, 0, -1):
            if slots[slot] == -1:
                slots[slot] = job_id
                total_profit += profit
                break

    return total_profit, slots


# Example
jobs = [
    (1, 2, 100),
    (2, 1, 19),
    (3, 2, 27),
    (4, 1, 25),
    (5, 3, 15)
]

print(job_sequencing(jobs))
