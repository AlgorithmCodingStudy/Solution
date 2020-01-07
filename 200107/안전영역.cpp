#include <iostream>
#include <queue>
#include <vector> //max
#include <algorithm> //max
using namespace std;

int N = 0;

int originalMap[100][100] = { 0 }; //비 상태 받을 배열
int paintedMap[100][100] = { 0 }; //새로 영역 구분할 배열
int visited[100][100] = { 0 };

void paintSafezone(int rain) {
    for (int a = 0; a < N; a++) {
        for (int b = 0; b < N; b++) {
            if (originalMap[a][b] <= rain) {
                paintedMap[a][b] = 0;
            }
            else {
                paintedMap[a][b] = 1;
            }
        }
    }
}

int bfs() {
    queue<pair <int, int>> q; //pair 빼먹지 말기
    int dx[4] = { -1,1,0,0 };
    int dy[4] = { 0,0,-1,1 };
    int cnt = 1;
    for (int c = 0; c < N; c++) {
        for (int d = 0; d < N; d++) {

            if (paintedMap[c][d] == 1 && visited[c][d] == 0)
            {
                visited[c][d] = 1;
                q.push(make_pair(c, d));
            }

            while (!q.empty()) {

                int x = q.front().first;
                int y = q.front().second;
                q.pop();

                for (int e = 0; e < 4; e++) {
                    int nx = x + dx[e];
                    int ny = y + dy[e];

                    if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                        if (paintedMap[nx][ny] == 1 && visited[nx][ny] == 0) {
                            q.push(make_pair(nx, ny));
                            visited[nx][ny] = 1;
                        }
                    }
                }
            }

            if (q.empty()) cnt++;
        }
    }
    return cnt;
}

int main()
{
    vector<int> calculatedZone;
    int max = 0;
    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> originalMap[i][j];

            if (max < originalMap[i][j]) {
                max = originalMap[i][j];
            }
        }
    }

    for (int k = 1; k < max; k++) {

        paintSafezone(k);
        int size = bfs();
        cout << size << endl;

        //calculatedZone.push_back(size);

    }

    //cout << *max_element(calculatedZone.begin(), calculatedZone.end());
}
