package Atividades.HerancaAtividade;

public class Mob extends Personagem{

    private Item drop;

    public Mob(String nome, int coracoes, int dano, int armadura, int xp) {
        super(nome, coracoes, dano, armadura, xp);
    }

    public void atacar(Personagem alvo){

        System.out.println("");

    }

    public Item getDrop() { return drop; }

}
