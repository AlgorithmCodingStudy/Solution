#include <iostream>
#include <queue>

using namespace std;

char map[250][250];
bool visited[250][250];
int finalSheep = 0, finalWolf = 0;
void bfs(int r, int c) {
	queue<pair<int, int>> q;
	int sheep = 0, wolf = 0;
	
	for (int a = 0; a < r; a++) {
		for (int b = 0; b < c; b++) {
			if (map[a][b] == 'v' || map[a][b] == 'o') {
				
				if (sheep > wolf) finalSheep += sheep;
				else finalWolf += wolf;

				sheep = (map[a][b] == 'o') ? 1 : 0;
				wolf = (map[a][b] == 'v') ? 1 : 0;
				q.push(make_pair(a, b));
			}
		
			while (!q.empty()) {
				int x = q.front().first;
				int y = q.front().second;
				q.pop();

				int dx[4] = { -1,1,0,0 };
				int dy[4] = { 0,0,-1,1 };
				
				for (int c = 0; c < 4; c++) {
					int nx = x + dx[c];
					int ny = y + dy[c];

					if (nx >= 0 && nx < r && ny >= 0 && ny < c&&!visited[nx][ny]) {
						if (map[nx][ny] == '#') {
							visited[nx][ny] = true;
						}
						if (map[nx][ny] == '.') {
							visited[nx][ny] = true;
							q.push(make_pair(nx, ny));
						}
						if (map[nx][ny] == 'v') {
							visited[nx][ny] = true;
							q.push(make_pair(nx, ny));
							wolf++;
						}
						if (map[nx][ny] == 'o') {
							visited[nx][ny] = true;
							q.push(make_pair(nx, ny));
							sheep++;
						}
					}
				}
			}
			
		}	
	}
}

int main() {
	int R = 0, C = 0;
	cin >> R >> C;

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cin >> map[i][j];
		}
	}

	bfs(R, C);
	cout << finalSheep << " " << finalWolf;
}
