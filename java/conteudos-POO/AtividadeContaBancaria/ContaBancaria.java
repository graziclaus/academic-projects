package Atividades.AtividadeContaBancaria;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Scanner;

public class ContaBancaria {

    private static final Scanner scanner = new Scanner(System.in);
    public static final String RESET = "\u001B[0m";
    public static final String VERDE = "\u001B[32m";
    public static final String AZUL = "\u001B[34m";
    public static final String NEGRITO = "\u001B[1m";
    public static final String ITALICO = "\u001B[3m";
    String LARANJA = "\u001B[38;5;208m";

    private int numeroConta;
    private String agencia;
    private String titular;
    private double saldo;
    private String tipoConta;
    private double limite;
    private LocalDate dataAbertura;
    private String senha;
    private Cliente cliente;
    ArrayList<String> saques = new ArrayList<>();
    ArrayList<String> depositos = new ArrayList<>();

    public ContaBancaria(){

        this.dataAbertura = LocalDate.now();

    }

    public void cadastrarContaBancaria(ArrayList<Cliente> clientes){

        System.out.println("Estamos na criação da conta bancária do cliente. Por favor, insira os dados que estão sendo pedidos abaixo: \n");

        boolean titularEncontrado = false;

        while (!titularEncontrado){

            System.out.println("Nome do titular da conta: ");
            String nomeTitularInserido = scanner.nextLine();

            Cliente achouNomeCliente = null;

            for (Cliente buscaNomeCliente : clientes){

                if (buscaNomeCliente.getNome().equalsIgnoreCase(nomeTitularInserido)){

                    achouNomeCliente = buscaNomeCliente;
                    break;

                }
            }

            if(achouNomeCliente != null) {

                this.cliente = achouNomeCliente;
                this.titular = achouNomeCliente.getNome();
                titularEncontrado = true;

            } else {

                System.out.println(LARANJA + "Cliente não encontrado. Escolha uma opção:" + RESET);
                System.out.println("1 - Criar novo cliente");
                System.out.println("2 - Tentar outro nome");
                int opcao = scanner.nextInt();
                scanner.nextLine();

                switch (opcao) {

                    case 1:

                        Cliente novoCliente = new Cliente();
                        novoCliente.cadastrarCliente();
                        clientes.add(novoCliente);
                        this.cliente = novoCliente;
                        this.titular = novoCliente.getNome();
                        break;

                    case 2:

                        System.out.println("Tente digitar outro nome.");
                        break;

                    default:

                        System.out.println(LARANJA + "Opção inválida, tente novamente." + RESET);
                        break;

                }
            }
        }

        System.out.println("Número da conta: ");
        this.numeroConta = scanner.nextInt();
        scanner.nextLine();

        System.out.println("\n");

        System.out.println("Agência da conta: ");
        this.agencia = scanner.nextLine();

        System.out.println("\n");

        System.out.println("Saldo atual da conta: ");
        this.saldo = scanner.nextDouble();
        scanner.nextLine();

        System.out.println("\n");

        System.out.println("Tipo de conta (Corrente, universitária, poupança etc");
        this.tipoConta = scanner.nextLine();

        System.out.println("\n");

        System.out.println("Limite da conta: ");
        this.limite = scanner.nextDouble();
        scanner.nextLine();

        System.out.println("\n");

        System.out.println("Senha da conta: ");
        this.senha = scanner.nextLine();

        this.dataAbertura = LocalDate.now();

        System.out.println("Conta cadastrada com sucesso!\n");

    }

    public ContaBancaria buscarConta(ArrayList<ContaBancaria> contas, int numeroConta){

        for (ContaBancaria c : contas){

            if(c.getNumeroConta() == numeroConta){

                return c;

            }
        }

        return null;

    }

    public void sacarContaBancaria(ArrayList<ContaBancaria> contas){

        ContaBancaria contaBancaria = null;

        while (contaBancaria == null) {

            System.out.println("Digite o número da conta para sacar: ");
            int numeroContaBusca = scanner.nextInt();
            scanner.nextLine();

            contaBancaria = buscarConta(contas, numeroContaBusca);

            if (contaBancaria == null) {

                System.out.println(LARANJA + "Conta não encontrada! Tente novamente." + RESET);

            }
        }

        System.out.println("Digite o valor a sacar: ");
        double valorSacar = scanner.nextDouble();
        scanner.nextLine();

        while (valorSacar <= 0 || valorSacar > contaBancaria.getSaldo()) {

            System.out.println(LARANJA + "Valor inválido ou saldo insuficiente. Tente novamente: " + RESET);
            valorSacar = scanner.nextDouble();
            scanner.nextLine();

        }

        contaBancaria.setSaldo(contaBancaria.getSaldo() - valorSacar);
        contaBancaria.saques.add("Saque: " + valorSacar);
        System.out.println("Saque feito com sucesso! Saldo atual: " + contaBancaria.getSaldo());

    }

    public void depositarContaBancaria(ArrayList<ContaBancaria> contas) {

        ContaBancaria contaBancaria = null;

        while (contaBancaria == null) {

            System.out.println("Digite o número da conta para depositar: ");
            int numeroContaBusca = scanner.nextInt();
            scanner.nextLine();

            contaBancaria = buscarConta(contas, numeroContaBusca);

            if (contaBancaria == null) {

                System.out.println(LARANJA + "Conta não encontrada! Tente novamente." + RESET);

            }
        }

        System.out.println("Digite o valor a depositar: ");
        double valorDepositar = scanner.nextDouble();
        scanner.nextLine();

        while (valorDepositar <= 0) {

            System.out.println(LARANJA + "Valor inválido. Tente novamente: " + RESET);
            valorDepositar = scanner.nextDouble();
            scanner.nextLine();

        }

        contaBancaria.setSaldo(contaBancaria.getSaldo() + valorDepositar);
        contaBancaria.depositos.add("Depósito: " + valorDepositar);
        System.out.println("Depósito feito com sucesso! Saldo atual: " + contaBancaria.getSaldo());

    }

    public void criarExtratoContaBancaria(){

        // pesquisar por número da conta

        System.out.println(NEGRITO + "Imprimindo extrato da conta..." + RESET);
        System.out.println("╔════════ Extrato da Conta ═════════╗\n");
        System.out.println("Titular: " + this.titular + "\n");
        System.out.println("Número da conta: " + this.numeroConta + "\n");
        System.out.println("Agência: " + this.agencia + "\n");
        System.out.println("Tipo: " + this.tipoConta + "\n");
        System.out.println("Saldo: " + this.saldo + "\n");
        System.out.println("Limite: " + this.limite + "\n");
        System.out.println("Data de abertura: " + this.dataAbertura + "\n");
        System.out.println("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅");
        System.out.println("\n");

        if(saques.isEmpty()){

            System.out.println(LARANJA + "Este cliente não realizou nenhum saque na conta." + RESET);

        } else {

            System.out.println(VERDE + "Todos os saques realizados por " + RESET +  ITALICO + AZUL + this.titular + RESET);
            for(String s : saques){

                System.out.println(s);

            }
        }

        if (depositos.isEmpty()){

            System.out.println(LARANJA + "Este cliente não realizou nenhum depósito na conta." + RESET);

        } else {

            System.out.println(VERDE + "Todos os depósitos realizados por " + RESET +  ITALICO + AZUL + this.titular + RESET);
            for(String d : depositos){

                System.out.println(d);

            }
        }

        System.out.println("╚════════════════════════════════════╝");

    }

    public void alterarInformacoesCadastraisContaBancaria(ArrayList<ContaBancaria> contas){

        ContaBancaria contaBancaria = null;

        while (contaBancaria == null) {

            System.out.println("Digite o número da conta para alterar os dados: ");
            int numeroContaBusca = scanner.nextInt();
            scanner.nextLine();

            contaBancaria = buscarConta(contas, numeroContaBusca);

            if (contaBancaria == null) {

                System.out.println(LARANJA + "Conta não encontrada! Tente novamente." + RESET);

            }
        }

        System.out.println("Saldo atual da conta: " + contaBancaria.getSaldo());
        double novoSaldo = scanner.nextDouble();
        scanner.nextLine();
        contaBancaria.setSaldo(novoSaldo);

        System.out.println("\nNovo tipo de conta (Corrente, universitária, poupança etc): ");
        String novoTipoConta = scanner.nextLine();
        contaBancaria.setTipoConta(novoTipoConta);

        System.out.println("\nNovo limite da conta: ");
        double novoLimite = scanner.nextDouble();
        scanner.nextLine();
        contaBancaria.setLimite(novoLimite);

        System.out.println("\nNova senha da conta: ");
        String novaSenha = scanner.nextLine();
        contaBancaria.setSenha(novaSenha);

        System.out.println("Dados da conta alterados com sucesso!\n");

    }

    public int getNumeroConta(){ return numeroConta; }
    public String getAgencia(){ return agencia; }
    public String getTitular(){ return titular; }
    public double getSaldo(){ return saldo; }
    public String getTipoConta(){ return tipoConta; }
    public double getLimite(){ return limite; }
    public LocalDate getDataAbertura(){ return dataAbertura; }
    public String getSenha(){ return senha; }
    public Cliente getCliente(){ return cliente; }

    // Um único cliente para uma única conta
    public void setCliente(Cliente cliente){ this.cliente = cliente; }
    public void setSaldo(double saldo){ this.saldo = saldo; }
    public void setTipoConta(String tipoConta) { this.tipoConta = tipoConta; }
    public void setLimite(double limite) { this.limite = limite; }
    public void setSenha(String senha){ this.senha = senha; }

}
