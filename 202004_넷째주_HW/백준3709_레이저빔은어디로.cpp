#include<iostream>
#include<queue>
#include<cstring>

using namespace std;

struct Laser { int x, y, dir; };
int n,r,T;
int resultx, resulty;
bool Mirror[55][55];
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
queue<Laser>Q;

void init_test();
bool BFS();
int change(int dir);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> T;
	for (int i = 0; i < T; i++) {

		init_test();
		Laser L;

		cin >> n >> r;
		for (int i = 0; i < r; i++)
		{
			int x, y;
			cin >> x >> y;
			Mirror[x][y] = true;
		}

		cin >> L.x >> L.y;
		if (L.x < 1) {
			L.dir = 1;
			L.x++;
		}
		else if (L.x > n) {
			L.dir = 0;
			L.x--;
		}
		else if (L.y < 1) {
			L.dir = 3;
			L.y++;
		}
		else if (L.y > n) {
			L.dir = 2;
			L.y--;
		}


		Q.push({ L.x,L.y,L.dir });
		if (!BFS()) cout << 0;
		else
		{
			cout << resultx << " " << resulty << endl;
		}
	}
	return 0;
}

void init_test()
{
	n = 0; r = 0; resultx = 0; resulty = 0;
	memset(Mirror, false, sizeof(Mirror));
	while (!Q.empty())
	{
		Q.pop();
	}

}

bool BFS()
{
	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		int cd = Q.front().dir;
		//cout << cx << cy << cd << endl;
		Q.pop();

		if (cx < 1 || cy < 1 || cx > n || cy > n)
		{
			resultx = cx;
			resulty = cy;
			return true;
		}
		bool skip = false;
		int nx = cx; int ny = cy; int nd = cd;
		while (Mirror[nx][ny] != true )
		{
			if (nx<=0 || ny<=0 || nx>=n + 1 || ny>=n + 1)
			{
				skip = true;
				break;
			}
			nx += dx[cd];
			ny += dy[cd];
		}
		if (!skip) {
			nd = change(cd);
			nx += dx[nd];
			ny += dy[nd];
		}
		Q.push({ nx,ny,nd });
	}
	return false;
}

int change(int dir)
{
	if (dir == 0) return 3;
	else if (dir == 1) return 2;
	else if (dir == 2) return 0;
	else if (dir == 3) return 1;
}
