#include <iostream>
#include <queue>

using namespace std;

bool visited[1000001];

int main() {
	
	vector<pair <int, int> > q; //벡터 선언 다시
	
	int A, B, N, M;
	
	cin >> A >> B >> N >> M;
	
	int p = N;

	int arr[8] = {p+1, p-1, p+A, p-A, p+B,p-B, p*A,p*B };
	
	int cnt = 0; //이동 횟수
	
	visited[N] = true;
	
	q.push_back(pair<int, int>(N, cnt));

	
	while (!q.empty()) {

		if (p == M) {
			cout << cnt << endl;
			return 0;
		}
		
		for (int i = 0; i < 8; i++) {
			if ( p> 0 &&  p< 1000001) {
				if (!visited[arr[i]]) {
					p = arr[i];

					visited[arr[i]] = true;

					q.push_back(pair<int, int>(visited[arr[i]], cnt + 1));
				}
			}
		}
	
	}



	
	
	
	
	
	
}
