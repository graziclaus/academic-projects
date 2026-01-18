// Objetivo: calcular a média de notas de um aluno e exibir sua situação
// (Aprovado/Reprovado/Recuperação)
// O aluno estará aprovado se obter a nota 7 ou mais; estará em recuperação se
// obter a nota entre 5 e 6,9 e;
// estará reprovado se obter nota menor que 5

// Código com erros

// function calcularMedia(notas) {
// soma = 0;
// for (let i = 0; i <= notas.length; i++) {
// soma += notas[i];
// }
// media = soma / notas.length;
// return media;
// }
// function verificarSituacao(media) {
// if (media > 7) {
// situacao = "Aprovado";
// } else if (media < 5) {
// situacao = "Reprovado";
// } else {
// situacao = "Recuperação";
// }
// return situacao;
// }
// let notasAluno = [8, 6, 7];
// let mediaFinal = calcularMedia(notasAluno);
// console.log("Média final: " + mediaFinal.toFixed(2));
// console.log("Situação do aluno: " + verificarSituacao(mediaFinal));

// Código corrigido

function calcularMedia(notas) {

    let soma = 0;

    for (let i = 0; i < notas.length; i++) {

        soma += notas[i];

    }

    let media = soma / notas.length;
    return media;
}

function verificarSituacao(media) {

    let situacao = "";

    if (media >= 7) {

        situacao = "Aprovado";

    } else if (media < 5) {

        situacao = "Reprovado";

    } else {

        situacao = "Recuperação";

    }

    return situacao;
}

let notasAluno = [8, 6, 7];
let mediaFinal = calcularMedia(notasAluno);
console.log("Média final: " + mediaFinal.toFixed(2));
console.log("Situação do aluno: " + verificarSituacao(mediaFinal));