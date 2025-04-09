import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Digite algo: ', (variavel: string) => {
    console.log('O tipo primitivo desse valor é', typeof variavel);
    console.log('Só tem espaços?', /^\s*$/.test(variavel));
    console.log('É um numero?', !isNaN(Number(variavel)));
    console.log('É alfabético?', /^[a-zA-Z]+$/.test(variavel));
    console.log('É alfanumérico?', /^[a-zA-Z0-9]+$/.test(variavel));
    console.log('Está em maiúsculas?', variavel === variavel.toUpperCase());
    console.log('Está em minúsculas?', variavel === variavel.toLowerCase());
    console.log('Está capitalizada?', variavel.charAt(0) === variavel.charAt(0).toUpperCase() && variavel.slice(1) === variavel.slice(1).toLowerCase());
    
    rl.close();
});

