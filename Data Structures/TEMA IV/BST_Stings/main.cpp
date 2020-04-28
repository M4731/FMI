#include <iostream>
#include <string>

using namespace std;

struct tree
{
    string info;
    tree *left, *right;
}*r;

void insert( string x )
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

int main()
{
    int n;
    string x;
    cin>>n;
    for (  unsigned i=0; i<n; i++ )
    {
        cin>>x;
        insert(x);
    }
    SRD(r);

}
