#include <iostream>
#include <queue>
 
using namespace std;
 
int adj[101][101];
int visited[101][101];
queue<pair<int, int>> q;
int N;
 
void bfs(int a, int b) {
     
    visited[a][b] = 1;
    
    q.push(make_pair(a, b));
     
    while(!q.empty()) {
         
        for(int i = 0; i < N; i++)
            if(adj[q.front().second][i] && !visited[a][i]) {
                visited[a][i] = 1;
                q.push(make_pair(q.front().second, i));
            }
        q.pop();
    }
}
 
 
 
int main(void) {
    
    cin >> N; 
     
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++)
            cin >> adj[i][j];
             
    
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++)
            if(adj[i][j])
                bfs(i, j);
     
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++)
            cout<<visited[i][j] << ' ';
            cout<<'\n';
        }
    
    
    
    
    
    
}
