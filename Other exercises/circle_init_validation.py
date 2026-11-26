'''
Add code to the init method to check that the type of center 
is a Coordinate obj and the type of radius is an int. 
If either are not these types, raise a ValueError.

class Coordinate(object):

  def __init__(self, x, y):
    self.x = x
    self.y = y


class Circle(object):

  def __init__(self, center, radius):
    self.center = center
    self.radius = radius

'''

class Coordinate(object):

  def __init__(self, x, y):
    self.x = x
    self.y = y

class Circle(object):

  def __init__(self, center, radius):
    if type(center) != Coordinate or type(radius) != int:
      raise ValueError
    
    self.center = center
    self.radius = radius

c = Coordinate(2,2)
circle = Circle(c,2)