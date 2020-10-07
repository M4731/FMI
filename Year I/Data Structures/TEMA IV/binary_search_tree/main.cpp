#include <iostream>

using namespace std;

struct tree
{
    int info;
    tree *left, *right;
}*r;

void insert( int x )
{
    if ( !r ){
        tree *insertion = new tree;
        insertion->info = x;
        insertion->left = NULL;
        insertion->right = NULL;
        r = insertion;
    }
    else {
        tree *w = r;
        tree *aux = w;
        while (w){
            aux = w;
            if ( x > w->info ){
                w = w->right;
            }
            else{
                w = w->left;
            }
        }
        tree *insertion = new tree;
        if ( aux->info < x ){
            insertion->info = x;
            insertion->left = NULL;
            insertion->right = NULL;
            aux->right = insertion;
        }
        else {
            insertion->info = x;
            insertion->left = NULL;
            insertion->right = NULL;
            aux->left = insertion;
        }
    }
}

void SRD ( tree* root )
{
    if ( root ){
       SRD(root->left);
       cout<<root->info<<" ";
       SRD(root->right);
    }
}

void RSD ( tree* root )
{
    if ( root ){
       cout<<root->info<<" ";
       RSD(root->left);
       RSD(root->right);
    }
}

bool search ( int x )
{
    tree *w = r;
    while  (w)
    {
        if ( w->info == x ) return 1;
        else if ( w->info < x ) w = w->right;
        else w = w->left;
    }
    return 0;
}

void remove ( int x )
{
    tree *w = r;
    tree *aux = w;
    while (w){
        if ( x > w->info ){
            aux = w;
            w = w->right;
        }
        else if ( x < w->info ){
            aux = w;
            w = w->left;
        }
        else{
            if ( w->left == 0 && w->right == 0 )
            {
                if ( aux->left == w ) aux->left = 0;
                else aux->right = 0;
                delete w;
            }
            else if ( w->left != 0 && w->right == 0 )
            {
                if ( aux->left == w ) aux->left = w->left;
                else aux->right = w->left;
            }
            else if ( w->left == 0 && w->right != 0 )
            {
                if ( aux->left == w ) aux->left = w->right;
                else aux->right = w->right;
            }
            else
            {
                tree *help = w->right;
                while ( help->left != 0 ) help = help->left;
                int v = help->info;
                remove(help->info);
                w->info=v;
            }
            return;
        }
    }
    return;
}

int main()
{
    int x[9] = { 6, 4, 2, 1, 3, 5, 9, 7, 8 };
    for ( unsigned i=0; i<9; i++ ) insert(x[i]);
    SRD(r);cout<<endl;
    RSD(r);cout<<endl;
    cout<<search(3)<<" ";
    cout<<search(8)<<" ";
    cout<<search(69)<<endl;
    remove(69);
    remove(6);
    RSD(r);cout<<endl;
    SRD(r);cout<<endl;
    insert(0);
    RSD(r);cout<<endl;
    SRD(r);cout<<endl;
    return 0;
}
