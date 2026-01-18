package Atividades.AtividadeContaBancaria;

import java.util.ArrayList;

public class Gerente {

    private String nome;
    private String cpf;
    private String telefone;
    private double salario;
    private String email;
    private String agencia;
    private ArrayList<Cliente> clientes = new ArrayList<>();

    public static final String RESET = "\u001B[0m";
    String LARANJA = "\u001B[38;5;208m";

    public Gerente(String nome, String cpf, String telefone, double salario, String email, String agencia){

        this.nome = nome;
        this.cpf = cpf;
        this.telefone = telefone;
        this.salario = salario;
        this.email = email;
        this.agencia = agencia;

    }

    public String getNome(){ return nome;}
    public String getCpf(){ return cpf; }
    public String getTelefone(){ return telefone; }
    public double getSalario(){ return salario; }
    public String getEmail(){ return email; }
    public String getAgencia(){ return agencia; }
    // 1:n --> Um gerente para várias contas

    public void adicionarClientes(Cliente cliente){

        this.clientes.add(cliente);

    }

    public void listarClientes(){

        System.out.println("Clientes do gerente " + this.nome + ": ");

        if (clientes.isEmpty()) {

            System.out.println(LARANJA + "Este gerente não tem nenhum cliente cadastrado ainda." + RESET);

        } else {

            for (Cliente c : clientes){

                System.out.println("➥ " + c.getNome());

            }
        }
    }

    public ArrayList<Cliente> getClientes(){ return clientes; }

}
