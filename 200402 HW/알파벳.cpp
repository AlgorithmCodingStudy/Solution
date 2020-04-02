#include <iostream>
#include <algorithm>

using namespace std;

int R, C,ret, visited[26], dy[4] = { 0,0,-1,1 }, dx[4] = { -1,1,0,0 };
char a[24][24];

void dfs(int y, int x,int cnt) {
	ret = max(ret, cnt);
	for (int i = 0; i < 4; i++) {
		int ny = y + dy[i];
		int nx = x + dx[i];		
		if (ny < 0 || ny >= R || nx < 0 || nx >= C) continue;		
		if (visited[a[ny][nx]-'A'] ) continue;		
		visited[a[ny][nx] - 'A'] = 1;
		dfs(ny, nx,cnt+1);
		visited[a[ny][nx] - 'A']=0;	
	}
}

int main() {
	cin >> R >> C;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cin >> a[i][j];
		}
	}		
	visited[a[0][0]-'A'] = 1;
	dfs(0, 0, 1);
	cout<<ret;	
}
