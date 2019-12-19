#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N = 0;
int map[25][25] = { 0 };
bool visited[25][25];
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };
int cnt = 0;
vector<int> arr;
void dfs(int i, int j) {
	
	/*
	//언제 종료..?
	if () { 
		
		arr.push_back(cnt);
		return; }

	*/

	visited[i][j] = true;
	cnt++;

	for (int k = 0; k < 4; k++) {
		int ax = i + dx[k];
		int ay = j + dy[k];
		// 상하좌우 중에
		if (ax >= 0 && ax < N) {
			if (ay >= 0 && ay < N) {
				//방문 안하고 숫자 1이면 다시 탐색 1조건 빼먹음
				//1만 있는 곳을 탐색해야 되니까
				//1인지 검사
				if (!visited[ax][ay] && map[ax][ay]==1) dfs(ax, ay);

			}
		}
	}
	
	
	}





int main() {
	
	
	cin >> N;
	
	
	//입력 받기
	for (int i = 0; i < N; i++) {
		
		for (int j = 0; j < N; j++) {
		
			cin >> map[i][j];
		}
	
	}

	// 0,0부터 시작하는 게 아니라
	// 1이면서 방문 안 한곳에서 갯수 세기 시작
	for (int a = 0; a < N; a++) {
		for (int b = 0; b < N; b++) {
			
			if (map[a][b] == 1 && visited[a][b] == false) {
				//새로운 영역 시작할 때 cnt 초기화
				cnt = 0;
				dfs(a, b);
				
				arr.push_back(cnt);
				//넓이 넣기

			}

		}
	}

	int arrsize = arr.size();

	cout << arrsize << endl;

	sort(arr.begin(), arr.end());
	
	for (int k = 0; k < arrsize; k++) {
		cout << arr[k] << endl;
	
	
	}

	return 0;

	
}
