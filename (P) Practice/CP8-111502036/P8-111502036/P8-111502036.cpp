/*
Practice 8 C++
Name: 沈哲寬
Student Number: 111502036
Course 2022-CE1003-B
*/
#include<iostream>
using namespace std;
int gcd(int a, int b){
    if(b==0){
        return a;
    }
    return gcd(b,a%b);
}
int main(){
    int number1,number2;
    cin >> number1 >> number2;
    cout << gcd(number1,number2)<<endl;
}