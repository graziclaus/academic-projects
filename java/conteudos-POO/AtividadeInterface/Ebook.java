package Atividades.AtividadeInterface;

public class Ebook extends ItemBibliotecaDigital implements Baixavel{


    public Ebook(String autor, String titulo) {
        super(autor, titulo);
    }

    @Override
    public void baixar() {

        System.out.println("Baixando o ebook: " + titulo);

    }

    @Override
    public String descricao() {
        return "Ebook: " + titulo +
                "Autor: " + autor;
    }
}
