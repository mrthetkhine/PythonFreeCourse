abstract class Gateway
{
    abstract void paymentProcess();
}
class KBZGateway extends Gateway
{
    void paymentProcess()
    {
        System.out.println("KBZ Payment");
    }
}
class YomaGateway extends Gateway
{
    void paymentProcess()
    {
        System.out.println("Yoma Payment");
    }
}
public class AbstractDemo
{
    public static void main(String[]args)
    {
        Gateway g = new KBZGateway();
        g.paymentProcess();
    }
}