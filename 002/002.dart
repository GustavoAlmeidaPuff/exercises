import 'dart:io';

void main() {
  stdout.write('Digite seu nome: ');
  String? nome = stdin.readLineSync();
  print("prazer em conhece-lo $nome");
}
