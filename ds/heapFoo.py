import heapq

data = [6, 5, 4, 3, 2, 1]
heap = []

# print(data)
# for n in data:
#     heapq.heappush(heap, n)
#     print(heap)
#
print(data)
heapq.heapify(data)
print(data)
print()

# for n in range(2):
#     heapq.heappop(data)
#     print(data)
# print()
#
# for n in range(6):
#     heapq.heapreplace(data, n)
#     print(data)

print(heapq.nlargest(2, data))
print(heapq.nsmallest(2, data))
print(sorted(data))
print(list(reversed(sorted(data))))
