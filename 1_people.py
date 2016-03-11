# let's explore inheritance and polymorphism

class Person:

  def __init__(self, name, hometown):
    self.name = name
    self.hometown = hometown

  def introduce(self):
    print("Hi, I'm "+self.name+". I'm from",self.hometown+'.')

  def meet(self, another):
    # class Employee
    self.introduce()
    # class Person
    another.introduce()


# This line makes Employee a child of Person
# The new __init__ overrules the old one.
# if no new __init__, defaults to old one
class Employee(Person):

  # def __init__(self, name, hometown):
  #   self.name = name
  #   self.hometown = hometown
  
  # you can overwrite functions too!
  def introduce(self):
    print("Yo!")

  def department(self):
    return "Software Consulting"

def greet_everyone(person1, person2):
  person1.introduce()
  person2.introduce()


me = Employee("Lakshman", "Bethesda")
# print(me.department())

friend = Person("Jeff", "Skokie")

me.meet(friend)
# Hi, I'm <your name>.  I'm from <your hometown>.
# Hi, I'm Jeff.  I'm from Skokie.
