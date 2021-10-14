interface Flyable
{
    public void fly();
}
class Bird implements Flyable
{
    public void fly()
    {
        System.out.println("Bird fly");
    }
}
class Aeroplane implements Flyable
{
    public void fly()
    {
        System.out.println("Aeroplane fly");
    }
}
public class FlyableDemo 
{
    public static void main(String[]args)
    {
        Flyable f = new Bird();
        f.fly();
        f = new Aeroplane();
        f.fly();
    }
}