"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var readline = require("readline");
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.question("digite um numero: ", function (num1) {
    rl.question("digite outro numero: ", function (num2) {
        var soma = parseInt(num1) + parseInt(num2);
        console.log("a soma dos dois numeros é: " + soma);
    });
});
