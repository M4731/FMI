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
        //cout<<"Stiva goala.";
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
    int x;
    int n;cout<<"CITESTE N : ";cin>>n;
    for (auto i=0; i<n; i++)
    {
        cout<<"ELEMENT "<<i<<" : ";cin >> x;
        if( pointer_global_element_varf )
            if ( pointer_global_element_varf->info == x )
            {
                pop();
            }
            else
            {
                push(x);
            }
        else{
            push(x);
        }
    }
    if( pop() == -1 )cout<<"VALID.";
    else cout<<"INVALID.";
    return 0;
}






