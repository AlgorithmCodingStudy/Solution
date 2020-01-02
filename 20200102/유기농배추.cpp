// 1.행열 반대
// 2. 2차원 초기화 방식 바꾸기
// 3. visited 추가
// 4. 배추 다섯 개 인 것도 몰랐음
// 방법을 바꾸기
#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int map[50][50] = { 0 };
bool check[50][50] = { false };
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };
int M = 0, N = 0;


void dfs(int px, int py) {
	

	

	

	//상하좌우
	for (int a = 0; a < 4; a++) {
		int ax = px + dx[a];
		int ay = py + dy[a];
		if (ax >= 0 && ax < M && ay >= 0 && ay < N && map[ax][ay] == 1 && check[ax][ay] == false) {

			check[ax][ay] = true;
			dfs(ax, ay);

		}
	}
	}

int main() {
		int T=0, M=0, N = 0, K=0,cnt=0;
		cin >> T;
	
		for (int i = 0; i < T; i++) {
		cin >> M >> N >> K;
		cnt = 0;
		

		memset(map, 0, sizeof(map));
		memset(check, false, sizeof(check));

		


		for (int k = 0; k < K; k++) {
			//배추 표시
			int x = 0, y = 0;
			cin >> x >> y;
			map[y][x] = 1;		
		}
		

		for (int a = 0; a < N; a++) {
			for (int b = 0; b < M; b++) {				
				if (map[a][b] == 1 && check[a][b] == false) {
					//여기서 방문체크 안함
					check[a][b] = true;
					dfs(a, b);
					cnt++;
				}
			}		
		}

		cout << cnt << "\n";
	}

}
