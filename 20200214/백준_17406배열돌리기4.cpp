#include<iostream>
#include<vector>
#include<cstring>
#include<queue>
#include<algorithm>

using namespace std;

struct info { int r, c, s; };
int N, M, K;
int originMap[55][55]; //초기배열
int cpyMap[55][55]; //배열회전저장
vector<info>Oper;
vector<info>selectoper;
vector<int>Result;
bool check[10];

void Select(int cnt);
void Calminimum();
void Rotate(int r, int c, int s);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M >> K;
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= M; j++)
		{
			cin >> originMap[i][j];
		}
	}
	for (int i = 0; i < K; i++)
	{
		int r, c, s;
		cin >> r >> c >> s;
		Oper.push_back({ r,c,s });
	}

	//연산순열로구하기
	Select(0);

	int Ans = *min_element(Result.begin(), Result.end());

	cout << Ans << "\n";

	return 0;
}

void Select(int cnt)
{
	if (cnt == K) //회전시킬연산자 순서구했을때
	{
		memcpy(&cpyMap, &originMap, sizeof(originMap));

		for (int i = 0; i < selectoper.size(); i++)
		{
			int cr = selectoper[i].r;
			int cc = selectoper[i].c;
			int cs = selectoper[i].s;

			Rotate(cr, cc, cs);
		}

		Calminimum();
		
		return;
	}

	for (int i = 0; i < K; i++)
	{
		if (check[i] == true)continue;
		check[i] = true;
		selectoper.push_back(Oper[i]);
		Select(cnt + 1);
		selectoper.pop_back();
		check[i] = false;
	}

}

void Rotate(int r, int c, int s)
{
	int cpy[55][55] = { 0 };
	int rotcnt = r + s / 2;
	queue<int>Q;
	memcpy(&cpy, &cpyMap, sizeof(cpyMap));

	//회전
	int sr = r - s; int sc = c - s; int er = r + s; int ec = c + s;
	while (rotcnt--)
	{
		//정보집어넣기
		while (!Q.empty())
		{
			Q.pop();
		}

		for (int y = sc; y <= ec; y++)
		{
			Q.push(cpy[sr][y]);
		}
		for (int x = sr + 1; x <= er; x++)
		{
			Q.push(cpy[x][ec]);
		}
		for (int y = ec - 1; y >= sc; y--)
		{
			Q.push(cpy[er][y]);
		}
		for (int x = er - 1; x >= sr + 1; x--)
		{
			Q.push(cpy[x][sc]);
		}

		if (Q.size() <= 1)break;
		//정보빼기
		for (int y = sc + 1; y <= ec; y++)
		{
			//cout << Q.front() << " ";
			cpyMap[sr][y] = Q.front();
			Q.pop();
		}
		for (int x = sr + 1; x <= er; x++)
		{
			//cout << Q.front() << " ";
			cpyMap[x][ec] = Q.front();
			Q.pop();
		}
		for (int y = ec - 1; y >= sc; y--)
		{
			//cout << Q.front() << " ";
			cpyMap[er][y] = Q.front();
			Q.pop();
		}
		for (int x = er - 1; x >= sr + 1; x--)
		{
			//cout << Q.front() << " ";
			cpyMap[x][sc] = Q.front();
			Q.pop();
		}
		//cout << Q.front() << " ";
		cpyMap[sr][sc] = Q.front();
		
		//cout << endl;

		//다음턴을위해 정보바꾸기
		sr++; sc++; er--; ec--;
	}

	
}


void Calminimum()
{
	int mmin = 99999999;
	for (int i = 1; i <= N; i++)
	{
		int hap = 0;
		for (int j = 1; j <= M; j++)
		{
			hap += cpyMap[i][j];
		}
		if (mmin > hap)
			mmin = hap;
	}
	Result.push_back(mmin);
}
