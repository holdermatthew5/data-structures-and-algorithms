def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  else:
    pivot = arr.pop()
    less = []
    more = []
    for i in arr:
      if i <= pivot:
        less.append(i)
      else:
        more.append(i)
    less = quick_sort(less)
    more = quick_sort(more)
    return less + [pivot] + more