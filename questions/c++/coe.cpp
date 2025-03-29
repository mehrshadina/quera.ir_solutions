#include <iostream>
#include <sstream>
#include <bitset>
#include <vector>
#include <string>
#include <iostream>
#include <string>
using namespace std;

int main() {

    int n=10;

    int *p=new int[n];
    for ( int i=0 ; i<n ; i++ )
    {
        p[i]=i*10;
    }
    for ( int i=0 ; i<n ; i++ )
    {
        cout<< *( p+ i )<<"     ";
    }
    cout <<p<<endl;

    delete p;

     for ( int i=0 ; i<n ; i++ )
    {
        p[i]=i*10;
    }

     for ( int i=0 ; i<n ; i++ )
    {
        cout<< *( p+ i )<<"     ";
    }
    cout<<p<<endl;

    return 0;
}