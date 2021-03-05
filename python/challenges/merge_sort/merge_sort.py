def merge_sort(li):
  """
    Sort a list by diving into 2 parts and iteratively merging the greater number of the 2 at index 0 for right and left into the result list.
  """
  n = len(li)//2
  right = li[0:n]
  left = li[n:]
  if len(left) > 1:
    print(1, left)
    left = merge_sort(left)
    print(2, left)
  if len(right) > 1:
    print(3, right)
    right = merge_sort(right)
    print(4, right)
  new = []
  lempty = False
  rempty = False
  while left[0] or right[0]:
    print('r', right, 'l', left)
    if right[0] >= left[0]:
      new.append(left[0])
      if len(left) == 1:
        lempty = True
      left.remove(left[0])
    elif right[0] <= left[0]:
      new.append(right[0])
      if len(right) == 1:
        rempty = True
      right.remove(right[0])
    if rempty == True:
      for i in left:
        new.append(i)
      return new
    elif lempty == True:
      for i in right:
        new.append(i)
      return new
  return new