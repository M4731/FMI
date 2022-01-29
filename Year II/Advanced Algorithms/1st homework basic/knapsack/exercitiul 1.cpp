#include<algorithm>
#include<iostream>

int pseudopolinomial(int S[], int K, int n)
{
    if(!n || !K)
    {
        return 0;
    }

    if(S[n-1] > K)
    {
        return pseudopolinomial(S, K, n-1);
    }
    else
    {
        int var = pseudopolinomial(S, K, n-1);
        int var2 = pseudopolinomial(S, K-S[n-1], n-1)+S[n-1];
        return std :: max(var, var2);
    }
}

int aproximativ(std :: istream &f, int K)
{
    int x;
    int s = 0;
    f>>x;
    while (x != -1)
    {
        if(x <= K-s){
            s+=x;
        }
        else if(x>s)
        {
            s=x;
        }
        f>>x;
    }
    return(s);
}

int main()
{
    int v[] = {1,33,2,2,3,66};
    std :: cout << pseudopolinomial(v,9,6);
    std :: cout << aproximativ(std :: cin, 9);
}