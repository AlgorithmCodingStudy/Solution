#include <string>
#include <vector>
using namespace std;
 
bool visited[201];
 
void DFS(int first, vector<vector<int>>&computers, int n) {
    visit[first] = true;
    
    for (int i = 0; i < n; i++) {
        if ((computers[start][i] == 1)&&(!visited[i])  ) {
            dfs(i, computers, n);
        }
      }
  }
 
int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            DFS(i, computers, n);
            answer++;
        }
      }
    
    return answer;
}
