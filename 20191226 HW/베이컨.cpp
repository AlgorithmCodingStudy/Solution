#include <iostream>
#include <queue>
#include <cstring>
using namespace std;
queue<int> q;
bool friends[101][101];
int visited[101] = { 0 };

int N = 0, M = 0;

void bfs(int start) {	

	visited[start] = 1; //방문체크
	q.push(start);

	while (!q.empty()) {
	
		int node = q.front();
		q.pop();
		 
		//모든 노드에 대해
		for (int a = 1; a <= N; a++) {
			//친구관계이고 방문한 적 없으면
			if (friends[node][a] == true && visited[a] == 0) {
				visited[a] = visited[node] + 1; //단계 증가
				q.push(a);
			
			}
				
			
		
		}
	}


}
int main() {
	int idx = 0;// 최소인 인덱스
	int max = 10000;

	cin >> N >> M;

	//행렬로 친구 관계 입력 받기
	
		for (int j = 1; j <= M; j++) {
			int row = 0, col = 0;
			cin >> row >> col;
			friends[row][col] = true;
			friends[col][row] = true;

		}
	

	for (int k = 1; k <= N; k++) {
		memset(visited, 0, sizeof(int) * (N + 1));
		bfs(k);
		int sum = 0;

		// 나 제외하고 단계의 합 구하기
		for (int h = 1; h <= N; h++) {
			if (k == h) continue;

			else sum += (visited[h] - 1);

			

		}
        //케빈 베이컨 수 최소인 거 업데이트
				if (sum < max) {
					max = sum;
					idx = k;

				}
			
			
			

		

		


	}

	cout << idx;

}
