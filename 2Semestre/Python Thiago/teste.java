import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class teste {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        exercicio1();
        exercicio2();
        exercicio3();
        exercicio4();
        exercicio5();
        exercicio6(sc);
        exercicio7(sc);
        exercicio8(sc);
        exercicio9(sc);
        exercicio10(sc);
        exercicio11();
        exercicio12(sc);
        exercicio13(sc);
        exercicio14(sc);
        exercicio15(sc);
        exercicio16(sc);
        exercicio17(sc);
        exercicio18(sc);
        exercicio19(sc);
        exercicio20(sc);
        exercicio21(sc);
        exercicio22(sc);
        exercicio23();
        exercicio24(sc);
        exercicio25(sc);
        exercicio26();
        exercicio27(sc);
        exercicio28();
        exercicio29(sc);
        exercicio30(sc);
        exercicio31(sc);
        exercicio32(sc);
        exercicio33(sc);
        exercicio34(sc);
        exercicio35(sc);
        exercicio36(sc);
        exercicio37(sc);
        exercicio38(sc);
        exercicio39();
        exercicio40(sc);
        exercicio41();
        exercicio42(sc);
        exercicio43(sc);
        exercicio44(sc);
        
        sc.close();
    }
    
    // Exercício 1: Contagem regressiva de 10 a 0
    public static void exercicio1() {
        System.out.println("=== Exercício 1 ===");
        int i = 10;
        while (i >= 0) {
            System.out.println(i);
            i--;
        }
        System.out.println("FIM!");
    }
    
    // Exercício 2: 5 primeiros números ímpares maiores que 0
    public static void exercicio2() {
        System.out.println("=== Exercício 2 ===");
        int contador = 0;
        int numero = 1;
        
        while (contador < 5) {
            if (numero % 2 != 0) {
                System.out.println(numero);
                contador++;
            }
            numero++;
        }
    }
    
    // Exercício 3: 10 primeiros números pares maiores que 0
    public static void exercicio3() {
        System.out.println("=== Exercício 3 ===");
        int contador = 0;
        int numero = 2;
        
        while (contador < 10) {
            if (numero % 2 == 0) {
                System.out.println(numero);
                contador++;
            }
            numero++;
        }
    }
    
    // Exercício 4: Números de 1 a 100 usando for e while
    public static void exercicio4() {
        System.out.println("=== Exercício 4 ===");
        System.out.println("Usando FOR:");
        for (int i = 1; i <= 100; i++) {
            System.out.print(i + " ");
        }
        
        System.out.println("\n\nUsando WHILE:");
        int i = 1;
        while (i <= 100) {
            System.out.print(i + " ");
            i++;
        }
        System.out.println();
    }
    
    // Exercício 5: Incrementar de 1000 em 1000 até 100000
    public static void exercicio5() {
        System.out.println("=== Exercício 5 ===");
        int numero = 0;
        while (numero <= 100000) {
            System.out.println(numero);
            numero += 1000;
        }
    }
    
    // Exercício 6: Somar 10 valores digitados pelo usuário
    public static void exercicio6(Scanner sc) {
        System.out.println("=== Exercício 6 ===");
        int soma = 0;
        
        for (int i = 1; i <= 10; i++) {
            System.out.print("Digite o " + i + "° valor: ");
            int valor = sc.nextInt();
            soma += valor;
        }
        
        System.out.println("Soma dos valores: " + soma);
    }
    
    // Exercício 7: Ler 10 inteiros e calcular média
    public static void exercicio7(Scanner sc) {
        System.out.println("=== Exercício 7 ===");
        int soma = 0;
        
        for (int i = 1; i <= 10; i++) {
            System.out.print("Digite o " + i + "° número: ");
            int numero = sc.nextInt();
            soma += numero;
        }
        
        double media = soma / 10.0;
        System.out.println("Média: " + media);
    }
    
    // Exercício 8: Ler 10 inteiros positivos e calcular média
    public static void exercicio8(Scanner sc) {
        System.out.println("=== Exercício 8 ===");
        int soma = 0;
        int contador = 0;
        
        while (contador < 10) {
            System.out.print("Digite um número positivo: ");
            int numero = sc.nextInt();
            
            if (numero > 0) {
                soma += numero;
                contador++;
            } else {
                System.out.println("Número não positivo ignorado!");
            }
        }
        
        double media = soma / 10.0;
        System.out.println("Média dos números positivos: " + media);
    }
    
    // Exercício 9: Menor e maior valor entre 10 números
    public static void exercicio9(Scanner sc) {
        System.out.println("=== Exercício 9 ===");
        System.out.print("Digite o 1° número: ");
        int primeiro = sc.nextInt();
        int menor = primeiro;
        int maior = primeiro;
        
        for (int i = 2; i <= 10; i++) {
            System.out.print("Digite o " + i + "° número: ");
            int numero = sc.nextInt();
            
            if (numero < menor) menor = numero;
            if (numero > maior) maior = numero;
        }
        
        System.out.println("Menor valor: " + menor);
        System.out.println("Maior valor: " + maior);
    }
    
    // Exercício 10: N primeiros números naturais ímpares
    public static void exercicio10(Scanner sc) {
        System.out.println("=== Exercício 10 ===");
        System.out.print("Digite N: ");
        int n = sc.nextInt();
        
        int contador = 0;
        int numero = 1;
        
        while (contador < n) {
            System.out.print(numero + " ");
            numero += 2;
            contador++;
        }
        System.out.println();
    }
    
    // Exercício 11: Soma dos 50 primeiros números pares (0 a 100)
    public static void exercicio11() {
        System.out.println("=== Exercício 11 ===");
        int soma = 0;
        int contador = 0;
        int numero = 0;
        
        while (contador < 50 && numero <= 100) {
            if (numero % 2 == 0) {
                soma += numero;
                contador++;
            }
            numero++;
        }
        
        System.out.println("Soma dos 50 primeiros números pares: " + soma);
    }
    
    // Exercício 12: Números naturais de 0 até N
    public static void exercicio12(Scanner sc) {
        System.out.println("=== Exercício 12 ===");
        System.out.print("Digite N: ");
        int n = sc.nextInt();
        
        for (int i = 0; i <= n; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
    
    // Exercício 13: Números pares de 0 até N (crescente)
    public static void exercicio13(Scanner sc) {
        System.out.println("=== Exercício 13 ===");
        System.out.print("Digite N (par): ");
        int n = sc.nextInt();
        
        for (int i = 0; i <= n; i += 2) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
    
    // Exercício 14: Números pares de 0 até N (decrescente)
    public static void exercicio14(Scanner sc) {
        System.out.println("=== Exercício 14 ===");
        System.out.print("Digite N (par): ");
        int n = sc.nextInt();
        
        for (int i = n; i >= 0; i -= 2) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
    
    // Exercício 15: Números ímpares de 1 até N (crescente)
    public static void exercicio15(Scanner sc) {
        System.out.println("=== Exercício 15 ===");
        System.out.print("Digite N (ímpar): ");
        int n = sc.nextInt();
        
        for (int i = 1; i <= n; i += 2) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
    
    // Exercício 16: Soma dos n primeiros números naturais
    public static void exercicio16(Scanner sc) {
        System.out.println("=== Exercício 16 ===");
        System.out.print("Digite n: ");
        int n = sc.nextInt();
        
        int soma = 0;
        for (int i = 1; i <= n; i++) {
            soma += i;
        }
        
        System.out.println("Soma dos " + n + " primeiros números naturais: " + soma);
    }
    
    // Exercício 17: Maior número entre uma quantidade definida pelo usuário
    public static void exercicio17(Scanner sc) {
        System.out.println("=== Exercício 17 ===");
        System.out.print("Quantos números deseja digitar? ");
        int quantidade = sc.nextInt();
        
        System.out.print("Digite o 1° número: ");
        int maior = sc.nextInt();
        
        for (int i = 2; i <= quantidade; i++) {
            System.out.print("Digite o " + i + "° número: ");
            int numero = sc.nextInt();
            if (numero > maior) {
                maior = numero;
            }
        }
        
        System.out.println("Maior número: " + maior);
    }
    
    // Exercício 18: Separar algarismos de um número entre 100 e 9999
    public static void exercicio18(Scanner sc) {
        System.out.println("=== Exercício 18 ===");
        System.out.print("Digite um número entre 100 e 9999: ");
        int numero = sc.nextInt();
        
        if (numero < 100 || numero > 9999) {
            System.out.println("Número fora do intervalo!");
            return;
        }
        
        while (numero > 0) {
            int algarismo = numero % 10;
            System.out.println(algarismo);
            numero /= 10;
        }
    }
    
    // Exercício 19: Contar números pares (termina com 0)
    public static void exercicio19(Scanner sc) {
        System.out.println("=== Exercício 19 ===");
        int totalLidos = 0;
        int totalPares = 0;
        int numero;
        
        do {
            System.out.print("Digite um número (0 para sair): ");
            numero = sc.nextInt();
            
            if (numero != 0) {
                totalLidos++;
                if (numero % 2 == 0) {
                    totalPares++;
                    System.out.println(numero + " é par");
                } else {
                    System.out.println(numero + " é ímpar");
                }
            }
        } while (numero != 0);
        
        System.out.println("Total de números lidos: " + totalLidos);
        System.out.println("Total de números pares: " + totalPares);
    }
    
    // Exercício 20: Soma de pares e multiplicação de ímpares em um intervalo
    public static void exercicio20(Scanner sc) {
        System.out.println("=== Exercício 20 ===");
        System.out.print("Digite o primeiro número: ");
        int num1 = sc.nextInt();
        System.out.print("Digite o segundo número: ");
        int num2 = sc.nextInt();
        
        int inicio = Math.min(num1, num2);
        int fim = Math.max(num1, num2);
        
        int somaPares = 0;
        int multiplicacaoImpares = 1;
        boolean temImpar = false;
        
        for (int i = inicio; i <= fim; i++) {
            if (i % 2 == 0) {
                somaPares += i;
            } else {
                multiplicacaoImpares *= i;
                temImpar = true;
            }
        }
        
        System.out.println("Soma dos pares: " + somaPares);
        if (temImpar) {
            System.out.println("Multiplicação dos ímpares: " + multiplicacaoImpares);
        } else {
            System.out.println("Não há números ímpares no intervalo");
        }
    }
    
    // Exercício 21: Média de notas válidas (0 a 10)
    public static void exercicio21(Scanner sc) {
        System.out.println("=== Exercício 21 ===");
        double soma = 0;
        int contador = 0;
        double nota;
        
        do {
            System.out.print("Digite uma nota (0 a 10): ");
            nota = sc.nextDouble();
            
            if (nota >= 0 && nota <= 10) {
                soma += nota;
                contador++;
            }
        } while (nota >= 0 && nota <= 10);
        
        if (contador > 0) {
            double media = soma / contador;
            System.out.println("Média das notas: " + media);
        }
    }
    
    // Exercício 22: Soma dos divisores de um número (exceto ele próprio)
    public static void exercicio22(Scanner sc) {
        System.out.println("=== Exercício 22 ===");
        System.out.print("Digite um número: ");
        int numero = sc.nextInt();
        
        int soma = 0;
        for (int i = 1; i < numero; i++) {
            if (numero % i == 0) {
                soma += i;
            }
        }
        
        System.out.println("Soma dos divisores de " + numero + ": " + soma);
    }
    
    // Exercício 23: Soma de múltiplos de 3 ou 5 menores que 1000
    public static void exercicio23() {
        System.out.println("=== Exercício 23 ===");
        int soma = 0;
        
        for (int i = 1; i < 1000; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                soma += i;
            }
        }
        
        System.out.println("Soma dos múltiplos de 3 ou 5 menores que 1000: " + soma);
    }
    
    // Exercício 24: Idade média de um grupo (para com idade 0)
    public static void exercicio24(Scanner sc) {
        System.out.println("=== Exercício 24 ===");
        int somaIdades = 0;
        int contador = 0;
        int idade;
        
        do {
            System.out.print("Digite uma idade (0 para sair): ");
            idade = sc.nextInt();
            
            if (idade != 0) {
                somaIdades += idade;
                contador++;
            }
        } while (idade != 0);
        
        if (contador > 0) {
            double media = (double) somaIdades / contador;
            System.out.println("Idade média: " + media);
        }
    }
    
    // Exercício 25: Cálculo de potenciação (x^y)
    public static void exercicio25(Scanner sc) {
        System.out.println("=== Exercício 25 ===");
        System.out.print("Digite a base (x): ");
        int base = sc.nextInt();
        System.out.print("Digite o expoente (y): ");
        int expoente = sc.nextInt();
        
        int resultado = 1;
        for (int i = 0; i < expoente; i++) {
            resultado *= base;
        }
        
        System.out.println(base + "^" + expoente + " = " + resultado);
    }
    
    // Exercício 26: Cálculo de S (não especificado na lista, implementando S = 1 + 1/2 + 1/3 + ... + 1/n)
    public static void exercicio26() {
        System.out.println("=== Exercício 26 ===");
        double s = 0;
        int n = 100; // Assumindo n = 100
        
        for (int i = 1; i <= n; i++) {
            s += 1.0 / i;
        }
        
        System.out.println("Valor de S: " + s);
    }
    
    // Exercício 27: Maior e menor número (para com número negativo)
    public static void exercicio27(Scanner sc) {
        System.out.println("=== Exercício 27 ===");
        System.out.print("Digite um número (negativo para sair): ");
        int numero = sc.nextInt();
        
        if (numero < 0) {
            System.out.println("Nenhum número positivo foi digitado!");
            return;
        }
        
        int maior = numero;
        int menor = numero;
        
        while (numero >= 0) {
            if (numero > maior) maior = numero;
            if (numero < menor) menor = numero;
            
            System.out.print("Digite um número (negativo para sair): ");
            numero = sc.nextInt();
        }
        
        System.out.println("Maior número: " + maior);
        System.out.println("Menor número: " + menor);
    }
    
    // Exercício 28: Salário com aumentos anuais
    public static void exercicio28() {
        System.out.println("=== Exercício 28 ===");
        double salario = 4000.0; // 2019
        double percentualAumento = 1.5; // 2020
        
        // 2020
        salario += salario * percentualAumento / 100;
        System.out.println("Salário 2020: R$ " + salario);
        
        // 2021 em diante até o ano atual (2025)
        for (int ano = 2021; ano <= 2025; ano++) {
            percentualAumento *= 2;
            salario += salario * percentualAumento / 100;
            System.out.println("Salário " + ano + ": R$ " + salario);
        }
    }
    
    // Exercício 29: Somar 5 números e exibir cada um
    public static void exercicio29(Scanner sc) {
        System.out.println("=== Exercício 29 ===");
        int[] numeros = new int[5];
        int soma = 0;
        
        for (int i = 0; i < 5; i++) {
            System.out.print("Digite o " + (i+1) + "° número: ");
            numeros[i] = sc.nextInt();
            soma += numeros[i];
        }
        
        System.out.println("Soma: " + soma);
        System.out.println("Números digitados:");
        for (int numero : numeros) {
            System.out.println(numero);
        }
    }
    
    // Exercício 30: Verificar se valor existe no vetor
    public static void exercicio30(Scanner sc) {
        System.out.println("=== Exercício 30 ===");
        int[] vetor = new int[10];
        
        // Lendo o vetor
        for (int i = 0; i < 10; i++) {
            System.out.print("Digite o " + (i+1) + "° número: ");
            vetor[i] = sc.nextInt();
        }
        
        System.out.print("Digite um valor para buscar: ");
        int valorBusca = sc.nextInt();
        
        boolean encontrado = false;
        for (int numero : vetor) {
            if (numero == valorBusca) {
                encontrado = true;
                break;
            }
        }
        
        if (encontrado) {
            System.out.println("Valor encontrado no vetor!");
        } else {
            System.out.println("Valor não encontrado no vetor!");
        }
    }
    
    // Exercício 31: Separar números pares e ímpares em listas
    public static void exercicio31(Scanner sc) {
        System.out.println("=== Exercício 31 ===");
        ArrayList<Integer> numeros = new ArrayList<>();
        ArrayList<Integer> pares = new ArrayList<>();
        ArrayList<Integer> impares = new ArrayList<>();
        
        for (int i = 0; i < 20; i++) {
            System.out.print("Digite o " + (i+1) + "° número: ");
            int numero = sc.nextInt();
            numeros.add(numero);
            
            if (numero % 2 == 0) {
                pares.add(numero);
            } else {
                impares.add(numero);
            }
        }
        
        System.out.println("Números originais: " + numeros);
        System.out.println("Números pares: " + pares);
        System.out.println("Números ímpares: " + impares);
    }
    
    // Exercício 32: Contar consoantes em vetor de caracteres
    public static void exercicio32(Scanner sc) {
        System.out.println("=== Exercício 32 ===");
        char[] vetor = new char[10];
        int consoantes = 0;
        ArrayList<Character> listaConsoantes = new ArrayList<>();
        
        for (int i = 0; i < 10; i++) {
            System.out.print("Digite o " + (i+1) + "° caractere: ");
            vetor[i] = sc.next().charAt(0);
            
            char c = Character.toLowerCase(vetor[i]);
            if (Character.isLetter(c) && !"aeiou".contains(String.valueOf(c))) {
                consoantes++;
                listaConsoantes.add(vetor[i]);
            }
        }
        
        System.out.println("Número de consoantes: " + consoantes);
        System.out.println("Consoantes: " + listaConsoantes);
    }
    
    // Exercício 33: Média de 10 alunos com 4 notas cada
    public static void exercicio33(Scanner sc) {
        System.out.println("=== Exercício 33 ===");
        double[] medias = new double[10];
        int alunosAprovados = 0;
        
        for (int i = 0; i < 10; i++) {
            System.out.println("Aluno " + (i+1) + ":");
            double soma = 0;
            
            for (int j = 0; j < 4; j++) {
                System.out.print("Digite a " + (j+1) + "ª nota: ");
                double nota = sc.nextDouble();
                soma += nota;
            }
            
            medias[i] = soma / 4;
            if (medias[i] >= 7.0) {
                alunosAprovados++;
            }
        }
        
        System.out.println("Médias dos alunos:");
        for (int i = 0; i < 10; i++) {
            System.out.println("Aluno " + (i+1) + ": " + medias[i]);
        }
        System.out.println("Alunos com média >= 7.0: " + alunosAprovados);
    }
    
    // Exercício 34: Verificar se número é primo
    public static void exercicio34(Scanner sc) {
        System.out.println("=== Exercício 34 ===");
        System.out.print("Digite um número maior que 1: ");
        int numero = sc.nextInt();
        
        if (numero <= 1) {
            System.out.println("Número deve ser maior que 1!");
            return;
        }
        
        boolean primo = true;
        for (int i = 2; i <= Math.sqrt(numero); i++) {
            if (numero % i == 0) {
                primo = false;
                break;
            }
        }
        
        if (primo) {
            System.out.println(numero + " é primo!");
        } else {
            System.out.println(numero + " não é primo!");
        }
    }
    
    // Exercício 35: Soma dos n primeiros números primos
    public static void exercicio35(Scanner sc) {
        System.out.println("=== Exercício 35 ===");
        System.out.print("Digite n: ");
        int n = sc.nextInt();
        
        int soma = 0;
        int contador = 0;
        int numero = 2;
        
        while (contador < n) {
            boolean primo = true;
            for (int i = 2; i <= Math.sqrt(numero); i++) {
                if (numero % i == 0) {
                    primo = false;
                    break;
                }
            }
            
            if (primo) {
                soma += numero;
                contador++;
            }
            numero++;
        }
        
        System.out.println("Soma dos " + n + " primeiros números primos: " + soma);
    }
    
    // Exercício 36: Soma de ímpares em um intervalo
    public static void exercicio36(Scanner sc) {
        System.out.println("=== Exercício 36 ===");
        System.out.print("Digite o valor inicial: ");
        int inicio = sc.nextInt();
        System.out.print("Digite o valor final: ");
        int fim = sc.nextInt();
        
        if (inicio > fim) {
            System.out.println("Intervalo de valores inválido");
            return;
        }
        
        int soma = 0;
        for (int i = inicio; i <= fim; i++) {
            if (i % 2 != 0) {
                soma += i;
            }
        }
        
        System.out.println("Soma dos ímpares neste intervalo: " + soma);
    }
    
    // Exercício 37: Associação em paralelo de resistores
    public static void exercicio37(Scanner sc) {
        System.out.println("=== Exercício 37 ===");
        double r1, r2;
        
        do {
            System.out.print("Digite R1 (0 para sair): ");
            r1 = sc.nextDouble();
            
            if (r1 != 0) {
                System.out.print("Digite R2: ");
                r2 = sc.nextDouble();
                
                if (r2 != 0) {
                    double rParalelo = (r1 * r2) / (r1 + r2);
                    System.out.println("Resistência em paralelo: " + rParalelo + " Ω");
                } else {
                    break;
                }
            }
        } while (r1 != 0);
    }
    
    // Exercício 38: Quadrado, cubo e raiz quadrada de números
    public static void exercicio38(Scanner sc) {
        System.out.println("=== Exercício 38 ===");
        double numero;
        
        do {
            System.out.print("Digite um número (negativo ou zero para sair): ");
            numero = sc.nextDouble();
            
            if (numero > 0) {
                double quadrado = numero * numero;
                double cubo = numero * numero * numero;
                double raiz = Math.sqrt(numero);
                
                System.out.println("Número: " + numero);
                System.out.println("Quadrado: " + quadrado);
                System.out.println("Cubo: " + cubo);
                System.out.println("Raiz quadrada: " + raiz);
                System.out.println();
            }
        } while (numero > 0);
    }
    
    // Exercício 39: Jogo de adivinhação
    public static void exercicio39() {
        System.out.println("=== Exercício 39 ===");
        Scanner sc = new Scanner(System.in);
        Random random = new Random();
        
        int numeroSecreto = random.nextInt(100) + 1;
        int tentativas = 0;
        int chute;
        
        System.out.println("Tente adivinhar o número entre 1 e 100!");
        
        do {
            System.out.print("Digite seu chute: ");
            chute = sc.nextInt();
            tentativas++;
            
            if (chute < numeroSecreto) {
                System.out.println("Muito baixo! Tente novamente.");
            } else if (chute > numeroSecreto) {
                System.out.println("Muito alto! Tente novamente.");
            } else {
                System.out.println("Parabéns! Você acertou!");
                System.out.println("Número de tentativas: " + tentativas);
            }
        } while (chute != numeroSecreto);
    }
    
    // Exercício 40: Menu de operações matemáticas
    public static void exercicio40(Scanner sc) {
        System.out.println("=== Exercício 40 ===");
        int opcao;
        
        do {
            System.out.println("\n=== MENU ===");
            System.out.println("1 - Adição");
            System.out.println("2 - Subtração");
            System.out.println("3 - Multiplicação");
            System.out.println("4 - Divisão");
            System.out.println("5 - Sair");
            System.out.print("Escolha uma opção: ");
            opcao = sc.nextInt();
            
            if (opcao >= 1 && opcao <= 4) {
                System.out.print("Digite o primeiro número: ");
                double num1 = sc.nextDouble();
                System.out.print("Digite o segundo número: ");
                double num2 = sc.nextDouble();
                
                switch (opcao) {
                    case 1:
                        System.out.println("Resultado: " + (num1 + num2));
                        break;
                    case 2:
                        System.out.println("Resultado: " + (num1 - num2));
                        break;
                    case 3:
                        System.out.println("Resultado: " + (num1 * num2));
                        break;
                    case 4:
                        if (num2 != 0) {
                            System.out.println("Resultado: " + (num1 / num2));
                        } else {
                            System.out.println("Erro: Divisão por zero!");
                        }
                        break;
                }
            } else if (opcao != 5) {
                System.out.println("Opção inválida!");
            }
        } while (opcao != 5);
        
        System.out.println("Programa encerrado!");
    }
    
    // Exercício 41: Diferença entre soma dos quadrados e quadrado da soma
    public static void exercicio41() {
        System.out.println("=== Exercício 41 ===");
        int n = 100;
        
        // Soma dos quadrados dos primeiros 100 números naturais
        int somaQuadrados = 0;
        for (int i = 1; i <= n; i++) {
            somaQuadrados += i * i;
        }
        
        // Soma dos primeiros 100 números naturais
        int soma = 0;
        for (int i = 1; i <= n; i++) {
            soma += i;
        }
        
        // Quadrado da soma
        int quadradoDaSoma = soma * soma;
        
        // Diferença
        int diferenca = quadradoDaSoma - somaQuadrados;
        
        System.out.println("Soma dos quadrados: " + somaQuadrados);
        System.out.println("Quadrado da soma: " + quadradoDaSoma);
        System.out.println("Diferença: " + diferenca);
    }
    
    // Exercício 42: Sistema de votação
    public static void exercicio42(Scanner sc) {
        System.out.println("=== Exercício 42 ===");
        
        // Contadores
        int votosCandidato1 = 0, votosCandidato2 = 0;
        int votosCandidato3 = 0, votosCandidato4 = 0;
        int votosNulos = 0, votosBrancos = 0;
        int totalVotos = 0;
        
        System.out.println("=== ELEIÇÃO PRESIDENCIAL ===");
        System.out.println("1 - José Silva");
        System.out.println("2 - João Santos");
        System.out.println("3 - Maria Oliveira");
        System.out.println("4 - Ana Costa");
        System.out.println("5 - Voto Nulo");
        System.out.println("6 - Voto em Branco");
        System.out.println("0 - Finalizar votação");
        
        int voto;
        do {
            System.out.print("\nDigite o código do voto: ");
            voto = sc.nextInt();
            
            switch (voto) {
                case 1:
                    votosCandidato1++;
                    totalVotos++;
                    break;
                case 2:
                    votosCandidato2++;
                    totalVotos++;
                    break;
                case 3:
                    votosCandidato3++;
                    totalVotos++;
                    break;
                case 4:
                    votosCandidato4++;
                    totalVotos++;
                    break;
                case 5:
                    votosNulos++;
                    totalVotos++;
                    break;
                case 6:
                    votosBrancos++;
                    totalVotos++;
                    break;
                case 0:
                    break;
                default:
                    System.out.println("Código inválido!");
                    break;
            }
        } while (voto != 0);
        
        // Resultados
        System.out.println("\n=== RESULTADOS DA ELEIÇÃO ===");
        System.out.println("José Silva: " + votosCandidato1 + " votos");
        System.out.println("João Santos: " + votosCandidato2 + " votos");
        System.out.println("Maria Oliveira: " + votosCandidato3 + " votos");
        System.out.println("Ana Costa: " + votosCandidato4 + " votos");
        System.out.println("Votos nulos: " + votosNulos);
        System.out.println("Votos em branco: " + votosBrancos);
        System.out.println("Total de votos: " + totalVotos);
        
        if (totalVotos > 0) {
            double percentualNulos = (votosNulos * 100.0) / totalVotos;
            double percentualBrancos = (votosBrancos * 100.0) / totalVotos;
            
            System.out.printf("Percentual de votos nulos: %.2f%%\n", percentualNulos);
            System.out.printf("Percentual de votos em branco: %.2f%%\n", percentualBrancos);
        }
    }
    
    // Exercício 43: Avaliação de ginasta
    public static void exercicio43(Scanner sc) {
        System.out.println("=== Exercício 43 ===");
        System.out.print("Nome do atleta: ");
        sc.nextLine(); // Limpar buffer
        String nome = sc.nextLine();
        
        double[] notas = new double[7];
        
        // Ler as notas
        for (int i = 0; i < 7; i++) {
            System.out.print("Nota " + (i + 1) + ": ");
            notas[i] = sc.nextDouble();
        }
        
        // Encontrar maior e menor nota
        double maior = notas[0];
        double menor = notas[0];
        double soma = 0;
        
        for (double nota : notas) {
            if (nota > maior) maior = nota;
            if (nota < menor) menor = nota;
            soma += nota;
        }
        
        // Calcular média excluindo maior e menor
        double media = (soma - maior - menor) / 5.0;
        
        System.out.println("\nResultado final:");
        System.out.println("Atleta: " + nome);
        System.out.println("Melhor nota: " + maior);
        System.out.println("Pior nota: " + menor);
        System.out.printf("Média: %.2f\n", media);
    }
    
    // Exercício 44: Sistema da Academia BemMaisFort
    public static void exercicio44(Scanner sc) {
        System.out.println("=== Exercício 44 ===");
        
        int idadeMaisVelha = 0;
        double alturaMaisAlto = 0;
        double maiorPeso = 0;
        double somaAlturas = 0;
        double somaIMC = 0;
        int masculino = 0, feminino = 0;
        
        for (int i = 1; i <= 25; i++) {
            System.out.println("\nPessoa " + i + ":");
            
            System.out.print("Idade: ");
            int idade = sc.nextInt();
            
            System.out.print("Sexo (M/F): ");
            char sexo = sc.next().toUpperCase().charAt(0);
            
            System.out.print("Altura (m): ");
            double altura = sc.nextDouble();
            
            System.out.print("Peso (kg): ");
            double peso = sc.nextDouble();
            
            // Calcular IMC
            double imc = peso / (altura * altura);
            
            // Atualizar estatísticas
            if (idade > idadeMaisVelha) {
                idadeMaisVelha = idade;
            }
            
            if (altura > alturaMaisAlto) {
                alturaMaisAlto = altura;
            }
            
            if (peso > maiorPeso) {
                maiorPeso = peso;
            }
            
            somaAlturas += altura;
            somaIMC += imc;
            
            if (sexo == 'M') {
                masculino++;
            } else if (sexo == 'F') {
                feminino++;
            }
        }
        
        // Calcular médias e percentuais
        double mediaAltura = somaAlturas / 25.0;
        double mediaIMC = somaIMC / 25.0;
        double percentualMasculino = (masculino * 100.0) / 25.0;
        double percentualFeminino = (feminino * 100.0) / 25.0;
        
        // Exibir resultados
        System.out.println("\n=== ESTATÍSTICAS DA ACADEMIA ===");
        System.out.println("Idade da pessoa mais velha: " + idadeMaisVelha + " anos");
        System.out.printf("Altura do mais alto: %.2f m\n", alturaMaisAlto);
        System.out.printf("Maior peso: %.2f kg\n", maiorPeso);
        System.out.printf("Média de altura: %.2f m\n", mediaAltura);
        System.out.printf("Média de IMC: %.2f\n", mediaIMC);
        System.out.printf("Percentagem de sexo masculino: %.2f%%\n", percentualMasculino);
        System.out.printf("Percentagem de sexo feminino: %.2f%%\n", percentualFeminino);
    }
}