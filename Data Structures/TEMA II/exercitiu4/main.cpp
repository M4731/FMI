#include <iostream>
#include <fstream>

using namespace std;
ifstream f("exercitiu4matrice.txt");

struct coada{
    int info;
    coada * prev, * next;
}*pointer_global_prim_element,
*pointer_global_ultim_element;

void push_right( int x )
{
    coada * s = new coada;
    if (!pointer_global_prim_element)
    {
        pointer_global_ultim_element = s;
        pointer_global_ultim_element->info = x;
        pointer_global_ultim_element->next = NULL;
        pointer_global_ultim_element->prev = NULL;
        pointer_global_prim_element = pointer_global_ultim_element;
    }
    else if(pointer_global_prim_element == pointer_global_ultim_element)
    {
        pointer_global_prim_element->next = s;
        s->prev = pointer_global_prim_element;
        s->info = x;
        s->next = NULL;
        pointer_global_ultim_element = s;

    }
    else
    {
        pointer_global_ultim_element->next = s;
        s->info = x;
        s->prev = pointer_global_ultim_element;
        s-> next = NULL;
        pointer_global_ultim_element = s;
    }
}

void push_left( int x )
{
    if (!pointer_global_prim_element)
    {
        coada * s = new coada;
        pointer_global_prim_element = s;
        pointer_global_prim_element->info = x;
        pointer_global_prim_element->next = NULL;
        pointer_global_prim_element->prev = NULL;
        pointer_global_ultim_element = pointer_global_prim_element;
    }
    else if(pointer_global_prim_element == pointer_global_ultim_element)
    {
        coada * s = new coada;
        pointer_global_prim_element->prev = s;
        s->next = pointer_global_prim_element;
        s->info = x;
        s->prev = NULL;
        pointer_global_prim_element = s;
    }
    else
    {
        coada * s = new coada;
        pointer_global_prim_element->prev = s;
        s->next = pointer_global_prim_element;
        s->info = x;
        s->prev = NULL;
        pointer_global_prim_element = s;
    }
}

int pop_left()
{
    if (!pointer_global_prim_element) {
       // cout<<"coada goala.";
        return -1;
    }
    else if(pointer_global_prim_element == pointer_global_ultim_element)
    {
        int q = pointer_global_prim_element->info;
        coada * s = pointer_global_prim_element;
        pointer_global_prim_element = NULL;
        pointer_global_prim_element = NULL;
        delete s;
        return q;
    }
    else
    {
        int q = pointer_global_prim_element->info;
        coada * s = pointer_global_prim_element;
        pointer_global_prim_element = s->next;
        delete s;
        pointer_global_prim_element->prev = NULL;
        return q;
    }
}

int pop_right()
{
    if (!pointer_global_prim_element) {
       // cout<<"coada goala.";
        return -1;
    }
    else if(pointer_global_prim_element == pointer_global_ultim_element)
    {
        int q = pointer_global_prim_element->info;
        coada * s = pointer_global_prim_element;
        pointer_global_prim_element = NULL;
        pointer_global_prim_element = NULL;
        delete s;
        return q;
    }
    else
    {
        int q = pointer_global_ultim_element->info;
        coada * s = pointer_global_ultim_element;
        pointer_global_ultim_element = s->prev;
        delete s;
        pointer_global_ultim_element->next = NULL;
        return q;
    }
}

void afisare_stanga()
{
    cout<<endl;
    coada * s = pointer_global_prim_element;
    while (s){
        cout<<s->info<<" ";
        s = s->next;
    }
}

int main()
{
    int m, counter=2;
    f >> m;
    int a[m+1][m+1],M[m+1][m+1];
    for ( auto i=0; i<m; i++ )
        for ( auto j=0; j<m; j++ )
            M[i][j] = 0;
    for ( auto i=0; i<m; i++ )
        for ( auto j=0; j<m; j++ )
            f >> a[i][j];
    for ( auto i=0; i<m; i++ )
        for ( auto j=0; j<m; j++ )
        {
            if ( a[i][j] == 1 )
            {

                push_right(i);push_right(j);
                while ( pointer_global_prim_element )
                {
                    int x = pop_left(); int y = pop_left();
                    M[x][y] = counter;
                    a[x][y] = 0;
                    if ( a[x-1][y] == 1 && x-1 >= 0 ){ push_right(x-1);push_right(y); }
                    if ( a[x][y-1] == 1 && y-1 >= 0 ){ push_right(x);push_right(y-1); }
                    if ( a[x+1][y] == 1 && x+1 < m ){ push_right(x+1);push_right(y); }
                    if ( a[x][y+1] == 1 && y+1 < m ){ push_right(x);push_right(y+1); }
                }
                counter++;
            }
        }
    for ( auto i=0; i<m; i++ ){
        for ( auto j=0; j<m; j++ )
            cout<<M[i][j]<<" ";
        cout<<endl;
    }


    return 0;
}
