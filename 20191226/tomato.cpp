#include <iostream>
#include <queue>
using namespace std;
bool visted[1000][1000];
queue <pair<int, int>> q;
int arr[1000][1000] = { 0 };
void bfs(int x, int y) {

	int dx[4] = { -1,1,0,0 };
	int dy[4] = { 0,0,-1,1 };

	visted[x][y] = true;
	q.push(pair<int,int>(x, y));

	while (!q.empty()) {
	
		pair<int, int> p = q.front();
		int nx = p.first;
		int ny = p.second;
		q.pop();
		
		for (int i = 0; i < 4; i++) {

			if (arr[nx + i][ny + i] != 0 && arr[nx][ny] == 0) {
			
				arr[nx][ny] = 1;
				visted[nx][ny] = true;
				q.push(pair<int, int>(nx, ny));
			}
		
		}
		
	
	}

}

int main() {

	int M = 0, N = 0;
	

	cin >> M >> N;

	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
		
			cin >> arr[M][N];
		}
	}

	for (int a = 0; a < M; a++) {
		for (int b = 0; b < N; b++) {
			if (arr[a][b] == 1 && ~visted[a][b]) bfs(a, b);

		
		}
	}

	for (int c = 0; c < M; c++) {
		for (int d = 0; d < N; d++) {
			if (arr[c][d] == 0) return -1;


		}
	}
	return 0;
}
