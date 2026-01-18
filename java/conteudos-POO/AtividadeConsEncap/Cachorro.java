package AtividadeObjetos;

public class Cachorro {

    private String nome;
    private String raca;
    private int idade;
    private double peso;
    private boolean vacinado;

    public Cachorro(){

        this.nome = "Rex";
        this.raca = "Labrador";
        this.idade = 8;
        this.peso = 25.5;
        this.vacinado = false;

    }

    public Cachorro(String nome, String raca, int idade, double peso, boolean vacinado){

        this.nome = nome;
        this.raca = raca;
        this.idade = idade;
        this.peso = peso;
        this.vacinado = vacinado;

    }

    public String getNome(){

        return nome;

    }

    public String getRaca(){

        return raca;

    }

    public int getIdade(){

        return idade;

    }

    public double getPeso(){

        return peso;

    }

    public boolean isVacinado() {

        return vacinado;

    }

    public String toString(){

        return "Nome: " + nome + "\n" +
               "Raça: " + raca + "\n" +
               "Idade: " + idade + "\n" +
               "Peso: " + peso + "\n" +
                "Vacinado: " + vacinado;

    }

}
