#include <iostream>

#include <queue>

1. 0없으면 0출력
2.BFS
3.큐 비었을 때 0 있으면 -1 출력
4. 큐 비었을 때 0 없으면 MAX-1 출력





using namespace std;

 

const int MAX = 100;

 

typedef struct

{

        int y, x, z;

}Dir;

 

Dir moveDir[6] = { {1, 0, 0}, {-1, 0, 0}, {0, 1, 0}, {0, -1, 0}, {0, 0, 1}, {0, 0, -1} };

 

int M, N, H;

int tomato[MAX][MAX][MAX];

queue<pair<pair<int, int>, int>> q;

int noTomato;

 



bool allRipe(void)

{

        int possible = M * N*H - noTomato; 

        int cnt = 0;

 

        for (int i = 0; i < H; i++)

                 for (int j = 0; j < N; j++)

                         for (int k = 0; k < M; k++)

                                 if (tomato[j][k][i] == 1)

                                          cnt++;

 
      //토마토 넣을 수 있는 칸에 토마토가 다 익었으면(다 )
        return possible == cnt;

}

 

int BFS(void)

{

        int day = 0;

 

        //처음부터 익힐 수 있는 토마토가 없는 경우

        if (q.empty())

                 return -1;

 

        while (!q.empty())

        {

                 int currentSize = q.size();

 

                 for (int i = 0; i < currentSize; i++)

                 {

                         int y = q.front().first.first;

                         int x = q.front().first.second;

                         int z = q.front().second;

 
                        //인접한 여섯 군데에 대하여
                         for (int i = 0; i < 6; i++)

                         {

                                 int nextY = y + moveDir[i].y;

                                 int nextX = x + moveDir[i].x;

                                 int nextZ = z + moveDir[i].z;

 

                                 // 배열 범위 안 벗어나고 안 익은 토마토인 경우
                                

                                 if (0 <= nextY && nextY < N && 0 <= nextX && nextX < M && 0 <= nextZ && nextZ < H)

                                          if (tomato[nextY][nextX][nextZ] == 0)

                                          {

                                                  tomato[nextY][nextX][nextZ] = 1;

                                                  q.push(make_pair(make_pair(nextY, nextX), nextZ));

                                          }

                         }

                         q.pop();

 

                         //큐가 비고 다 익혔으면 일수 리턴

                         if (q.size() == 0 && allRipe())

                                 return day;

                         //큐는 비었는 데 안 익은 게 있

                         else if (q.size() == 0 && !allRipe())

                                 return -1;

                 }

                 day++;

        }

}

 

int main(void)

{

        cin >> M >> N >> H;

 
  //3차원 배열에 토마토 입력
        for (int i = 0; i < H; i++)

                 for (int j = 0; j < N; j++)

                         for (int k = 0; k < M; k++)

                         {

                                 cin >> tomato[j][k][i];

                                 if (tomato[j][k][i] == 1)

                                          q.push(make_pair(make_pair(j, k), i)); 

                                 if (tomato[j][k][i] == -1)

                                          noTomato++; // 토마토 넣을 수 없는 수

                         }

 

        if (q.size() == M * N*H - noTomato)

        {

                 cout << 0 << endl; // 처음부터 모든 토마토가 익은 

        }

        else

        {

                 int result = BFS();

                 cout << result << endl;

        }

        return 0;

}

