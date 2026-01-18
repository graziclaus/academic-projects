package Atividades.AtividadeInterface;

public abstract class ItemBibliotecaDigital {

    protected String autor;
    protected String titulo;

    public ItemBibliotecaDigital(String autor, String titulo){

        this.autor = autor;
        this.titulo = titulo;

    }

    public abstract String descricao();

    public String getAutor() { return autor; }
    public String getTitulo() { return titulo; }

}
