#include<iostream>
#include<queue>
#include<cstring>
#include<set>

struct info { int num, time; };

struct info2 { int num, Rec_num, Rec_time; //고객번호, 접수창구번호, 접수창구에서 정비로옮긴시간
bool operator<(const info2 & a)const
{
	if (Rec_time == a.Rec_time)
	{
		if (Rec_num == a.Rec_num)
		{
			return num > a.num;
		}
		return Rec_num > a.Rec_num;
	}
	return Rec_time > a.Rec_time;
};
};

using namespace std;

int N, M, K, A, B, Allpeople;
int init_Rec[15]; //초기접수시간
int init_Rep[15]; //초기정비시간
info Rec[15]; //접수
info Rep[15]; //정비
int People[1100];//고객
bool check[1100];
int Time = 0;

priority_queue<info2>waitRec;//접수대기 
priority_queue<info2>waitRep;//정비대기
set<int>Recc;
set<int>Repp;

void init_All();
void Reception();
void Repair();
void Go_Rec();
void work_Rec();
void Go_Rep();
void work_Rep();


int main()
{
	int T;
	cin >> T;
	for (int q = 1; q <= T; q++) 
	{
		init_All();

		cin >> N >> M >> K >> A >> B;
		for (int i = 1; i <= N; i++)
		{
			cin >> init_Rec[i];
			Rec[i].time = -1;
			Rec[i].num = -1;
		}
		for (int i = 1; i <= M; i++)
		{
			cin >> init_Rep[i];
			Rep[i].time = -1;
			Rep[i].num = -1;
		}
		for (int i = 1; i <= K; i++)
		{
			cin >> People[i];
		}

		Allpeople = K;

		while (1)
		{
			Reception();
			Repair();
			Time++;
			if (Allpeople == 0)break;
		}

		vector<int>RReecc;
		vector<int>Result;

		set<int>::iterator iter;
		for (iter = Recc.begin(); iter != Recc.end(); iter++)
		{
			RReecc.push_back(*iter);
		}

		for (int i = 0; i < RReecc.size(); i++)
		{
			if (Repp.find(RReecc[i]) != Repp.end())
			{
				Result.push_back(RReecc[i]);
			}
		}

		int Ans = 0;
		for (int i = 0; i < Result.size(); i++)
		{
			Ans += Result[i];
		}
		if(Ans == 0) cout << '#' << q << " " << -1 << endl;
		else
			cout << '#'<<q<<" "<<Ans << endl;
	}
	return 0;
}


void Reception()
{
	for (int i = 1; i <= K; i++) //접수대기시키기
	{
		if (Time == People[i] && !check[i])
		{
			waitRec.push({i,0,0 });
			check[i] = true;
		}
	}
	
	Go_Rec();
	work_Rec();
}


void Repair()
{
	Go_Rep();
	work_Rep();
}

void Go_Rec()
{
	for (int i = 1; i <= N; i++)
	{
		if (waitRec.empty())return;
		if (Rec[i].num == -1 && Rec[i].time == -1)
		{
			Rec[i].num = waitRec.top().num;
			Rec[i].time = init_Rec[i];
			waitRec.pop();
		}
	}
}
void work_Rec()
{
	if (Rec[A].num > 0)
	{
		Recc.insert(Rec[A].num);
	}
	for (int i = 1; i <= N; i++)
	{
		if (Rec[i].time > 0 && Rec[i].num > 0) //창구에 사람있으면
		{
			Rec[i].time--; //시간--
		}
		if (Rec[i].time == 0 && Rec[i].num > 0) //사람있는데 시간이0이면
		{
			waitRep.push({ Rec[i].num,i,Time }); //정비대기로push, 현재창구 초기화
			Rec[i].time = -1;
			Rec[i].num = -1;
		}
	}
}
void Go_Rep()
{
	
	for (int i = 1; i <= M; i++)
	{
		if (waitRep.empty())return;
		if (Rep[i].num == -1 && Rep[i].time == -1)
		{
			Rep[i].num = waitRep.top().num;
			Rep[i].time = init_Rep[i];
			waitRep.pop();
		}
	}
}
void work_Rep()
{
	if (Rep[B].num > 0)
	{
		Repp.insert(Rep[B].num);
	}

	for (int i = 1; i <= M; i++)
	{
		if (Rep[i].time > 0 && Rep[i].num > 0) //창구에 사람있으면
		{
			Rep[i].time--; //시간--
		}
		if (Rep[i].time == 0 && Rep[i].num > 0) //사람있는데 시간이0이면
		{
			Rep[i].time = -1; //정비창구초기화
			Rep[i].num = -1;
			Allpeople--;
		}
	}

	
}

void init_All()
{
	N = 0, M = 0, K = 0, A = 0, B = 0, Time = 0;
	memset(init_Rec, 0, sizeof(init_Rec));
	memset(init_Rep, 0, sizeof(init_Rep));
	memset(People, 0, sizeof(People));
	memset(check, false, sizeof(check));
	Recc.clear();
	Repp.clear();
}
