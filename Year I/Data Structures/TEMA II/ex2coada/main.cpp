#include <iostream>

using namespace std;

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
        cout<<"coada goala.";
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
        cout<<"coada goala.";
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
    push_left(1);
    push_right(2);
    pop_right();
    pop_left();
    push_right(3);
    afisare_stanga();
   return 0;
}
