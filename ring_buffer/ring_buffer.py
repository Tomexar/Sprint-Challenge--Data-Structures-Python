class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item

    if self.current == len(self.storage) - 1:
      self.current = 0
    else:
      self.current += 1  

  def get(self):
    temp = []
    for i in range(len(self.storage)):
      if self.storage[i] != None:
        temp.append(self.storage[i])
    return temp