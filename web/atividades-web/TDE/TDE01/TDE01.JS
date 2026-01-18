// • Criar funções que realizem operações básicas (soma, subtração, multiplicação, divisão).
// • Implementar uma função que manipule arrays (ex: filtrar números pares, calcular média).
// • Usar arrow functions em pelo menos duas partes do código.
// • Criar uma função que receba outra função como parâmetro (callback).


// --------------------------- Operações básicas --------------------------- \\

function somar(num1, num2) {

    return num1 + num2;

}

function subtrair(num1, num2) {

    return num1 - num2;

}

function multiplicar(num1, num2) {

    return num1 * num2;

}

function dividir(num1, num2) {

    if (num2 === 0) {

        return 'Não pode dividir por zero.';

    }  

    return num1 / num2;
}

// --------------------------- Manipulação de arrays --------------------------- \\

function encontrarMaior(array) {

    let maior = array[0];

    for (let index = 1; index < array.length; index++) {

        if (array[index] > maior) {

            maior = array[index];
        }
    }

    return maior;
}

// --------------------------- Arrow Functions --------------------------- \\


const filtrarPares = (pares) => {

    return pares.filter(num => num % 2 === 0);

};

const calcularMedia = (array) => {
    
    let soma = array.reduce((n, num) => n + num, 0);
    let media = soma / array.length;
    return media.toFixed(2);

};

// --------------------------- Callback --------------------------- \\


function chamarOutraFuncao(a, b, funcao) {

    return funcao(a, b);

}

let numeros = [3, 13, 3, 9, 48, 35, 0, 36, 16, 21, 42];


console.log('//--------- Operações básicas ---------//');
console.log('Soma: ', somar(4, 8));
console.log('Subtração: ', subtrair(6, 13));
console.log('Multiplicação: ', multiplicar(30, 2));
console.log('Divisão: ', dividir(294, 2) + "\n");

console.log('//--------- Manipulação de arrays ---------//');

console.log('Array de números: ', numeros);
console.log('Maior número: ', encontrarMaior(numeros));

console.log('//--------- Arrow Functions ---------//');
console.log('Filtrar um array só por pares. \nNúmeros pares: ', filtrarPares(numeros));
console.log('Média dos números do array: ', calcularMedia(numeros) + "\n");

console.log('//--------- Callback ---------//');
console.log('Callback da função soma:', chamarOutraFuncao(10, 5, somar));