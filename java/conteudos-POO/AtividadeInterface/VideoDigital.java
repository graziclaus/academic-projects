package Atividades.AtividadeInterface;

public class VideoDigital extends ItemBibliotecaDigital implements Visualizavel, Baixavel{

    public VideoDigital(String autor, String titulo) { super(autor, titulo); }

    @Override
    public void baixar() {

        System.out.println("Baixando o vídeo digital: " + titulo);

    }

    @Override
    public String descricao() {
        return "Vídeo Digital: " + titulo +
                "Autor: " + autor;
    }

    @Override
    public void visualizar() {

        System.out.println("Reproduzindo " + titulo + "...");

    }
}
