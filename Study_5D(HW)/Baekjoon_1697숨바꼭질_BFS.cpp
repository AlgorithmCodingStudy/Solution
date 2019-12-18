#include<iostream>
#include<queue>

using namespace std;

int N, K;
bool check[100001] = { false };

queue<pair<int, int>>Q;

int BFS()
{
	while (!Q.empty()) 
	{
		int subin = Q.front().first;
		int time = Q.front().second;

		Q.pop();

		if (subin == K) //수빈이위치랑 동생위치 같으면
		{
			return time; //걸린시간 리턴
		}

		int nx = subin + 1; //다음위치 = 수빈위치 + 1
		if (nx <= 100000 && check[nx] == false) { //다음위치가 100,000을 넘지않고, 방문하지 않았으면 Q에 다음위치랑, 걸린 시간 넣어줌
			check[nx] = true;
			Q.push({ nx,time + 1 });
		}


		nx = subin - 1;
		if (nx >= 0 && check[nx] == false) {  //다음위치가 0미만이지 않고, 방문하지 않았으면 Q에 다음위치랑, 걸린 시간 넣어줌
			check[nx] = true;
			Q.push({ nx,time + 1 });
		}

		nx = subin * 2;
		if (nx <= 100000 && check[nx] == false) { //다음위치가 100,000을 넘지않고, 방문하지 않았으면 Q에 다음위치랑, 걸린 시간 넣어줌
			check[nx] = true;
			Q.push({ nx,time + 1 });
		}


	}

}

int main()
{
	cin >> N >> K;
  
	Q.push({ N,0 }); //Q에 초기값 넣어줌 (수빈이 위치, 움직인시간)
	check[N] = true; //현재 수빈이 위치 방문체크
	
	int result = BFS(); 
  
	cout << result << endl;
  
	return 0;

}



/*-------------------------------------------------------------------------------------------------------------------------*/


#include<iostream>
#include<queue>

using namespace std;

int N, K;
bool check[100001] = { false };

queue<pair<int, int>>Q;

int BFS()
{
	while (!Q.empty())
	{
		int subin = Q.front().first;
		int time = Q.front().second;
		Q.pop();

		if (subin == K)
		{
			return time;
		}

		int nx[] = { subin + 1,subin - 1,subin * 2 }; //가능한 다음위치를 배열에 저장해서
		for (int i = 0; i < 3; i++) //for문을 돌리면서 만족하지 않는 조건은 패스한다
		{
			if (nx[i] < 0 || nx[i] > 100000 || check[nx[i]] == true)continue;
			check[nx[i]] = true;
			Q.push({ nx[i],time + 1 });			
		}
	}
}

int main()
{
	
	cin >> N >> K;
	Q.push({ N,0 });
	check[N] = true;
	
	int result = BFS();
	cout << result << endl;
	return 0;

}
