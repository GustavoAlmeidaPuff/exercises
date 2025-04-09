import "dart:io";

void main() {
  stdout.write("Digite algo: ");
  String? input = stdin.readLineSync();
  print("O tipo primitivo desse valor é ${input.runtimeType}");
  print("Só tem espaços? ${input!.isEmpty}");
  print("É um numero? ${input.contains(RegExp(r'^\d+$'))}");
  print("É alfabético? ${input.contains(RegExp(r'^[a-zA-Z]+$'))}");
  print("É alfanumérico? ${input.contains(RegExp(r'^[a-zA-Z0-9]+$'))}");
  print("Está em maiúsculas? ${input == input.toUpperCase()}");
  print("Está em minúsculas? ${input == input.toLowerCase()}");
  print(
    "Está capitalizada? ${input.startsWith(input[0]) && input.substring(1) == input.substring(1).toLowerCase()}",
  );
}
