class Student{
    String name;
    private int age;

    public Student(String name, int age)
    {
        this.name = name;
        this.age = age;
    }
    public void display()
    {
        System.out.println("Name "+this.name +" Age "+this.age);
    }
}
public class EncapsulationTest
{
    public static void main(String[]ars)
    {
        Student mgMg = new Student("Mg Mg",18);
        mgMg.age = 2000;
        mgMg.display();
    
    }
   
}