#include <iostream>
#include <queue>

using namespace std;

int L, R, C,sL,sR,sC,eL,eR,eC,visited[50][50][50];
char a[50][50][50];
int bfs(int sl,int sr, int sc, int el, int er, int ec) {
    queue<pair<pair<int, int>, int>> q;
    q.push(make_pair(make_pair(sr,sc),sl));
    visited[sl][sr][sc] = 1;

    while (!q.empty()) {
        int z = q.front().first.second;
        int y = q.front().first.first;
        int x=
        q.pop();
    }
}

int main()
{
    while (true) {       
        cin >> L >> R >> C;
        if (L == 0) break;
        for (int k = 0; k < C; k++) {
           for (int i = 0; i < L; i++) {
                for (int j = 0; j < R; j++) {
                
                    cin >> a[i][j][k];
                    if (a[i][j][k] == 'S') {
                        sL = i;
                        sR = j;
                        sC = k;
                    }
                    if(a[i][j][k] == 'E') {
                        eL = i;
                        eR = j;
                        eC = k;
                    }
             }
            }
        }
        int res = bfs(sL,sR,sC,eL,eR,eC);       
    }    
}
