package Atividades.AtividadeInterface;

public class Main {

    public static void main(String[] args) {

        ItemBibliotecaDigital ebook1 = new Ebook("Ana Souza", "Java para Iniciantes");
        ItemBibliotecaDigital ebook2 = new Ebook("Carlos Lima", "Design de Software");

        ItemBibliotecaDigital video1 = new VideoDigital("TechPro", "Introdução ao Java");
        ItemBibliotecaDigital video2 = new VideoDigital("CodeMaster", "Padrões de Projeto");

        System.out.println("------------------------ Descrições -----------------------------");

        System.out.println(ebook1.descricao());
        System.out.println(ebook2.descricao());
        System.out.println(video1.descricao());
        System.out.println(video2.descricao());

        System.out.println("-----------------------------------------------------------------");

        System.out.println("------------------------ Downloads e Visualizações -----------------------------");

        ((Ebook) ebook1).baixar();
        ((Ebook) ebook2).baixar();

        ((VideoDigital) video1).baixar();
        ((VideoDigital) video1).visualizar();

        ((VideoDigital) video2).baixar();
        ((VideoDigital) video2).visualizar();

        System.out.println("-----------------------------------------------------------------");

    }
}
