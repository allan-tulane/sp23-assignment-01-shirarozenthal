"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    
    if x <= 1:
        return x
    
    else:
        (ra, rb) = (foo(x - 1), foo(x - 2))
        return ra + rb
    
   

def longest_run(mylist, key):
    count = 0
    maxCount = 1
    
    for i in range(len(mylist)):
        if (key == mylist[i]) & (mylist[i] == mylist[i-1)]:
            count += 1
            continue
        if count >= maxCount:
            maxCount = count
            count = 1
        else:
            continue
    return maxCount


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):

  if len(mylist) == 0:
    return Result(0, 0, 0, False)

  if len(mylist) == 1:
    if mylist[0] == key:
      return Result(1, 1, 1, True)
    else:
      return Result(0, 0, 0, False)

  l = longest_run_recursive(mylist[:len(mylist)//2], key)
  r = longest_run_recursive(mylist[len(mylist)//2:], key)
  
  if l.is_entire_range and r.is_entire_range:
    return Result(l.left_size + l.right_size, r.left_size + r.right_size, (l.longest_size + r.longest_size), True)

  elif l.is_entire_range:
    if (r.left_size + l.longest_size) <= l.longest_size:
      return Result(l.left_size + r.left_size, r.right_size,  l.longest_size, False)
    else:
      return Result(l.left_size + r.left_size, r.right_size, (r.left_size + l.longest_size), False)

  elif r.is_entire_range:
    if (l.right_size + r.longest_size) <= r.longest_size:
      return Result(l.left_size, r.right_size + l.right_size, r.longest_size, False)
    else:
      return Result(l.left_size, r.right_size + l.right_size, (l.right_size + r.longest_size), False)

  else:
    if (l.right_size + r.left_size) < r.longest_size:
      return Result(l.left_size, r.right_size, r.longest_size, False)
    elif (l.right_size + r.left_size) < l.longest_size:
      return Result(l.left_size, r.right_size, l.longest_size, False)
    else:
      return Result(l.left_size, r.right_size, (l.right_size + r.left_size), False)
                                 

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
                                 
def test_longest_run_recursive():
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12).longest_size == 3
