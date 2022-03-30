// Função convencional com parâmetros
let saudacao = function (usuario) {
    return `Olá, ${usuario}`;
}

console.log(saudacao("Rafael"))

// Arrow function com parâmetros
let saudacao2 = (usuario) => {
    return `Olá, ${usuario}`;
}

console.log(saudacao2("Puyau"))

// Ou 

let saudacao3 = usuario => `Olá, ${usuario}`;

console.log(saudacao3("Rafael Puyau"))