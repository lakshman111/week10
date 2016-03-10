# let's explore inheritance and polymorphism

class Person:

  def __init__(self, name, hometown):
    pass

  def introduce(self):
    pass

  def meet(self, another):
    self.introduce()
    another.introduce()


me = Person("<your name>", "<your hometown>")
friend = Person("Jeff", "Skokie")

me.meet(friend)
# Hi, I'm <your name>.  I'm from <your hometown>.
# Hi, I'm Jeff.  I'm from Skokie.
