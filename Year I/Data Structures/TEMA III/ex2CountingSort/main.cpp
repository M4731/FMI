#include <iostream>
#include <fstream>

using namespace std;
ifstream f("array.txt");



void display ( int siz, int *a )
{
    for( unsigned i=0; i<siz; i++)
        cout<<a[i]<<" ";
    cout<<endl;
}

void counting_sort ( int *a, int maxim, int siz )
{
    int i;
    int *b = new int[siz];
    int *c = new int[maxim+1];
    for ( i=0; i<=maxim; i++ )
        c[i]=0;
    for ( i=0; i<siz; i++ )
        c[a[i]]++;
    for ( i=1; i<=maxim; i++ )
        c[i] = c[i] + c[i-1];
    for ( i=siz-1; i>=0; i-- ){
        b[c[a[i]]-1] = a[i];
        c[a[i]]--;
    }
    for ( i=0; i<siz; i++ )
        a[i] = b[i];

	delete[]b;
	delete[]c;
}

int main()
{
    int n;
    f >> n;
    int *a = new int[n];
    f >> a[0];
    int maxim = a[0];
    for ( unsigned i=1; i<n; i++ ){
        f >> a[i];
        if ( a[i]>maxim ) maxim = a[i];
    }
    display (n, a);
    counting_sort (a, maxim, n);
    display (n, a);
    return 0;
}
