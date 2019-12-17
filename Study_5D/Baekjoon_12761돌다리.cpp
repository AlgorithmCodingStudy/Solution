// 움직이는 방법 8가지
// +1칸,-1칸,+A칸,-A칸,+B칸,-B칸,현위치*A칸,현위치*B칸
// 콩콩이의힘 A,B,동규위치N,주미위치M
// 0~100,000개의 돌
// 최소이동횟수?
/*
	동규위치부터 시작
	queue에 이동가능한 위치 넣고 
	pop하면서 이동횟수 체크
	배열에 입력한 이동횟수와 겹칠때 최솟값 구하기!

*/

#include<iostream>
#include<queue>

using namespace std;

int A, B, N, M;
bool Stone[100001] = { false };
queue<pair<int,int>>Go;

int BFS()
{
	while(!Go.empty())
	{
		int cur = Go.front().first;
		int num = Go.front().second;
		Go.pop();

		if (cur == M)
		{
			return num;
		}

		int nx = cur + 1;
		if (nx <= 100000 && Stone[nx] == false) {
			Stone[nx] = true;
			Go.push({ nx,num + 1 });
		}

		nx = cur - 1;
		if (nx >= 0 && Stone[nx] == false) {
			Stone[nx] = true;
			Go.push({ nx,num + 1 });
		}
		
		nx = cur + A;
		if (nx <= 100000 && Stone[nx] == false) {
			Stone[nx] = true;
			Go.push({ nx,num + 1 });
		}
		
		nx = cur - A;
		if (nx >= 0 && Stone[nx] == false) {
			Stone[nx] = true;
			Go.push({ nx,num + 1 });
		}
		
		nx = cur + B;
		if (nx <= 100000 && Stone[nx] == false) {
			Stone[nx] = true;
			Go.push({ nx,num + 1 });
		}
		
		nx = cur - B;
		if (nx >= 0 && Stone[nx] == false) {
			Stone[nx] = true;
			Go.push({ nx,num + 1 });
		}
		

		nx = cur * A;
		if (nx <= 100000 && Stone[nx] == false) {
			Stone[nx] = true;
			Go.push({ nx,num + 1 });
		}
		
		nx = cur * B;
		if (nx <= 100000 && Stone[nx] == false) {
			Stone[nx] = true;
			Go.push({ nx,num + 1 });
		}
		
	}
}

int main()
{
	cin >> A >> B >> N >> M;

	Go.push({ N,0 });
	Stone[N] = true;

	cout << BFS() << endl;

	return 0;
}
