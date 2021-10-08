class Human
{
    private String name;

    public Human(String name)
    {
        this.name = name;
        //System.out.println("Human constructor");
    }
    public void work()
    {
        System.out.println("Human "+this.name+ " works");
    }
}
class Doctor extends  Human
{
    private String medicalField;

    public Doctor(String name, String medicalField)
    {
        super(name);
        this.medicalField = medicalField;
        //System.out.println("Doctor constructor");
    }
    public void work()
    {
        //
        System.out.println("Doctor work");
    }
}
class Teacher extends  Human
{
    private String school;

    public Teacher(String name, String school)
    {
        super(name);
        this.school = school;
        //System.out.println("Teacher constructor");
    }
    public void work()
    {
        //
        System.out.println("Teacher teach at "+this.school);
    }
}
class Robot
{
    public void work()
    {
        System.out.println("Robot work");
    }
}
public class Inheritance
{
    public static void main(String[]args)
    {
        Human h = new Doctor("Tint Swe","General");//Sub typing
        h.work();

        h = new Teacher("Daw Hla","UCSY");
        h.work();

        //h = new Robot();
    }
}