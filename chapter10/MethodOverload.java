public class MethodOverload
{
    void method()
    {
        System.out.println("version 1");
    }
    void method(int a)
    {
        System.out.println("version int");
    }
    void method(char a)
    {
        System.out.println("version char");
    }
    public static void main(String[]args)
    {
        MethodOverload m = new MethodOverload();
        m.method();
        m.method(12);
        m.method('A');
    }
}