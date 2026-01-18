package Atividades.AtividadeContaBancaria;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);

    public static final String RESET = "\u001B[0m";
    public static final String VERDE = "\u001B[32m";
    public static final String AZUL = "\u001B[34m";
    public static final String NEGRITO = "\u001B[1m";
    public static final String ITALICO = "\u001B[3m";

    public static void main(String[] args) {

        ArrayList<ContaBancaria> contas = new ArrayList<>();
        ArrayList<Cliente> clientes = new ArrayList<>();
        ArrayList<Gerente> gerentes = getGerentes();
        ContaBancaria conta = new ContaBancaria();
        Random random = new Random();

        String LARANJA = "\u001B[38;5;208m";
        int opcao = 0;

        while (opcao != 7) {

            System.out.println(LARANJA + "Olá! Nosso sistema gerência as contas bancárias dos clientes. O que você deseja fazer hoje?" + "\n" + RESET);
            System.out.println("———————————————————————————————————————— || ————————————————————————————————————————");
            System.out.println(NEGRITO + "Opções:" + RESET);
            System.out.println("1. Cadastrar;\n");
            System.out.println("2. Sacar;\n");
            System.out.println("3. Depositar;\n");
            System.out.println("4. Extrato;\n");
            System.out.println("5. Alterar Informações Cadastrais;\n");
            System.out.println("6. Listar clientes por gerentes;\n");
            System.out.println("7. Sair.\n");
            System.out.println("———————————————————————————————————————— || ————————————————————————————————————————");

            System.out.println(ITALICO + AZUL + "Sistema está aguardando por uma resposta... " + RESET + "➦");
            opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao) {

                case 1:

                    System.out.println(VERDE + "Para o cadastro de uma conta bancária, precisamos cadastrar o nosso cliente!" + RESET);
                    System.out.println("\n");

                    Cliente cliente = new Cliente();
                    cliente.cadastrarCliente();
                    clientes.add(cliente);

                    int numeroAleatorio = random.nextInt(gerentes.size());
                    Gerente gerenteSorteado = gerentes.get(numeroAleatorio);
                    cliente.setGerente(gerenteSorteado);
                    gerenteSorteado.adicionarClientes(cliente);

                    conta.setCliente(cliente);
                    contas.add(conta);

                    System.out.println("Voltando a área de cadastro da conta bancária");

                    for (int i = 0; i < 3; i++) {

                        try {

                            Thread.sleep(1000);

                        } catch (InterruptedException e) {

                            System.err.println("Algo deu errado... " + e.getMessage());

                        }

                        System.out.println(".");

                    }

                    System.out.println("\n");

                    conta.cadastrarContaBancaria(clientes);
                    break;

                case 2:

                    conta.sacarContaBancaria(contas);
                    break;

                case 3:

                    conta.depositarContaBancaria(contas);
                    break;

                case 4:

                    conta.criarExtratoContaBancaria();
                    break;

                case 5:

                    conta.alterarInformacoesCadastraisContaBancaria(contas);
                    break;

                case 6:

                    System.out.println("Gerentes disponíveis:");

                    for (Gerente g : gerentes) {

                        System.out.println("➥ " + g.getNome());

                    }

                    System.out.println("Digite o nome do gerente para poder listar todos os seus clientes: ");
                    String nomeGerenteBusca = scanner.nextLine();
                    Gerente buscaGerente = null;

                    for (Gerente g : gerentes) {

                        if (g.getNome().equalsIgnoreCase(nomeGerenteBusca)) {

                            buscaGerente = g;
                            break;

                        }
                    }

                    if (buscaGerente != null) {

                        buscaGerente.listarClientes();

                    } else {

                        System.out.println(LARANJA + "Parece que o gerente não existe ou foi digitado errado." + RESET);

                    }
                    break;

                case 7:

                    System.out.println(ITALICO + AZUL + "Encerrando o sistema... " + RESET + "Até logo!");
                    break;

                default:

                    System.out.println(LARANJA + "Opção inválida! Tente novamente." + RESET);
                    break;

            }
        }
    }

    private static ArrayList<Gerente> getGerentes() {
        Gerente gerenteNumeroUm = new Gerente(

                "Ana Beatriz Souza",
                "123.456.789-00",
                "(11) 91234-5678",
                8500.00,
                "ana.souza@banco.com",
                "Agência Centro - SP"

        );
        Gerente gerenteNumeroDois = new Gerente(

                "Carlos Henrique Lima",
                "987.654.321-11",
                "(21) 99876-5432",
                9200.00,
                "carlos.lima@banco.com",
                "Agência Copacabana - RJ"

        );
        Gerente gerenteNumeroTres = new Gerente(

                "Fernanda Oliveira",
                "456.789.123-22",
                "(31) 93456-7890",
                8700.00,
                "fernanda.oliveira@banco.com",
                "Agência Savassi - BH"

        );
        Gerente gerenteNumeroQuatro = new Gerente(

                "Ricardo Mendes",
                "321.654.987-33",
                "(41) 97654-3210",
                9100.00,
                "ricardo.mendes@banco.com",
                "Agência Batel - Curitiba"

        );

        ArrayList<Gerente> gerentes = new ArrayList<>();
        gerentes.add(gerenteNumeroUm);
        gerentes.add(gerenteNumeroDois);
        gerentes.add(gerenteNumeroTres);
        gerentes.add(gerenteNumeroQuatro);
        return gerentes;
    }
}
