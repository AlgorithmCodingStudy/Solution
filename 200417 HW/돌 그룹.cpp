#include <iostream>
#include <queue>
using namespace std;

int A, B, C, D;
bool check[1000][1000];

void bfs() {
    queue<pair<int, int>> q;
    q.push({ A,B });
    check[A][B] = true;
    while (!q.empty()) {
        int x = q.front().first, y = q.front().second; q.pop();
        int z = D - x - y;
        if (x == y && y == z) {
            cout << "1";
            return;
        }
        int nx[] = { x,x,y };
        int ny[] = { y,z,z };
        for (int i = 0; i < 3; i++) {
            int a = nx[i], b = ny[i];
            if (a < b)b -= a, a += a;
            else if (a > b)a -= b, b += b;
            else continue;
            int c = D - a - b;
            int X = min(min(a, b), c);
            int Y = max(max(a, b), c);
            if (!check[X][Y]) {
                q.push({ X,Y });
                check[X][Y] = true;
            }
        }
    }
    cout << "0";
}
int main()
{
    cin >> A >> B >> C;
    D = A + B + C;
    if (D % 3) {
        cout << "0";
        return 0;
    }
    else bfs();
    return 0;
}
