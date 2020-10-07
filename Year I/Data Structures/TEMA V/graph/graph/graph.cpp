#include <iostream>
#include <vector>
#include <list>

using namespace std;

class directedGraph
{
    vector <list <int> > v;
public:
    void addNode(int);
    void addEdge(int, int);
    bool hasEdge(int, int);
    void DFS(int);
    void DFSUtil(int, vector<bool>);
    void BFS(int);
    int twoCycles();
};

void directedGraph::addNode(int a)
{
    if (a >= v.size())
    {
        v.resize(a+1, list<int>());
    }
    v[a] = list<int>();
}

void directedGraph::addEdge(int source, int target)
{
    v[source].push_back(target);
}

bool directedGraph::hasEdge(int source, int target)
{
    for (auto i = v[source].begin(); i != v[source].end(); i++)
    {
        if (target == *i)
            return true;
    }
    return false;
}

void directedGraph::DFS(int startNode)
{
    vector<bool> ok(v.size(), false);
    DFSUtil(startNode, ok);
}

void directedGraph::DFSUtil(int w, vector<bool> ok)
{
    ok[w] = true;
    cout << w << " ";

    for ( auto i:v[w] )
        if ( !ok[i] )
            DFSUtil( i, ok);
}

void directedGraph::BFS(int startNode)
{
    vector<bool> ok(v.size(), false);
    list<int> queue;

    ok[startNode] = true;
    queue.push_back(startNode);

    while ( !queue.empty() )
    {
        startNode = queue.front();
        cout << startNode << " ";
        queue.pop_front();

        for ( auto i:v[startNode] )
        {
            if (!ok[i])
            {
                ok[i] = true;
                queue.push_back(i);
            }
        }
    }
}

int directedGraph::twoCycles()
{
    int cal = 0;
    for (unsigned i = 0; i < v.size(); i++)
    {
        for (auto j : v[i])
        {
            for (auto y : v[j])
            {
                if (y == i)
                    cal++;
            }
        }
    }
    return cal / 2;
}

int main()
{
    directedGraph g;
    g.addNode(0);
    g.addNode(1);
    g.addNode(2);
    g.addNode(4);
    g.addEdge(0, 1);
    g.addEdge(1, 4);
    g.addEdge(0, 2);
    g.addEdge(2, 0);
    g.addEdge(4, 1);
    g.DFS(0);
    cout << endl;
    g.BFS(0);
    cout << endl;
    cout << g.twoCycles() << " twoCycles." << endl;
    cout << g.hasEdge(0, 1) << " " << g.hasEdge(1, 2);
}
