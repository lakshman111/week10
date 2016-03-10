class Person {

  public void introduce() {
    System.out.println("Hello");
  }

  public void meet(Person another) {
      this.introduce();
      another.introduce();
  }
}

class Employee extends Person {

  public void introduce() {
    System.out.println("Goodbye");
  }

}

class Main {
  public static void main(String[] args) {
    Person p = new Person();
    p.meet(new Employee());
  }
}
