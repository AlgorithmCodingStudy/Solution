// 200221 알고리즘 스터디.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <queue>
using namespace std;
queue<int> q;
int air_R,air_C,R, C, T, temp[50][50],arr[50][50], visited[50][50], dx[4] = { -1,1,0,0 }, dy[4] = { 0,0,-1,1 };
void spread(int y,int x) {
    int cnt = 0,num=0;
    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny < 0 || ny >= R || nx < 0 || nx >= C)continue;
        if (arr[ny][nx] == -1) continue;
        num = arr[y][x] / 5;
        temp[ny][nx] += num;
        cnt++;
    }
    temp[y][x] += arr[y][x] - (num * cnt);
}
void spreadAll() {
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (arr[i][j] >= 1) spread(i,j);
        }
    }
}

int main()
{
    cin >> R >> C >> T;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == -1) {
                air_R = i;
                air_C = j;
                
            }
        }
    }
    spreadAll();
    
    
}


