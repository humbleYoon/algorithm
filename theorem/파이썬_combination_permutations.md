# Python combination vs permutations

```python
items = ['1', '2', '3', '4', '5']

from itertools import permutations
list(permutations(items, 2))
# [('1', '2'), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]

from itertools import combinations
list(combinations(items, 2))
# [('1', '2'), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
```

```python
import itertools

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
m = int(input())
info_list = list(itertools.combinations(nums, m))
```

