# 파이썬 deque

```python
import collections

# deque 생성
d = collections.deque([10, 20, 30, 40, 50])

# 오른쪽에 추가
d.append(60)

# 왼쪽에 추가
d.appendleft(0)

# 입력값을 순환하면서 오른쪽에 추가
d.extend([70, 80])

# 입력값을 순환하면서 왼쪽에 추가
d.extendleft([-10, -20, -30])

# 값 삭제
d.remove(0)

# 오른쪽의 끝값 가져오면서 deque에서 제거
maxValue = d.pop()

# 왼쪽의 끝값 가져오면서 deque에서 제거
minValue = d.popleft()

# 값 회전(rotating) 
d = collections.deque(range(5)) # [0, 1, 2, 3, 4]

d.rotate(1) # [4, 0, 1, 2, 3]
d.rotate(1) # [3, 4, 0, 1, 2]
d.rotate(-1) # [4, 0, 1, 2, 3]
d.rotate(-1) # [0, 1, 2, 3, 4]
```

