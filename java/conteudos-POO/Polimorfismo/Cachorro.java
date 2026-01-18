package Atividades.Polimorfismo;

public class Cachorro extends Animal{

    private String tamanho;

    public void mostrarBarriga(){

        System.out.println("Quem é o bom garoto!! " +
                "\u001B[3m--Mostra a barriga--\u001B[0m");

    }

    public void fazerBarulho(){

        System.out.println("AuAu \uD83D\uDC36");

    }

}
