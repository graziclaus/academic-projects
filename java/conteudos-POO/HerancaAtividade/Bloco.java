package Atividades.HerancaAtividade;

public class Bloco {

    private String nome;
    private int durabilidade;
    private Item dropBloco;

    public Bloco(String nome, int durabilidade, Item dropBloco){

        this.nome = nome;

        this.durabilidade = durabilidade;
        this.dropBloco = dropBloco;

    }

    public void quebrar(Jogador jogador) {

        if (durabilidade <= 0) {
            System.out.println("O bloco " + nome + " já está destruído.");
            return;
        }

        durabilidade--;
        System.out.println(jogador.getNome() + " quebrou o bloco " + nome + ". Durabilidade restante: " + durabilidade);

        if (durabilidade == 0) {
            System.out.println("O bloco " + nome + " foi destruído!");

            if (dropBloco != null) {
                jogador.adicionarItem(dropBloco);
                System.out.println("Você recebeu: " + dropBloco.getNome());
            }
        }
    }

    public String getNome() { return nome; }
    public int getDurabilidade() { return durabilidade; }
    public Item getDropBloco() { return dropBloco; }

}
