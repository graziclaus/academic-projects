package Atividades.Polimorfismo;

public class Gato extends Animal{

    private String tipoPelo;

    public void enterrarNecessidadesAreia(){

        System.out.println("\u001B[3m--Enterrando cocô/xixi na areia--\u001B[0m");

    }

    public void fazerBarulho(){

        System.out.println("Miau~~ \uD83D\uDC31");

    }

}
