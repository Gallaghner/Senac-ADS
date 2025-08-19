

//1)
// import java.util.Scanner;

// public class Lista1 {
//     public static void main(String[] args){
//         //cria o objeto Scanner pra ler a entrada do teclado
//         Scanner sc = new Scanner(System.in);

//         //Pede e le o primeiro número
//         System.out.print("Digite o primeiro numero inteiro: ");        
//         int n1 = sc.nextInt();

//         //Pede e le o segundo numero
//         System.out.print("Digite o segundo numero inteiro: ");
//         int n2 = sc.nextInt();

//         //Pede e le o numero real
//         System.out.print("Digite um numero real: ");
//         double n3 = sc.nextDouble();

//         //calculando os resultados
//         double produto = n1 * (n2 / 2.0);
//         double soma = (3 * n1) + n3;
//         double cubo = Math.pow(n3, 3);

//         //Mostrando os resultados
//         System.out.printf("O produto do primeiro com a metade do segundo: %.2f\n", produto);
//         System.out.printf("A soma do terceiro com o triplo do primeiro: %.2f\n", soma);
//         System.out.printf("O teceiro numero ao cubo: %.2f\n", cubo);

//         //fecha o scanner
//         sc.close();
//     }
// }


//2)
// import java.util.Scanner;

// public class Lista1 {
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);

//         System.out.print("Digite o primeiro número: ");
//         int n = sc.nextInt();

//         if (n > 10){
//             System.out.print("É maior que 10");
//         }
//         else if (n == 10){
//             System.out.print("É igual a 10");
//         }
//         else{
//             System.out.print("É menor que 10");
//         }
//         sc.close();
//     }

// }

//3
// import java.util.Scanner;

// public class Lista1 {
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
        
//         //recebe os dois números
//         System.out.print("Digite o primeiro número: ");
//         int n1 = sc.nextInt();
//         System.out.print("Digite o segundo número: ");
//         int n2 = sc.nextInt();
        
//         if(n1 > n2){
//             System.out.printf("O número %d é maior que o número %d", n1, n2);
//         }
//         else if(n1 < n2){
//             System.out.printf("O número %d é menor que o número %d", n1, n2);
//         }
//         else{
//             System.out.printf("O numero %d é igual a %d", n1, n2);
//         } 
//         sc.close();
//     }

// }

//4)
// import java.util.Scanner;

// public class Lista1 {
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);

//         //recebe os 3 números
//         System.out.println("Digite o primeiro número: ");
//         int n1 = sc.nextInt();
//         System.out.println("Digite o segundo número: ");
//         int n2 = sc.nextInt();
//         System.out.println("Digite o terceiro número: ");
//         int n3 = sc.nextInt();

//         //verifica se os numeros estao ou não em ordem crescente
//         if (n1 < n2 && n2 < n3) {
//             System.out.println("Os numeros estão em ordem crescente.");
//         } else {
//             System.out.println("Os números não estão em ordem crescente.");
//         }
//         sc.close();
//     }
// }

//5)
// import java.util.Scanner;

// public class Lista1 {
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
            
//             //recebe o input do usuário
//             System.out.println("Digite o sexo F/M: ");
//             char sexo = sc.next().charAt(0);

//             //verifica se o input é F ou M
//             if (sexo == 'F' || sexo == 'f') {
//                 System.out.println("Sexo feminio.");
//             } else if (sexo == 'M' || sexo == 'm') {
//                 System.out.println("Sexo masculino.");
//             } else {
//                 System.out.println("Sexo invalido.");
//             }
            
//         sc.close();
//     }
// }


//6)
// import java.util.Scanner;
// public class Lista1 {
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
//             //pergunta o turno que estuda
//             System.out.println("Em que turno voce estuda? (Digite Apenas M - Matutino, V - Vespertino, N - Noturno)");
//             //tranforma o input do usuario em minusculo e adiciona o valor na variavel turno
//             char turno = Character.toLowerCase(sc.next().charAt(0));

//             //verifica se o input é Matutino, Verpertino ou Noturno
//             if (turno == 'm'){
//                 System.out.println("Turno Matutino.");
//             } else if (turno == 'v') {
//                 System.out.println("Turno Vespertino.");
//             } else if (turno == 'n'){
//                 System.out.println("Turno Noturno.");
//             } else  {
//                 System.out.println("Tuno inválido.");
//             }
//         sc.close();
//     }
// }

//7)
// import java.util.Scanner;
// public class Lista1 {
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
//         //recebe o valor de compra da roupa
//         System.out.println("Digite o valor de compra da roupa: ");
//         double v = sc.nextDouble();
        
//         //verifica se o valor de compra é maior ou menor que 50
//         if (v == 50 || v > 50) {
//             v = v + (v * 0.3);
//             System.out.println("O valor de venda da peça deve ser igual a R$"+ v);
//         } else if ( v < 50 || v > 0){
//             v = v + (v * 0.45);
//             System.out.println("O Valor de venda da peça deve sr igual a R$"+ v);
//         }
//         sc.close();
//     }                
// }

// //8)
// import java.util.Scanner;
// public class Lista1 {
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
//         //recebe o input do usuário
//         System.out.println("Digite o numero: ");
//         double n = sc.nextDouble();

//         //verifica se o numero de input é maior que 0 
//         if (n > 0) {
            
//             double r = Math.sqrt(n);
//             System.out.printf("A raiz quadrada do número %.2f é %.2f", n, r);
//         } else {
//             System.out.println("Número inválido");
//         }
//         sc.close();
//     }
// }

//9)
// import java.util.Scanner;
// public class Lista1 {
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
//         //recebe os números do usuário
//         System.out.println("Digite o primeiro número: ");
//         double n1 = sc.nextDouble();
//         System.out.println("Digite o segundo número: ");
//         double n2 = sc.nextDouble();

//         //inverte os valores usando uma terceira variável (x) como auxiliar para aramzaenar o valor de n1 antes dele ser transformado em n2
//         double x = n1;
//         n1 = n2;
//         n2 = x;

//         System.out.printf("OS números invertidos são %.2f e %.2f" ,n1, n2);
//         sc.close();
//     }
// }

//10)
// import java.util.Scanner;
// public class Lista1 { 
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
//         //recebe o input do usuário
//         System.out.println("Digite um número inteiro: ");
//         int n = sc.nextInt();

//         if (n > 0) {
            
//             double q = Math.pow(n, 2);
//             double r = Math.sqrt(n);
//             System.out.printf("%d elevado ao quadrado é igual a %.1f e a raiz de %d é igual a %.1f", n, q, n, r);
//         }else {
//             System.out.println("Por favor, digite um número inteiro positivo!");
//         }
//         sc.close();
//     }
// }

//11)
// import java.util.Scanner;
// public class Lista1 {
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
//         //recebe o numero inteiro do usuario
//         System.out.println("Digite um número inteiro: ");
//         int n = sc.nextInt();
        
//         //verifica se é par ou impar
//         if (n % 2 == 0) {
//             System.out.println("O número é par.");
//         } else if (n % 2 == 1) {
//             System.out.println("O número é ímpar.");
//         }
//         sc.close();
//     }
// }

//12)
// import java.util.Scanner;
// public class Lista1{
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
//         //recebe os inputs do usuario
//         System.out.println("Digite o primeiro número inteiro: ");
//         int n1 = sc.nextInt();
//         System.out.println("Digite o segundo número: ");
//         int n2 = sc.nextInt();

//         //verifica e mostra qual número é maior do que o outro e a diferenca entre eles atrelada a r
//         if (n1 > n2) {
//             int r = n1 - n2;
//             System.out.printf("%d é maior do que %d e a diferença entre eles é de %d.", n1,n2,r);
//         } else if (n2 > n1){
//             int r = n2 - n1;
//             System.out.printf("%d é maior do que %d e a diferença entre eles é de %d.", n2,n1,r);
//         } else if (n1 == n2){
//             System.out.println("Digite números diferentes.");
//         } else {
//             System.out.println("Digite números válidos e inteiros.");
//         }
//         sc.close();
//     }
// }

//13
// import java.util.Scanner;
// public class Lista1{
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
//         //recebe os inputs do usuario
//         System.out.println("Digite o primeiro número inteiro: ");
//         int n1 = sc.nextInt();
//         System.out.println("Digite o segundo número: ");
//         int n2 = sc.nextInt();

//         //verifica e mostra qual número é maior do que o outro e a diferenca entre eles atrelada a r
//         if (n1 > n2) {
//             System.out.printf("%d é maior do que %d.", n1,n2);
//         } else if (n2 > n1){
//             System.out.printf("%d é maior do que %d.", n2,n1);
//         } else if (n1 == n2){
//             System.out.println("Números iguais.");
//         } else {
//             System.out.println("Digite números válidos e inteiros.");
//         }
//         sc.close();
//     }
// }

//14)
// import java.util.Scanner;
// public class Lista1{
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
//         //recebe as notas do usuário
//         System.out.println("Digite a primeira nota: ");
//         double n1 = sc.nextDouble();
//         System.out.println("Digite a segunda nota: ");
//         double n2 = sc.nextDouble();

//         if (n1 >= 0 && n1 <=10 || n2 >= 0 && n2 <= 10) {
//             double m = (n1 + n2) / 2;
//             System.out.printf("A média das notas é igual a %.1f.", m);
//         } else {
//             System.out.println("Digite notas válidas.");
//         }
//         sc.close();
//     }
// }

//15
// import java.util.Scanner;
// public class Lista1{
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
//         //recebe o número de horas trabalhadas
//         System.out.println("Digite o número de horas trabalhadas: ");
//         double h = sc.nextDouble();
//         //calculo do salário bruto
//         double sb = h * 40.5;

//         //verifica se o salario bruto é maior do que 2500, se for, aplica um desconto de 11%
//         if (sb > 2500){
//             double sf = sb - (sb * 0.11);
//             System.out.printf("O salário bruto é igual R$%.2f. Aplicando o desconto de 11 porcento o salário líquido fica igual a R$%.2f.", sb, sf);
//         } else {

//             System.out.println("O salário líquido é igual a R$"+sb);
//         }
//         sc.close();
//     }
// }

//16)
import java.util.Scanner;
public class Lista1{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        //recebe o salario e o valor do emprestimo solicitado
        System.out.println("Digite o seu salário: ");
        double s = sc.nextDouble();
        System.out.println("Digite o valor do emprestimo: ");
        double e = sc.nextDouble();
        //define quanto é 20% do salário
        double p = s*0.2;

        if(e > p){
            System.out.println("Empréstimo não concedido.");
        } else {
            System.out.println("Empréstimo concedido");
        }
        sc.close();
    }
}

