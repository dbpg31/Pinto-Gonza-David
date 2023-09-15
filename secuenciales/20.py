import os
os.system("cls")

dinero = int( input("monto de dinero = S/ "))

if dinero >= 200 :
    nbilletes=dinero // 200
    print(f"billetes de 200 = {nbilletes:.2f}")
    dinero = dinero % 200
if dinero >= 100 :
    nbilletes=dinero // 200
    print(f"billetes de 100 = {nbilletes:.2f}")
    dinero = dinero % 100
if dinero >= 50 :
    nbilletes=dinero // 50
    print(f"billetes de 50 = {nbilletes:.2f}")
    dinero = dinero % 50
if dinero >= 20 :
    nbilletes=dinero // 20
    print(f"billetes de 20 = {nbilletes:.2f}")
    dinero = dinero % 20
if dinero >= 10 :
    nbilletes=dinero // 10
    print(f"billetes de 10 = {nbilletes:.2f}")
    dinero = dinero % 10
if dinero >= 5 :
    nbilletes=dinero // 5
    print(f"moneda de 5 = {nbilletes:.2f}")
    dinero = dinero % 5
if dinero >= 2 :
    nbilletes=dinero // 2
    print(f"moneda de 2 = {nbilletes:.2f}")
    dinero = dinero % 2
if dinero >= 1 :
    nbilletes=dinero // 1
    print(f"moneda de 1 = {nbilletes:.2f}")
    dinero = dinero % 1

""" intento de lista
dinero = int( input("monto de dinero = S/ "))
lista = [200,100,50,20,10,5,2,1]
for N in lista:
    if dinero >= N:
        nbilletes=dinero // N
    print(f"cantidad de ('billete' if dinero >= 10 else 'moneda')= {N:.2f}")
    dinero = dinero % N"""





public class DescomposicionDinero {
    public static void main(String[] args) {
        double cantidadDinero = 567.50; // Ingresar la cantidad de dinero en soles

        int billetes200 = (int) (cantidadDinero / 200);
        cantidadDinero %= 200;

        int billetes100 = (int) (cantidadDinero / 100);
        cantidadDinero %= 100;

        int billetes50 = (int) (cantidadDinero / 50);
        cantidadDinero %= 50;

        int billetes20 = (int) (cantidadDinero / 20);
        cantidadDinero %= 20;

        int billetes10 = (int) (cantidadDinero / 10);
        cantidadDinero %= 10;

        int monedas5 = (int) (cantidadDinero / 5);
        cantidadDinero %= 5;

        int monedas2 = (int) (cantidadDinero / 2);
        cantidadDinero %= 2;

        int monedas1 = (int) (cantidadDinero / 1);
        cantidadDinero %= 1;

        System.out.println("Billetes de 200 soles: " + billetes200);
        System.out.println("Billetes de 100 soles: " + billetes100);
        System.out.println("Billetes de 50 soles: " + billetes50);
        System.out.println("Billetes de 20 soles: " + billetes20);
        System.out.println("Billetes de 10 soles: " + billetes10);
        System.out.println("Monedas de 5 soles: " + monedas5);
        System.out.println("Monedas de 2 soles: " + monedas2);
        System.out.println("Monedas de 1 sol: " + monedas1);
    }
}