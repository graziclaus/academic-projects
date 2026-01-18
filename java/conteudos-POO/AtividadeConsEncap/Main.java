package AtividadeObjetos;

public class Main {

    public static final String RESET = "\u001B[0m";
    public static final String VERDE = "\u001B[32m";
    public static final String AZUL = "\u001B[34m";
    public static final String NEGRITO = "\u001B[1m";

    public static void main(String[] args) {

        String LARANJA = "\u001B[38;5;208m";

        Gato primeiroGato = new Gato();
        Gato seguntoGato = new Gato("Chico", "Laranja", "Vira-lata", 3, 8);

        System.out.println(NEGRITO + "Gatos" + RESET);
        System.out.println(LARANJA + "Primeiro gato: " + RESET + "\n" + primeiroGato + "\n");
        System.out.println(LARANJA + "Segundo gato: " + RESET + "\n" + seguntoGato + "\n");

        Cachorro primeiroCachorro = new Cachorro();
        Cachorro segundoCachorro = new Cachorro("Luna", "Pastora Alemã", 5, 20.8, true);

        System.out.println(NEGRITO + "Cachorros" + RESET);
        System.out.println(VERDE + "Primeiro cachorro: " + RESET + "\n" + primeiroCachorro + "\n");
        System.out.println(VERDE + "Segundo cachorro: " + RESET + "\n" + segundoCachorro + "\n");

        Passaro primeiroPassaro = new Passaro();
        Passaro segundoPassaro = new Passaro("Papagaio", "Verde", 35, 400, true);

        System.out.println(NEGRITO + "Pássaros" + RESET);
        System.out.println(AZUL + "Primeiro pássaro: " + RESET + "\n" + primeiroPassaro + "\n");
        System.out.println(AZUL + "Segundo pássaro: " + RESET + "\n" + segundoCachorro + "\n");

    }

}
