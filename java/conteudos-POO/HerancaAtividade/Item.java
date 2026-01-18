package Atividades.HerancaAtividade;

public class Item {

    private final String nome;
    private int quantidade;
    private final int quantidadeMaxima;

    public Item(String nome, int quantidade, int quantidadeMaxima) {

        this.nome = nome;
        this.quantidade = quantidade;
        this.quantidadeMaxima = quantidadeMaxima;

    }

    public String getNome() { return nome; }
    public int getQuantidade() { return quantidade; }
    public int getQuantidadeMaxima() { return quantidadeMaxima; }

    public void setQuantidade(int quantidade) { this.quantidade = quantidade; }
}
