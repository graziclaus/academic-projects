package AtividadeObjetos;

public class Passaro {

    private String especie;
    private String cor;
    private double tamanho;
    private double peso;
    private boolean podeVoar;

    public Passaro(){

        this.especie = "Canário";
        this.cor = "Amarelo";
        this.tamanho = 12.5;
        this.peso = 25;
        this.podeVoar = true;

    }

    public Passaro(String especie, String cor, double tamanho, double peso, boolean podeVoar){

        this.especie = especie;
        this.cor = cor;
        this.tamanho = tamanho;
        this.peso = peso;
        this.podeVoar = podeVoar;

    }

    public String getEspecie(){

        return especie;

    }

    public String getCor(){

        return cor;

    }

    public double getTamanho(){

        return tamanho;

    }

    public double getPeso(){

        return peso;

    }

    public boolean isPodeVoar(){

        return podeVoar;

    }

    public String toString(){

        return "Espécie: " + especie + "\n" +
               "Cor: " + cor + "\n" +
               "Tamanho: " + tamanho + "\n" +
               "Peso: " + peso + "\n" +
               "Pode voar?: " + podeVoar;

    }

}
