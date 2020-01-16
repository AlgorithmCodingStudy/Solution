#include <iostream>
#include <queue>
#include <cstring> //memset
using namespace std;
int visited[300][300] = { 0 };
int I = 0;
int bfs(int firstx, int firsty,int lastx,int lasty) {
	queue<pair<int, int>> q;
	memset(visited, 0, sizeof(visited));
	
	q.push(make_pair(firstx, firsty));
	visited[firstx][firsty] = 0;

	while (!q.empty()) {
		//팝팝팝팝팝
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		int dx[8] = { -1,-2,-2,-1,1,2,2,1 };
		int dy[8] = { -2,-1,1,2,-2,-1,1,2 };
	
		for (int a = 0; a < 8; a++) {
			int ax = x + dx[a];
			int ay = y + dy[a];

			if (ax >= 0 && ax < I && ay >= 0 && ay < I) {
				if (visited[ax][ay] == 0) {
					q.push(make_pair(ax, ay));
					visited[ax][ay] = visited[x][y] + 1;
				}
			}		
		}
	}
	return visited[lastx][lasty];

}
int main() {
	int rotation = 0;
	cin >> rotation;

	for (int i = 0; i < rotation; i++) {
		int first_x = 0, first_y = 0, last_x = 0, last_y = 0;

		cin >> I;
		cin >> first_x >> first_y;
		cin >> last_x >> last_y;
		if ((first_x == last_x) && (last_x == last_y)) {
			cout << 0 << endl;
			continue;
		}
		cout << bfs(first_x, first_y,last_x,last_y) << endl;
	}
}
