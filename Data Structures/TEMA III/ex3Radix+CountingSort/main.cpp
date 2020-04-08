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

void counting_sort ( int *a, int siz, int e )
{
    int i;
    int *b = new int[siz];
    int *c = new int[10];
    for ( i=0; i<=9; i++ )
        c[i]=0;
    for ( i=0; i<siz; i++ )
        c[a[i]/e%10]++;
    for ( i=1; i<=9; i++ )
        c[i] = c[i] + c[i-1];
    for ( i=siz-1; i>=0; i-- ){
        b[c[a[i]/e%10]-1] = a[i];
        c[a[i]/e%10]--;
    }
    for ( i=0; i<siz; i++ )
        a[i] = b[i];

	delete[]b;
	delete[]c;
}

void radix_sort(int *a, int siz, int maxim) {
	for ( unsigned e=1; maxim/e>0; e*=10) {
		counting_sort(a, siz, e);
	}
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
    radix_sort (a, n, maxim);
    display (n, a);
    return 0;
}
