// Declaração de variáveis

// Tipos primitivos

// boolean
var vouf = false;
console.log(typeof(vouf));

// var numero
var numeroQualquer = 1;
console.log(typeof(numeroQualquer));

// string
var nome = "igor";
console.log(typeof("igor"));

// como declarar
var variavel = 'xyz';
variavel = "alpha"
console.log(variavel);

let variavel2 = 'xyz2';
variavel2 = 'beta';
console.log(variavel2);

// Constante. Não pode ser alterada. Dará erro.
const constante = "xyz3";
// constante = "delta"; // assim fica com erro pois não pode redefinir uma constante. Apagar.
console.log(constante);

var escopoGlobal = 'global';
console.log(escopoGlobal);

function escopoLocal() {
    let escopoLocalInterno = 'Local';
    console.log(escopoLocalInterno);
}
escopoLocal();

// atribuição
var atribuicao = 'igor';

//comparação
var comparacao = '0' == 0; 
console.log(comparacao);

var comparacaoIdentica = '0' === 0; 
console.log(comparacaoIdentica);

// operadores aritméticos
// adição
var adicao = 1 + 1;
console.log(adicao);
//subtração
var subtracao = 2 - 1;
console.log(subtracao);
//multiplicação
var multiplicacao = 2 * 3;
console.log(multiplicacao);
//divisão real
var divisaoReal = 6 / 2;
console.log(divisaoReal);
//divisão inteira. É o resto da divisão.
var divisaoInteira = 5 % 2;
console.log(divisaoInteira);;
//potenciação
var potenciacao = 2**10;
console.log(potenciacao);

// operadores relacionais
// maior que
var maiorQue = 5 > 2;
console.log(maiorQue);
        
// menor que
var menorQue = 5 < 2;
console.log(menorQue);
      
// maior ou igual a
var maiorOuIgual = 5 >= 2;
console.log(maiorOuIgual);
    
// menor ou igual a
var menorOuIgual = 5 <= 2;
console.log(menorOuIgual);

// operadores lógicos
// && - todos os valores devem ser true
var e = true && true;
console.log(e);
// || - somente um valor deve ser true
var ou = true || false;
console.log(ou);
// ! - inverte os valores
var nao = !true;
console.log(nao);