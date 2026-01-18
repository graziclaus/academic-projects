package Atividades.Polimorfismo;

public class Passaro extends Animal{

    private double tamanhoAsas;

    public void voar(){

        System.out.println("\u001B[3mBarulho das asas batendo\u001B[0m");

    }

    public void fazerBarulho(){

        System.out.println("\u001B[3m--Imitando barulho dos humanos--\u001B[0m \uD83D\uDC26");

    }

}
