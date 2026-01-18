package Atividades.HerancaAtividade;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Jogador extends Personagem{

    // A barra de fome tem (20) pontos no total.
    private int fome;
    private Ferramenta ferramentaEquipada;
    private Armadura armaduraEquipada;
    private String modoDeJogo;
    public static Scanner scanner = new Scanner(System.in);
    public static Random random = new Random();

    // Notas: A fome afeta tanto a vida, dano e a sua defesa aqui, dependendo do quanto está a fome
    // As três coisas podem diminuir. Isso é para substituir o velocidade do jogador já que não sei como seria feito aqui
    // então decidi colocar isso e dificultar um pouco. Dar dano diminui a fome também.

    // Estou pensando na parte:
    // Fazer um recorte que será implementado (ex: perspectiva do usuário/ perspectiva do admin)
    // A parte de admin seria aqueles que possuem o modo criativo, enquanto o survival teria o modo usuário

    public Jogador(String nome, int coracoes, int dano, int armadura, int xp, String modoDeJogo) {

        super(nome, coracoes, dano, armadura, xp);
        this.fome = 20;
        this.ferramentaEquipada = null;
        this.modoDeJogo = modoDeJogo;
        this.armaduraEquipada = null;

    }

    // --------------------------------------------------- Defensividade ---------------------------------------------------

    public void equiparFerramenta(Ferramenta ferramenta){

        this.ferramentaEquipada = ferramenta;
        System.out.println(getNome() + " equipou " + ferramenta.getNome() + ". A ferramenta possui " + ferramenta.getDano());

    }

    public void equiparArmadura(Armadura armadura){

        this.armaduraEquipada = armadura;
        System.out.println(getNome() + " equipou " + armadura.getNome() + ". Defesa: " + armadura.getDefesa());

    }

    // --------------------------------------------------- Fome ---------------------------------------------------


    public double multiplicadorFome(){

        if (isModoCriativo()) { return 1.0; }
        else if (fome >= 15){ return 1.0;}
        else if(fome >= 10){ return 0.9; }
        else if(fome >= 5) { return 0.7; }
        else if(fome >= 1) { return 0.5; }
        else { return 0.3; }

    }

    public void gastarFome(int quantidade) {

        if (isModoCriativo()) { return; }
        fome -= quantidade;
        if(fome < 0) { fome = 0; }
        System.out.println("Opa! " + getNome() + " perdeu " + quantidade + " de fome. Fome atual: " + fome);

    }

    public void recuperarFome() {

        fome = 20;
        System.out.println(getNome() + " recuperou toda a fome! Fome atual: " + fome);

    }

    public void restaurarVida() {

        int vidaMax = 20;
        super.setCoracoes(vidaMax);
        System.out.println(getNome() + " recuperou toda a vida! Vida atual: " + getCoracoes());

    }

    // --------------------------------------------------- || ---------------------------------------------------

    // --------------------------------------------------- Ofensividade ---------------------------------------------------

    public void atacar(Personagem alvo) {

        int danoBase = getDano();

        if (ferramentaEquipada != null) {

            if (ferramentaEquipada.getDurabilidade() > 0) {

                danoBase += ferramentaEquipada.getDano();
                ferramentaEquipada.usar();

            } else {

                System.out.println(ferramentaEquipada.getNome() + " quebrou!");
                ferramentaEquipada = null;
            }
        }

        int danoFinal = (int)(danoBase * multiplicadorFome());
        //??????????????
        if(danoFinal < 1) { danoFinal = 1; }

        System.out.println(getNome() + " atacou " + alvo.getNome() + " causando " + danoFinal + " de dano! (Fome: " + fome + ")");
        alvo.receberDano(danoFinal, this);
        gastarFome(1);

    }

    @Override
    public void receberDano(int danoRecebido, Personagem atacante) {

        if (isModoCriativo()) {

            System.out.println(getNome() + " está no modo criativo e não sofre dano!");
            return;

        }

        int defesa = 0;

        if (armaduraEquipada != null) {

            if (armaduraEquipada.getDurabilidade() > 0) {

                defesa = armaduraEquipada.getDefesa();

            } else {

                System.out.println(armaduraEquipada.getNome() + " quebrou!");
                armaduraEquipada = null;
            }
        }

        int danoFinal = danoRecebido - defesa;
        if (danoFinal < 0) { danoFinal = 0; }

        super.receberDano(danoFinal, atacante);

        if (atacante != null && atacante != this) {

            System.out.println(getNome() + " recebeu " + danoFinal + " de dano de " + atacante.getNome() + ". Vida atual: " + getCoracoes());

        }

        if (fome <= 0 && getCoracoes() > 0) {

            super.setCoracoes(super.getCoracoes() - 1);
            System.out.println("Você está morrendo de fome e perdeu 1 de vida extra!");

        }

        if (ferramentaEquipada != null && ferramentaEquipada.getDurabilidade() <= 0) {


            System.out.println(ferramentaEquipada.getNome() + " quebrou!");
            ferramentaEquipada = null;

        }

        if (armaduraEquipada != null && armaduraEquipada.getDurabilidade() <= 0) {

            System.out.println(armaduraEquipada.getNome() + " quebrou!");
            armaduraEquipada = null;

        }
    }

    // --------------------------------------------------- Opções menu ---------------------------------------------------
    public void farmar() {

        final String RESET = "\u001B[0m";
        final String GREEN = "\u001B[32m";
        final String GRAY = "\u001B[37m";
        final String YELLOW = "\u001B[33m";

        if (isModoCriativo()) {
            System.out.println(YELLOW + "✨ Modo Criativo: você coletou recursos infinitos! ✨" + RESET);

            adicionarItem(new Item("Pedra", 999, 64));
            adicionarItem(new Item("Madeira", 999, 64));

            System.out.println(GRAY + "🗿 +999 Pedras" + RESET);
            System.out.println(GREEN + "🌳 +999 Madeiras" + RESET);

        } else {

            System.out.println(GRAY + "⛏️ Você minerou 10 pedras e coletou 15 madeiras!" + RESET);

            adicionarItem(new Item("Pedra", 10, 64));
            adicionarItem(new Item("Madeira", 15, 64));

            System.out.println(GRAY + "🗿 +10 Pedras" + RESET);
            System.out.println(GREEN + "🌳 +15 Madeiras" + RESET);

            gastarFome(1);
        }
    }

    public void plantar() {

        if (isModoCriativo()) {

            System.out.println("Modo Criativo: você plantou sementes sem gastar nada!");
            mostrarHorta();
            return;

        }

        int qtdSementes = contarItem("Semente");

        if (qtdSementes > 0) {

            System.out.println("Você plantou sementes!");
            mostrarHorta();


        } else {

            System.out.println("Você não tem sementes! Explore para encontrar.");

        }
    }

    public void mostrarCasa(){

        System.out.println("Você construiu sua casa!");

        System.out.println("\n      🏠 Sua casa 🏠\n");
        System.out.println("/\\\n" +
                "                              /\\  //\\\\\n" +
                "                       /\\    //\\\\///\\\\\\        /\\\n" +
                "                      //\\\\  ///\\////\\\\\\\\  /\\  //\\\\\n" +
                "         /\\          /  ^ \\/^ ^/^  ^  ^ \\/^ \\/  ^ \\\n" +
                "        / ^\\    /\\  / ^   /  ^/ ^ ^ ^   ^\\ ^/  ^^  \\\n" +
                "       /^   \\  / ^\\/ ^ ^   ^ / ^  ^    ^  \\/ ^   ^  \\       *\n" +
                "      /  ^ ^ \\/^  ^\\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \\     /|\\\n" +
                "     / ^ ^  ^ \\ ^  _\\___________________|  |_____^ ^  \\   /||o\\\n" +
                "    / ^^  ^ ^ ^\\  /______________________________\\ ^ ^ \\ /|o|||\\\n" +
                "   /  ^  ^^ ^ ^  /________________________________\\  ^  /|||||o|\\\n" +
                "  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\\\n" +
                " / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |\n" +
                "/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo\n" +
                "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo");

    }

    public void mostrarHorta(){

        final String RESET = "\u001B[0m";
        final String GREEN = "\u001B[32m";
        final String BROWN = "\u001B[33m";

        System.out.println(GREEN + "🌱 Sua mini horta está assim: " + RESET);

        System.out.println(BROWN + "============================" + RESET);
        System.out.println(BROWN + "|| " + GREEN + "🌱 🌱 🌱 🌱 🌱" + BROWN + " ||" + RESET);
        System.out.println(BROWN + "|| " + GREEN + "🌾 🥕 🌾 🥕 🌾" + BROWN + " ||" + RESET);
        System.out.println(BROWN + "|| " + GREEN + "🌱 🌾 🌱 🥕 🌱" + BROWN + " ||" + RESET);
        System.out.println(BROWN + "============================" + RESET);

        System.out.println(GREEN + "As plantas estão crescendo... ⏳" + RESET);
        removerItem("Semente", 1);
        gastarFome(1);

    }

    public void construirCasa() {

        if (isModoCriativo()) {

            System.out.println("Você construiu a casa no modo criativo! 🏠");
            mostrarCasa();
            return;

        }

        int quantidadeMadeira = contarItem("Madeira");
        int quantidadePedra = contarItem("Pedra");

        if (quantidadeMadeira >= 40 && quantidadePedra >= 20) {

            removerItem("Madeira", 40);
            removerItem("Pedra", 20);
            mostrarCasa();

        } else {

            System.out.println("Você não tem recursos suficientes para construir a casa (40 madeiras e 20 pedras)!");
        }
    }

    public void explorar() {

        final String RESET = "\u001B[0m";
        final String RED = "\u001B[31m";
        final String GREEN = "\u001B[32m";
        final String CYAN = "\u001B[36m";
        final String YELLOW = "\u001B[33m";
        final String PURPLE = "\u001B[35m";

        System.out.println(CYAN + "1 - Derrotar mobs | 2 - Explorar biomas" + RESET);
        int escolha = scanner.nextInt();

        if (escolha == 1) {

            if (isModoCriativo()) {

                System.out.println(GREEN + "✨ Modo Criativo: você derrota todos os mobs instantaneamente! ✨" + RESET);
                return;
            }

            MobOfensivo[] mobs = {

                    new MobOfensivo("Zumbi 🧟", 20, 3, 0, 5, new Item("Carne Podre", 1, 64)),
                    new MobOfensivo("Esqueleto 💀", 15, 4, 0, 7, new Item("Osso", 1, 64)),
                    new MobOfensivo("Aranha 🕷️", 12, 3, 0, 6, new Item("Fio", 1, 64))

            };

            MobOfensivo mob = mobs[random.nextInt(mobs.length)];
            System.out.println(RED + "⚠️ Você encontrou um " + mob.getNome() + "! Prepare-se para o combate!" + RESET);

            while (mob.getCoracoes() > 0 && this.getCoracoes() > 0) {

                try {

                    Thread.sleep(1000);

                } catch (InterruptedException e) {

                    e.printStackTrace();
                }

                System.out.println(PURPLE + "\n👉 Sua vez de atacar!" + RESET);
                this.atacar(mob);

                if (mob.getCoracoes() > 0) {

                    try {

                        Thread.sleep(5000);

                    } catch (InterruptedException e) {

                        e.printStackTrace();
                    }

                    System.out.println(RED + mob.getNome() + " contra-ataca!" + RESET);
                    mob.atacar(this);
                }

                System.out.println(YELLOW + "\n❤️ Vida Atual: " + getNome() + " = " + getCoracoes() + " | "
                        + mob.getNome() + " = " + mob.getCoracoes() + RESET);
            }

            if (getCoracoes() > 0 && mob.getDrop() != null) {

                System.out.println(GREEN + " Você derrotou o " + mob.getNome() + " e recebeu: " + mob.getDrop().getNome() + "!" + RESET);
                adicionarItem(mob.getDrop());
                gastarFome(2);

            } else if (getCoracoes() <= 0) {

                System.out.println(RED + "💀 Você morreu! Tente novamente..." + RESET);
            }

        } else if (escolha == 2) {

            if (isModoCriativo()) {

                System.out.println(GREEN + "🌍 Modo Criativo: você coleta todos os recursos automaticamente!" + RESET);
                adicionarItem(new Item("Madeira", 999, 64));
                adicionarItem(new Item("Pedra", 999, 64));
                adicionarItem(new Item("Semente", 999, 64));
                return;

            }

            int madeira = random.nextInt(31);
            int pedra = random.nextInt(31);
            int sementes = random.nextInt(31);

            System.out.println(GREEN + "🌿 Você explorou o bioma e encontrou: " + madeira + " madeiras, " +
                    pedra + " pedras, " + sementes + " sementes." + RESET);

            if (madeira > 0) { this.adicionarItem(new Item("Madeira", madeira, 64)); }
            if (pedra > 0) { this.adicionarItem(new Item("Pedra", pedra, 64)); }
            if (sementes > 0) { this.adicionarItem(new Item("Semente", sementes, 64)); }

            if (random.nextInt(100) < 70) {

                MobInofensivo[] mobsInofensivos = {

                        new MobInofensivo("Porco 🐖", 10, 0, 0, 2, new Item("Carne de Porco", 2, 64)),
                        new MobInofensivo("Galinha 🐔", 5, 0, 0, 2, new Item("Frango", 2, 64)),
                        new MobInofensivo("Vaca 🐄", 20, 0, 0, 5, new Item("Carne de Vaca", 2, 64)),
                        new MobInofensivo("Ovelha 🐑", 20, 0, 0, 5, new Item("Lã", 3, 64))

                };

                MobInofensivo mobEncontrado = mobsInofensivos[random.nextInt(mobsInofensivos.length)];

                try {

                    Thread.sleep(1500);

                } catch (InterruptedException e) {

                    e.printStackTrace();
                }

                System.out.println(YELLOW + "✨ Você encontrou um " + mobEncontrado.getNome() + "!" + RESET);
                System.out.println(RED + "⚡ Você derrotou o " + mobEncontrado.getNome() + " instantaneamente!" + RESET);

                this.adicionarItem(mobEncontrado.getDrop());
                System.out.println(GREEN + "🎁 Você recebeu: " + mobEncontrado.getDrop().getNome() + RESET);
            }

            this.gastarFome(2);
        }
    }

    public void dormir() {

        int qtdLa = contarItem("Lã");
        int qtdMadeira = contarItem("Madeira");

        if (qtdLa >= 3 && qtdMadeira >= 3) {

            System.out.println("🛏️ Você deitou para dormir...");

            try {

                for (int i = 0; i < 5; i++) {
                    Thread.sleep(800); // espera 0.8s
                    System.out.print("Z..");
                    Thread.sleep(500);
                    System.out.print(".. z ...");
                    Thread.sleep(500);
                    System.out.print("Z... ");
                }

                System.out.println();

            } catch (InterruptedException e) {

                e.printStackTrace();

            }

            System.out.println("☀️ Você acordou descansado e passou o dia!");
            removerItem("Lã", 3);
            removerItem("Madeira", 3);
            restaurarVida();
            recuperarFome();

        } else {

            System.out.println("⚠️ Você precisa de 3 Lãs e 3 Madeiras para dormir!");

        }
    }

    public void mostrarInventario() {

        ArrayList<Item> inventario = getInventario();
        int totalSlots = 27;
        int colunas = 9;

        String RESET = "\u001B[0m";
        String VERDE = "\u001B[32m";
        String MARROM = "\u001B[33m";
        String CINZA = "\u001B[37m";
        String AZUL = "\u001B[34m";
        String VERMELHO = "\u001B[31m";

        System.out.print("❤ Vida: ");
        for (int i = 0; i < getCoracoes(); i++) {
            System.out.print("❤");
        }
        System.out.println();

        System.out.print("🍗 Fome: ");
        for (int i = 0; i < fome; i++) {
            System.out.print("🍗");
        }
        System.out.println("\n");

        System.out.println("--- Inventário ---");

        for (int i = 0; i < totalSlots; i++) {
            if (i < inventario.size()) {
                Item item = inventario.get(i);
                String cor = RESET;

                switch (item.getNome().toLowerCase()) {
                    case "semente": cor = VERDE; break;
                    case "madeira": cor = MARROM; break;
                    case "pedra": cor = CINZA; break;
                    case "picareta": cor = AZUL; break;
                    case "carne podre":
                    case "osso":
                    case "fio": cor = VERMELHO; break;
                    default: cor = RESET; break;
                }

                System.out.printf("%s[%s x%d]%s ", cor, item.getNome(), item.getQuantidade(), RESET);

            } else {
                System.out.print("[Vazio] ");
            }

            if ((i + 1) % colunas == 0) {
                System.out.println();
            }
        }
        System.out.println("-----------------\n");

    }

    public void adicionarItem(Item novoItem) {

        for (Item item : getInventario()) {

            if (item.getNome().equalsIgnoreCase(novoItem.getNome())) {

                item.setQuantidade(item.getQuantidade() + novoItem.getQuantidade());

                return;
            }
        }

        getInventario().add(novoItem);
    }

    public int contarItem(String nome) {

        int total = 0;
        for(Item i : getInventario()) {

            if(i.getNome().equalsIgnoreCase(nome)) {

                total += i.getQuantidade();

            }
        }

        return total;
    }

    public void removerItem(String nomeItem, int quantidade) {

        for (int i = 0; i < getInventario().size(); i++) {

            Item item = getInventario().get(i);

            if (item.getNome().equalsIgnoreCase(nomeItem)) {

                int novaQuantidade = item.getQuantidade() - quantidade;

                if (novaQuantidade > 0) {

                    item.setQuantidade(novaQuantidade);

                } else {

                    getInventario().remove(i);

                }

                System.out.println("Removido " + quantidade + "x " + nomeItem + " do inventário.");
                return;
            }
        }

        System.out.println("Item " + nomeItem + " não encontrado no inventário!");
    }

    public boolean isModoCriativo() { return modoDeJogo.equals("criativo"); }

    public String getModoDeJogo(){ return modoDeJogo; }
    public void setModoDeJogo(String modoDeJogo) { this.modoDeJogo = modoDeJogo; }
    // public boolean isModoSobrevivencia() { return modoDeJogo.equals("survival"); }

}