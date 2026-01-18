package Atividades.HerancaAtividade;

import java.util.Locale;

public class Armadura extends Item{

    private int defesa;
    private int durabilidade;

    public Armadura(String nome, int quantidade, int defesa, int durabilidade) {

        super(nome, 1, 1);

        this.defesa = 1;
        this.durabilidade = 80;

    }

    public void receberDano(int dano) {

        if (durabilidade > 0) {

            durabilidade -= dano;
            if (durabilidade < 0){

                durabilidade = 0;

            }
            System.out.println(getNome() + " recebeu dano, durabilidade diminuindo! Restante: " + durabilidade);
        }
    }

    public int getDefesa() { return defesa; }
    public int getDurabilidade() { return durabilidade; }

}
