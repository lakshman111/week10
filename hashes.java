import java.util.*;

class Person {
    public String name;

    Person() {
        name = "Jeff";
    }

    public void displayMoney() {
        Hashtable balances = new Hashtable();
        balances.put("checking", 125.0);
        System.out.println(balances.get("checking"));
    }
}


class Main {
  public static void main(String[] args) {
    Person p = new Person();
    System.out.println(p.name);
    p.displayMoney();
  }
}
