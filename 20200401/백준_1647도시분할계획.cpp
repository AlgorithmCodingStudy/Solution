#include<iostream>
#include<vector>
#include<algorithm>

#define ll long long
using namespace std;

struct Edge {ll from, to, weight;
bool operator<(const Edge& A) const
{
	return weight < A.weight;
};
};

vector<Edge>E;
vector<ll>R;

ll N, M;
ll Parent[100010];
ll Height[100010];

int findParent(int a);
void merge(int a, int b);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	ll result = 0;

	cin >> N >> M;
	for (int i = 0; i <M; i++)
	{
		ll a, b, c;
		cin >> a >> b >> c;
		E.push_back({ a,b,c });
	}

	sort(E.begin(), E.end());

	for (int i = 1; i <= N; i++)
	{
		Parent[i] = i;
	}
	
	
	for (int i = 0; i < E.size(); i++)
	{
		if (findParent(E[i].from) == findParent(E[i].to)) continue;
		result += E[i].weight;
		R.push_back(E[i].weight);
		merge(E[i].from, E[i].to);
	}


	cout << result-R[R.size()-1]<< endl;

	return 0;
}


int findParent(int a)
{
	
	if (Parent[a] == a) return a;
	return Parent[a] = findParent(Parent[a]);
}

void merge(int a, int b)
{

	int roota = findParent(a);
	int rootb = findParent(b);

	if (roota == rootb) return;
	
	Parent[roota] = rootb;
}

