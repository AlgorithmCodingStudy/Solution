
#include<iostream>
#include <queue>

using namespace std;
int arr[20][20] = { 0 };
bool visited[20][20];

int main(int argc, char** argv)
{
	int test_case;
	int T;
	int N = 0;
	int dx[4] = { -1,1,-1,1 };
	int dy[4] = { -1,-1,1,1 };
	int length = 0;
	vector<int> lenarr;
	typedef struct {
		int x;
		int y;
		int z;
	}st;

	/*
	상좌:1
	상우:2
	하좌:3
	하우:4
	*/
	queue<st>q;
	vector<int> dessrt;
	
	
	cin >> T;
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> N;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> arr[i][j];
			
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				q.push({ i,j,0 });
				q.push({ i,j,0 });
				q.push({ i,j,0 });
				q.push({ i,j,0 });
				dessrt.push_back(arr[i][j]);
				visited[i][j] = true;
				length = 1;

				while (!q.empty()) {
					
					int x = q.front().x;
					int y = q.front().y;
					int dir = q.front().z;
					q.pop();

					for (int k = 0; k < 4; k++) {
						
						int nx = x + dx[k];
						int ny = y + dy[4];
						if (nx > 0 && nx < N && ny>0 && ny < N) {
							auto a = find(dessrt.begin(), dessrt.end(), arr[nx][ny] == dessrt.end();
							if (a == dessrt.end()) {
								q.push({ nx, ny,k + 1 });
								visited[nx][ny] = true;
								dessrt.push_back(arr[nx][ny]);
								if (dir == k + 1) length++;
								else {
									lenarr.push_back(length);
									length = 0;
								}
							}
						
						}

					
					}
				
				
				
				}

				

			}
		}
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
