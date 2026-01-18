package Atividades.AtividadeContaBancaria;

import java.util.Scanner;

public class Cliente {

    private static final Scanner scanner = new Scanner(System.in);
    private String nome;
    private String cpf;
    private String telefone;
    private String email;
    private String endereco;
    private ContaBancaria contaBancaria;
    private Gerente gerente;

    public Cliente(){ }

    public void cadastrarCliente(){

        System.out.println("Estamos na criação da conta do cliente. Por favor, insira os dados que estão sendo pedidos abaixo: \n");

        System.out.println("Nome do cliente: ");
        this.nome = scanner.nextLine();

        System.out.println("\n");

        System.out.println("CPF do cliente: ");
        this.cpf = scanner.nextLine();

        System.out.println("\n");

        System.out.println("Telefone de contato do cliente: ");
        this.telefone = scanner.nextLine();

        System.out.println("\n");

        System.out.println("E-mail de contato do cliente: ");
        this.email = scanner.nextLine();

        System.out.println("\n");

        System.out.println("Endereço do cliente: ");
        this.endereco = scanner.nextLine();

        System.out.println("Cliente cadastrado com sucesso!\n");

    }

    public String getNome(){ return nome; }
    public String getCpf(){ return cpf; }
    public String getEmail(){ return email; }
    public String getEndereco(){ return endereco; }
    public String getTelefone(){ return telefone; }
    public ContaBancaria contaBancaria(){ return contaBancaria; }
    public Gerente getGerente(){ return gerente; }

    // 1:1 --> Uma única conta para um único usuário
    public void setContaBancaria(ContaBancaria contaBancaria){ this.contaBancaria = contaBancaria; }
    // 1:1 --> Um gerente para um único cliente
    public void setGerente(Gerente gerente){ this.gerente = gerente; }

}
