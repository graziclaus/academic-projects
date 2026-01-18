package Atividades.HerancaAtividade;

public class MobOfensivo extends Mob{

    private Item drop;

    public MobOfensivo(String nome, int coracoes, int dano, int armadura, int xp, Item drop) {
        super(nome, coracoes, dano, armadura, xp);

        this.drop = drop;

    }

    public void atacar(Personagem alvo) {

        int danoBase = getDano();
        System.out.println(getNome() + " atacou " + alvo.getNome() + " causando " + danoBase + " de dano!");
        alvo.receberDano(danoBase, this);

    }

    public Item getDrop() { return drop; }
}
