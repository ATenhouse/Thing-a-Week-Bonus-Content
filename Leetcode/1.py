# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2


def two_sum(nums, target):
    lookup = dict(((v, i) for i, v in enumerate(nums)))
    return next(((i + 1, lookup.get(target - v) + 1)
                 for i, v in enumerate(nums)
                 if lookup.get(target - v, i) != i), None)

print two_sum([2, 7, 11, 15], 9)
