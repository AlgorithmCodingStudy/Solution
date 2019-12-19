#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int visited[100001] = { 0, };
queue<int> q;
int N = 0, K = 0;

int bfs(int first) {
	//수빈이 위치 큐에 넣고 방문 체크
	int cnt = 0;
	q.push(first);
	visited[first] = 0;

	while (!q.empty()) {

		
		//큐에 제일 앞에 있는 거 꺼냄
		int pt = q.front();
		q.pop();
		//만났으면 횟수 리턴
		if (pt == K) return visited[pt];

		//+1,-1,*2 3가지 경우 모두 방문한다
		// 방문하기전에 		
		// 배열 범위 안 벗어나고 방문 안 했는지 검사하고
		//조건 만족하면 방문체크하고 큐에 넣기
		//visited에 이동횟수 저장
		if (pt + 1 < 100001 && visited[pt + 1] == 0) {
			visited[pt + 1] = visited[pt ]+ 1 ;
			q.push(pt + 1);
		}

		if (pt - 1 >0  && visited[pt - 1] == 0) {
			visited[pt - 1] = visited[pt] + 1;
			q.push(pt - 1);
		}

		if (pt * 2 < 100001 && visited[pt * 2] == 0) {
			visited[pt * 2] = visited[pt] + 1;
			q.push(pt * 2);
		}
	}








}
int main(void) {

	
	
	

	cin >> N >> K;
    
	cout << bfs(N);

	

}
