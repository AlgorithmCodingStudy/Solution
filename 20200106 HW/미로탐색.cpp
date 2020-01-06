#include <iostream>
#include <queue> //헤더 추가하기

using namespace std;


int main() {

	int N = 0, M = 0;
	int map[100][100] = { 0 };
	int visited[100][100] = { 0 };
	int dx[4] = { -1,1,0,0 };
	int dy[4] = { 0,0,-1,1 };
	queue<pair<int, int>> q;
	int cnt = 1;

	cin >> N >> M;

	//붙어서 하는 경우 정리
	
	for (int i = 0; i < N; i++) {
		string temp;
		cin >> temp;
		//이렇게 하면 인덱스 0부턴데 N-1까지 
		//1부터 N까지 해서 오류 났음
		for (int j = 0; j < M; j++) {
			map[i][j] = temp[j] - '0';			
		}	
	}



	q.push(make_pair(0, 0));
	visited[0][0] = 1;


	while (!q.empty()) {

		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		
		if ((x == N - 1) && (y == M - 1)) {
			cout << visited[N - 1][M - 1] << endl;
			return 0;
			//많이 돌려보기

		}

		for (int a = 0; a < 4; a++) {

			int ax = x + dx[a];
			int ay = y + dy[a];


			if (ax >= 0 && ax < N && ay >= 0 && ay < M) {
				
				if (visited[ax][ay] == 0 && map[ax][ay] == 1) {
					q.push(make_pair(ax, ay));
					visited[ax][ay] = visited[x][y] + 1;
				}
			}
		}
	}

	

	
}
