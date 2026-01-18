package Atividades.Polimorfismo;

public class Animal {

    protected String nome;
    protected String raca;
    protected String cor;
    protected int idade;
    protected double peso;

    public Animal(String nome, String raca, String cor, int idade, double peso){

        this.nome = nome;
        this.raca = raca;
        this.cor = cor;
        this.idade = idade;
        this.peso = peso;

    }

    public Animal(){

        this.nome = "";
        this.raca = "";
        this.cor = "";
        this.idade = 0;
        this.peso = 0.0;

    }

    public void comer(){

        System.out.println(nome + "está comendo.");

    }

    public void fazerBarulho(){

        System.out.println("???");

    }

    public void exclusivoAnimal(Animal a) {

        if (a instanceof Cachorro){

            Cachorro c = (Cachorro) a;
            c.mostrarBarriga();

        } else if (a instanceof Gato){

            Gato c = (Gato) a;
            c.enterrarNecessidadesAreia();

        } else if (a instanceof Passaro){

            Passaro p = (Passaro) a;
            p.voar();

        }
    }
}
