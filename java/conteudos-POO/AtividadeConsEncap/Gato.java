package AtividadeObjetos;

public class Gato {

    private String nome;
    private String cor;
    private String raca;
    private int idade;
    private double peso;

    public Gato(){

        this.nome = "Lucy";
        this.cor = "Laranja";
        this.raca = "Vira-lata";
        this.idade = 3;
        this.peso = 4;

    }

    public Gato(String nome, String cor, String raca, int idade, float peso){

        this.nome = nome;
        this.cor = cor;
        this.raca = raca;
        this.idade = idade;
        this.peso = peso;

    }

    public String getNome(){

        return nome;

    }

    public String getCor(){

        return cor;

    }

    public String getRaca(){

        return cor;

    }

    public int getIdade(){

        return idade;

    }

    public double getPeso(){

        return peso;

    }

    public String toString(){

        return "Nome: " + nome + "\n" +
               "Cor: " + cor + "\n" +
               "Raça: " + raca + "\n" +
               "Idade: " + idade + "\n" +
               "Peso: " + peso;

    }

}
