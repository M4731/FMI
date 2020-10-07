#include <iostream>

using namespace std;

struct stiva{
    int info;
    stiva * next;
}*pointer_global_element_varf;

void push ( int x )
{
    if(!pointer_global_element_varf){
        pointer_global_element_varf = new stiva;
        pointer_global_element_varf->info = x;
        pointer_global_element_varf->next = NULL;
    }
    else{
        stiva * c = new stiva;
        c -> info = x;
        c->next = pointer_global_element_varf;
        pointer_global_element_varf = c;
    }

}

int pop ()
{
    int x;
    if(!pointer_global_element_varf) {
        cout<<"Stiva goala.";
        return -1;
    }
    else{
        x = pointer_global_element_varf->info;
        stiva * c = pointer_global_element_varf;
        pointer_global_element_varf = c->next;
        delete c;
    }
    return x;
}

void afisare ()
{
    stiva * c = pointer_global_element_varf;
    while(c){
        cout << c->info << " ";
        c = c->next;
    }
}

int main()
{
    push(1);
    pop();
    push(2);
    push(3);
    afisare();
    return 0;
}
