#include <iostream>
#include <vector>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int parent[101], setSize[101],n;
double x, y, result;
vector<pair<double, double>> v;


int findParent(int node){
    if (node == parent[node])
        return node;
    return parent[node] = findParent(parent[node]);
}

void merge(int node1, int node2){
    node1 = findParent(node1); 
    node2 = findParent(node2); 

    if (node1 != node2){
        if (setSize[node1] < setSize[node2])
            swap(node1, node2);
        parent[node2] = node1; 
        setSize[node1] += setSize[node2];
        setSize[node2] = 0; 
    }
}

struct Edge {
    int u, v;
    double weight;
    bool operator<(Edge const& e){
        return weight < e.weight;
    }
};

int main(void){
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        v.push_back({ x,y });
    }

    vector<Edge> edge;
    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            double d=sqrt(pow(v[i].first - v[j].first, 2) + pow(v[i].second - v[j].second, 2));
            edge.push_back({ i,j,d });
        }
    }
   
    sort(edge.begin(), edge.end());

    for (int i = 0; i < n; i++){
        parent[i] = i;
        setSize[i] = 1;
    }

    for (int i = 0; i < edge.size(); i++){
        Edge e = edge[i];

        if (findParent(e.u) != findParent(e.v)){
            result += e.weight;
            merge(e.u, e.v);
        }
    }
    cout << fixed;
    cout.precision(2);
    cout << result << "\n";
}
