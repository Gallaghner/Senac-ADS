public class Funcoes2{
    public static void main(String[] args){

        hello();
        hello2("joao");
        hello3("jow",55);
        soma(2,5);
        imc(70,1.80);
    }

    public static void hello(){
        System.out.println("Hellooo!!");
    }

    public static void hello2(String nome){
        System.out.printf("\nHellooooooooooooooo %s", nome);
    }

    public static void hello3(String nome, int idade){
        System.out.printf("\nHelloooo %s voce tem %d anos",nome,idade);
    }

    public static int soma(int x, int y){
        int sum = x + y;
        return sum;
    }

    public static String myname(){
        return "Thiago";
    }
    public static double imc(double peso, double altura){
        double myimc = peso / (altura*altura);
        return myimc;
    }



}