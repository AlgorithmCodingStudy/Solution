//우선순위 큐 이용하면 시간초과! (시간복잡도 계산해보기!)

#include<iostream>
#include<vector>
#include<cstring>
#include<queue>

using namespace std;

struct tree { int x,y,age; 
bool operator < (const tree& a)const
	{
		return age > a.age;
	}
};

int N, M, K;
int init_map[15][15];
int nutrient[15][15]; // 겨울
priority_queue<tree>Q; //봄_초기값
queue<tree>live; //가을
queue<tree>dead; // 여름
int dx[] = { -1,-1,-1,0,0,1,1,1 };
int dy[] = { -1,0,1,-1,1,-1,0,1};

void spring();
void summer();
void fall();
void winter();

int main()
{
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
	cin >> N >> M >> K;

	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			cin >> nutrient[i][j]; //겨울에 추가할 양분입력
			init_map[i][j] = 5;
		}
	}
	

	for (int i = 0; i < M; i++)
	{
		int a = 0, b = 0, c = 0;
		cin >> a >> b >> c;
		Q.push({ a,b,c }); //심은나무를 큐에저장(우선순위큐)
	}


	while (K--)
	{
		//cout << K << "번쩨" << endl;
		spring();
		summer();
		fall();
		winter();
	}

	cout << Q.size() << "\n";
}

void spring()
{
	while (!live.empty())
	{
		live.pop();
	}
	while (!Q.empty())
	{
		int cx = Q.top().x;
		int cy = Q.top().y;
		int age = Q.top().age;
		Q.pop();
		//cout << cx << " "<<cy<<" " << age<<" " << init_map[cx][cy] << endl;
		
		if (init_map[cx][cy] >= age)
		{
			init_map[cx][cy] -= age;
			//cout << "live: " <<cx << " " << cy << " " << age << " " << init_map[cx][cy] << endl;
			live.push({ cx,cy,age + 1 }); //양분먹음
		}
		else if(init_map[cx][cy] < age){
		
			//cout << "spring dead: " << cx << " " << cy << " " << age << " " << init_map[cx][cy] << endl;
			dead.push({ cx,cy,age });
		}
	}
}

void summer()
{
	while (!dead.empty())
	{
		int cx = dead.front().x;
		int cy = dead.front().y;
		int age= dead.front().age;
		dead.pop();

		init_map[cx][cy] +=(age/2);
		//cout << "summer dead: " << cx << " " << cy << " " << age << " " << init_map[cx][cy] << endl;
	}
}

void fall()
{
	while (!Q.empty())
	{
		Q.pop();
	}

	while (!live.empty())
	{
		int cx = live.front().x;
		int cy = live.front().y;
		int age = live.front().age;
		live.pop();

		Q.push({ cx,cy,age }); //봄에작동할거 저장

		if (age % 5 == 0)
		{
			for (int i = 0; i < 8; i++)
			{
				int nx = cx + dx[i];
				int ny = cy + dy[i];

				if (nx <= 0 || ny <= 0|| nx > N || ny > N)continue;

				Q.push({ nx,ny,1 });
				//cout << "fall_live: " << cx << " " << cy << " " << age << " " << init_map[cx][cy] << endl;
			}
		}
	}
}

void winter()
{
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			init_map[i][j] += nutrient[i][j]; //양분추가
		}
	}
}
