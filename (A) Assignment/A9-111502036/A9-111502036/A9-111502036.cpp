/*
Assignment 9
Name: 沈哲寬
Student Number: 111502036
Course: 2022-CE1001-B
*/
#include<iostream>
using namespace std;
int which_date(int y, int m, int d){
    int c;
    if(m==1){
        m = 11;
        y = y-1;
    }
    else if(m==2){
        m = 12;
        y = y-1;
    }
    else{
        m = m-2;
    }
    c = y/100;
    y = y%100;
    int temp = (2.6*m)-0.2;
    int part1,part2,part3,part4;
    d = d%7;
    part1 = temp%7;
    part2 = ((5*(y%4))%7);
    part3 = ((3*y)%7);
    part4 = ((5*(c%4))%7);
    int w = (d + part1 + part2 +part3+part4)%7;
    return w;
}
void  display_calendar(int y, int m, int d){  
    int t = which_date(y,m,1);
    int day = 0;
    if( m==2 ){
        day = 28;
    }
    else if(m == 1 || 3 || 5 || 7 || 8 || 10 || 12){
        day = 31;
    }
    else{
        day = 30;
    }
    for (int a=0;a<7;a++)
        cout <<"    "<<a;
    cout << endl << "=====================================" << endl;
    int i = 1;
    for(;i<=t;i++){
    cout <<"     ";
    }
    if(i%7==0){
        cout <<'\n';
    }
    for(int c=1;c<=day;c++,i++){
        if(c<10){
            if(c==d){
                cout <<"   *"<<c; 
            }
            else{
                cout <<"    "<<c;
            }
        }
        else{
            if(c==d){
                cout <<"  *"<<c; 
            }
            else{
                cout <<"   "<<c;
            }
        }
        if(i%7==0){
            cout <<'\n';
        }
    }
    cout << endl << "=====================================" << endl;
}
int main(){
    int d,m,y,c;
    cin >> y >> m >>d;
    int w = which_date(y,m,d);
    switch(w){
        case 0:
            cout << "Sunday" <<endl;
            break;
        case 1:
            cout << "Monday" <<endl;
            break;
        case 2:
            cout << "Tuesday" <<endl;
            break;
        case 3:
            cout << "Wednesday" <<endl;
            break;
        case 4:
            cout << "Thursday" <<endl;
            break;
        case 5:
            cout << "Friday" <<endl;
            break;
        case 6:
            cout << "Saturday" <<endl;
            break;
    }
    display_calendar( y,  m,  d);
}