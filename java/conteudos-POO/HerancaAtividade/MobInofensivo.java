package Atividades.HerancaAtividade;

public class MobInofensivo extends Mob{

    private Item drop;

    public MobInofensivo(String nome, int coracoes, int dano, int armadura, int xp,
                         Item drop) {

        super(nome, coracoes, dano, armadura, xp);

        this.drop = drop;

    }

    public Item getDrop() { return drop; }

}
