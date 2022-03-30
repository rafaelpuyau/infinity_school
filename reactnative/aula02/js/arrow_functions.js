// Função convencional
let saudacao = function () {
    return 'Olá, Mundo!';
}

console.log(saudacao())

// Com Arrow function
let saudacao2 = () => {
    return 'Olá, Mundo da Arrow Function!';
}

console.log(saudacao2())

// Arrow Function com apenas um único comando
let saudacao3 = () => 'Olá Mundo com um único parâmetro!';

console.log(saudacao3())