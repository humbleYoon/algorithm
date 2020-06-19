# heapq

- 데이터를 정렬된 상태로 저장하기 위해서 사용

- 이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조 제공

  ```python
  import heapq
  
  heap = []
  heapq.heappush(heap, 4)
  heapq.heappush(heap, 1)
  heapq.heappush(heap, 7)
  heapq.heappush(heap, 3)
  print(heap)
  # [1, 3, 7, 4]
  
  # 가장 작은 1이 인덱스 0에 위치하며, 인덱스 1(=k)에 위치한 3은 인덱스 3(=2k+1)에 위치한 4보다 크므로 힙의 공식을 만족합니다.
  # 내부적으로 이진 트리에 원소를 추가하는 heappush() 함수는 O(logN)의 시간복잡도를 가집니다
  
  print(heapq.heappop(heap))
  print(heap)
  # 1
  # [3, 4, 7]
  print(heapq.heappop(heap))
  print(heap)
  # 3
  # [4, 7]
  
  # 내부적으로 이진 트리로부터 원소를 삭제하는 heappop() 함수도 역시 O(logN)의 시간 복잡도를 가집니다.
  
  # 최소값을 삭제하지 않고 얻기
  print(heap[0])
  # 4
  
  # 기존 리스트를 힙으로 변환
  heap = [4, 1, 7, 3, 8, 5]
  heapq.heapify(heap)
  print(heap)
  # [1, 3, 5, 4, 8, 7]
  # O(N)
  
  # [응용]최대 힙
  nums = [4, 1, 7, 3, 8, 5]
  heap = []
  for num in nums:
      heapq.heappush(heap, (-num, num))
  
  while heap:
      print(heapq.heappop(heap)[1])
  # 8
  # 7
  # 5
  # 4
  # 3
  # 1
  
  # [응용]K번째 최소값/최대값
  def kth_smallest(nums, k):
      heap = []
      for num in nums:
          heapq.heappush(heap, num)
         
     	kth_min = None
      for _ in range(k):
          kth_min = heapq.heappop(heap)
      return kth_min
  
  print(kth_smallest([4, 1, 7, 3, 8, 5], 3))
  # 4
  
  # [응용]힙 정렬
  def heap_sort(nums):
      heap = []
      for num in nums:
          heapq.heappush(heap, num)
          
      sorted_nums = []
      while heap:
          sorted_nums.append(heapq.heappop(heap))
      return sorted_nums
  print(heap_sort([4, 1, 7, 3, 8, 5]))
  # [1, 3, 4, 5, 7, 8]
  ```

  