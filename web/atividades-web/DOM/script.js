/*Insira uma função auto-invocada que simule a busca do seu nome em um banco de dados.
Isso quer dizer: quando visualizarmos o HTML no navegador, irá aparecer
no canto superior direito "Bem-vindo(a), <seu_nome>.".
Tente fazer isso com o querySelector que vimos hoje.
Na sequência, armazene o nome em uma variável (caso você não tenha feito isso anteriormente.
Por fim, verifique se há um nome armazenado nessa variável, havendo, apresente: "Bem-vindo(a), <seu_nome>.".
Senão, esconda o "Bem-vindo(a),"*/


(function() {

    const nome = "Grazi"; 

    if (nome) {

        document.querySelector(".top-bar p").textContent = "Bem-vindo(a), ${nome}.";

    } else {

        document.querySelector(".top-bar p").style.display = "none";

    }

})();