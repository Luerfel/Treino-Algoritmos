#include <iostream>
using namespace std;

class Carro {
public:
    string marca;
    string modelo;
    int ano;

    void mostrarDetalhes() {
        cout << "Marca: " << marca << ", Modelo: " << modelo << ", Ano: " << ano << endl;
    }
};

int main() {
    Carro meuCarro; // Criando um objeto da classe Carro
    meuCarro.marca = "Toyota";
    meuCarro.modelo = "Corolla";
    meuCarro.ano = 2020;
    meuCarro.mostrarDetalhes();

    return 0;
}
