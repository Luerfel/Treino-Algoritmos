#include <iostream>

using namespace std;

bool isPalindrome(int num) {
    if (num < 0) {
        return false; // Números negativos não são palíndromos
    }
    
    int original = num;
    int reversed = 0;
    
    while (num > 0) {
        int digito = num % 10;
        reversed = reversed * 10 + digito;
        num /= 10;
    }
    
    // Verificando se o número original é igual ao número invertido
    return original == reversed;
}

int main() {
    int num = 121;
    
    if (isPalindrome(num)) {
        cout << num << " é um número palíndromo." << endl;
    } else {
        cout << num << " não é um número palíndromo." << endl;
    }
    
    return 0;
}
