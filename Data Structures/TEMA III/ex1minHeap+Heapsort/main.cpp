#include <iostream>
#include <fstream>

using namespace std;

ifstream f("array.txt");
int size, a[21];

void swap (int &a, int &b)
{
    int aux;
    aux = a;
    a = b;
    b = aux;
}

void reading ()
{
    unsigned x;
    while(f>>x){
        a[size] = x;
        size++;
    }
}

int left (int i)
{
    return 2*i+1;
}

int right (int i)
{
    return 2*i+2;
}

int parent (int i)
{
    return (i-1)/2;
}

void min_heapify (int i, int siz)
{
    int smallest;
    int l=left(i), r=right(i);
    if ( l<siz && a[l] < a[i] )
        smallest = l;
    else smallest = i;
    if ( r<siz && a[r] < a[smallest] )
        smallest = r;
    if ( smallest != i ){
        swap (a[i], a[smallest]);
        min_heapify(smallest,siz);
    }
}

void build_min_heap ()
{
    for ( auto i=(size-1)/2; i>=0; i-- )
        min_heapify(i, size);
}

int extract ()
{
    int returnare;
    if (!size){
        cout<<"Can't exctract.";
        return -43212;
    }
    else{
        returnare = a[0];
        a[0] = a[size-1];
        size--;
        min_heapify(0,size);
        return returnare;
    }
}

void insert (int x)
{
    size++;
    a[size-1]=x;
    int pozitie = size-1;
    while ( parent(pozitie) >= 0 && a[parent(pozitie)] > a[pozitie] ){
        swap ( a[pozitie], a[parent(pozitie)] );
        pozitie = parent(pozitie);
    }
}

void display ()
{
    for( auto i=0; i<size; i++)
        cout<<a[i]<<" ";
    cout<<endl;
}

int heapsort ()
{
    build_min_heap ();
    int length = size;
    for ( auto i=size-1; i>=0; i-- ){
        swap( a[i], a[0] );
        length--;
        min_heapify (0, length);
    }
 	for (auto i=0; i<size/2; i++)
		swap( a[i], a[size-i-1] );
}

int main()
{
    reading();
    cout<<size<<endl;
    display();
    build_min_heap();
    display();
    insert(22);extract();
    display();
    heapsort();
    display();
    insert(-22);insert(23212);insert(-1);
    heapsort();
    display();
}
