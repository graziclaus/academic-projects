package Atividades.HerancaAtividade;

public class Ferramenta extends Item {

    private final int dano;
    private int durabilidade;

    public Ferramenta(String nome, int quantidade, int dano, int durabilidade) {

        super(nome, 1, 1);
        this.dano = 3;
        this.durabilidade = 131;

    }

    public void usar() {

        if (durabilidade > 0) {

            durabilidade--;
            System.out.println(getNome() + " foi usada. Durabilidade restante: " + durabilidade);

        } else {

            System.out.println(getNome() + " quebrou!");

        }
    }

    public int getDano() { return dano; }
    public int getDurabilidade() { return durabilidade; }

}
