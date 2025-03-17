 import * as readline from 'readline';const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.question("digite um numero: ", function (num1: string) {
    rl.question("digite outro numero: ", function (num2: string) {
        var soma = parseInt(num1) + parseInt(num2);
        console.log("a soma dos dois numeros é: " + soma);
    });
});