import "dart:io";

void main() {
  stdout.write("digite um numero: ");
  int? num1 = int.parse(stdin.readLineSync()!);
  stdout.write("digite outro numero: ");
  int? num2 = int.parse(stdin.readLineSync()!);
  print("a soma é ${num1 + num2}");
}
