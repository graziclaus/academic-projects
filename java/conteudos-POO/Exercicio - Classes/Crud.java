import java.util.ArrayList;
import java.util.Scanner;

public class Crud
{

    public static class Pessoa
    {

        public String nome;
        public int idade;
        public String telefone;
        public String email;

    }

    // Uma única lista de pessoas para todos os métodos (criar, atualizar...) acessarem. A lista vai armazenar diferentes pessoas
    // na mesma lista: [Pessoa1, Pessoa2, Pessoa3...]
    // Inicialmente ficaria apenas o idenficiador do objeto, como [Crud$Pessoa@1b6d3586], mas pode ser modificado com um metodo que converta em string
    static ArrayList<Pessoa> listaPessoas = new ArrayList<>();

    // Mesmo caso, todos os outros métodos podem usar o scanner, não precisaria criar a mesma linha de código para todos
    static Scanner scanner = new Scanner(System.in);

    public static void cadastrarPessoa() {

        Pessoa pessoa = new Pessoa();
        System.out.println("Estamos na criação dos dados de uma pessoa!");

        System.out.println("Digite o nome: ");
        pessoa.nome = scanner.nextLine();

        System.out.println("Digite a idade: ");
        pessoa.idade = scanner.nextInt();
        scanner.nextLine();
        // Tava dando algum erro e não conseguia digitar o telefone depois da idade

        System.out.println("Digite o telefone: ");
        pessoa.telefone = scanner.nextLine();

        System.out.println("Digite o email: ");
        pessoa.email = scanner.nextLine();

        listaPessoas.add(pessoa);
        System.out.println("Pessoa cadastrada com sucesso!");

    }

    public static void buscarPessoa()
    {

        System.out.println("Digite o nome da pessoa a buscar: ");
        String nomePessoaBusca = scanner.nextLine();
        boolean existePessoa = false;

        // foreach
        for (Pessoa pessoa : listaPessoas)
        {

            // Procura o nome independente se esteja "gRaZi" ou "GRAZI"
            if (pessoa.nome.equalsIgnoreCase(nomePessoaBusca))
            {
                System.out.println("A pessoa chamada " + pessoa.nome + " foi encontrada!");
                existePessoa = true;
                break;

            }
        }
        // Outro jeito para usar existePessoa == false, se tentar colocar isso, faz um aviso de que pode ser simplificado
        if (!existePessoa)
        {

            System.out.println("A pessoa não existe no sistema! Tente cadastrar ou acessar outro nome.");

        }
    }

    public static void atualizarPessoa()
    {

        boolean pessoaExiste = false;

        while (!pessoaExiste)
        {

            System.out.println("Digite o nome da pessoa a ser atualizada!: ");
            String nomePessoaBusca = scanner.nextLine();

            // foreach
            for (Pessoa pessoa : listaPessoas) {

                // Procura o nome independente se esteja "gRaZi" ou "GRAZI"
                if (pessoa.nome.equalsIgnoreCase(nomePessoaBusca)) {

                    pessoaExiste = true;

                    System.out.println("Estamos na atualização dos dados de " + pessoa.nome + "!");

                    System.out.print("Digite o novo nome de " + pessoa.nome + ": ");
                    pessoa.nome = scanner.nextLine();

                    System.out.print("Nova idade: ");
                    pessoa.idade = scanner.nextInt();
                    scanner.nextLine();
                    // Tava dando algum erro e não conseguia digitar o telefone depois da idade

                    System.out.print("Novo telefone: ");
                    pessoa.telefone = scanner.nextLine();

                    System.out.print("Novo email: ");
                    pessoa.email = scanner.nextLine();

                    System.out.println("Dados atualizados com sucesso!");
                    break;
                }
            }

            if (!pessoaExiste)
            {

                System.out.println("Pessoa não encontrada! Tente outro nome ou cadastre uma nova pessoa.");

            }
        }
    }

    public static void listarPessoa() {

        System.out.println("Pessoas cadastradas no sistema: ");
        System.out.println("---------------------------// ---------------------------");
        // Lista de pessoas vazia
        if (listaPessoas.isEmpty())
        {

            System.out.println("Nenhuma pessoa foi cadastrada.");

        }

        for (Pessoa pessoa : listaPessoas)
        {

            System.out.println("Nome: " + pessoa.nome);
            System.out.println("Idade: " + pessoa.idade);
            System.out.println("Telefone: " + pessoa.telefone);
            System.out.println("Email: " + pessoa.email);
            System.out.println("--------------------------- ~~~~~ ---------------------------");

        }
    }

    public static void removerPessoa() {

        boolean pessoaExiste = false;

        while (!pessoaExiste)
        {

            System.out.println("Estamos na removeção dos dados de uma pessoa! Digite o nome da pessoa a ser removida: ");
            String nomeBusca = scanner.nextLine();

            for (Pessoa pessoa : listaPessoas) {

                if (pessoa.nome.equalsIgnoreCase(nomeBusca)) {

                    pessoaExiste = true;
                    listaPessoas.remove(pessoa);
                    System.out.println("Pessoa removida com sucesso!");
                    break;

                }
            }

            if (!pessoaExiste) {

                System.out.println("A pessoa não existe no sistema! Tente cadastrar ou acessar outro nome.");

            }
        }
    }

    public static void main(String[] args) {

        int opcao = 0;

        while (opcao != 6) {

            System.out.println("Bem-vindo! Este é um sistema de gerenciamento de usuário. " +
                    "Digite o comando que deseja realizar:");

            System.out.println("-------------------------------------------------------------");

            System.out.println("1 - Cadastrar nova pessoa\n");
            System.out.println("2 - Listar todas as pessoas\n");
            System.out.println("3 - Buscar pessoa por nome\n");
            System.out.println("4 - Atualizar dados de uma pessoa\n");
            System.out.println("5 - Remover pessoa pelo nome\n");
            System.out.println("6 - Sair\n");

            System.out.println("-------------------------------------------------------------");

            opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao) {

                case 1:
                    // Se o metodo não estiver estático, não é possível chamar desta maneira
                    cadastrarPessoa();
                    break;

                case 2:

                    listarPessoa();
                    break;

                case 3:

                    buscarPessoa();
                    break;

                case 4:

                    atualizarPessoa();
                    break;

                case 5:

                    removerPessoa();
                    break;

                case 6:

                    System.out.println("Obrigada por usar o sistema! Até logo!");
                    break;

                default:

                    System.out.println("Opção inválida! Tente novamente!");

            }
        }
    }
}


// --------------------------------------------------

// "String nome = scanner.nextLine();" é um atributo temporário
// "nome = scanner.nextLine();" usa diretamente o atributo nome do objeto