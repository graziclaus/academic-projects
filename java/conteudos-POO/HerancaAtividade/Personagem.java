package Atividades.HerancaAtividade;

import java.util.ArrayList;

public class Personagem {

    private String nome;
    private int coracoes;
    private final int dano;
    private final int armadura;
    private final int xp;
    private ArrayList<Item> inventario;
    private ArrayList<Bloco> inventarioBlocos;

    public Personagem(String nome, int coracoes, int dano, int armadura, int xp){

        this.nome = nome;
        this.coracoes = coracoes;
        this.dano = dano;
        this.armadura = armadura;
        this.xp = xp;
        this.inventario = new ArrayList<>();
        this.inventarioBlocos = new ArrayList<>();

    }

    public void atacar(Personagem alvo){

        int danoFinal = this.dano;
        System.out.println(nome + " atacou " + alvo.getNome() + " causando " + danoFinal + " de dano!");
        alvo.receberDano(danoFinal, this);

    }

    public void receberDano(int danoRecebido, Personagem atacante){

        int danoFinal = danoRecebido - armadura;

        if (danoFinal < 0){

            danoFinal = 0;

        }

        coracoes -= danoFinal;

        if (coracoes < 0) {

            coracoes = 0;

        }
    }

    public String getNome(){ return nome; }
    public int getCoracoes(){ return coracoes; }
    public int getDano(){ return dano; }
    public int getArmadura(){ return armadura; }
    public int getXp(){ return xp; }
    public ArrayList<Item> getInventario(){ return inventario; }
    public ArrayList<Bloco> getInventarioBlocos() { return inventarioBlocos; }

    public void setCoracoes(int coracoes) { this.coracoes = coracoes; }
}
