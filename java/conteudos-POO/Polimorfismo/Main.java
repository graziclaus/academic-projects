package Atividades.Polimorfismo;

public class Main {

    public static void main(String[] args) {

        Animal a = new Animal();

        Animal c = new Cachorro();
        Animal g = new Gato();
        Animal p = new Passaro();

        a.exclusivoAnimal(c);
        a.exclusivoAnimal(g);
        a.exclusivoAnimal(p);

        c.fazerBarulho();
        g.fazerBarulho();
        p.fazerBarulho();

    }
}
