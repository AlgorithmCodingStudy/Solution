#include <iostream>

#include <queue>

#include <string>

#include <cstring> //memset

using namespace std;



const int MAX = 100;



typedef struct

{

    int y, x;

}Dir;



Dir moveDir[4] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };



int N;

string graph[MAX];

bool visited[MAX][MAX];



void BFS(int y, int x, bool colorBlind)

{

    char search = graph[y][x]; //해당 칸의 색깔



    queue<pair<int, int>> q;

    q.push(make_pair(y, x));

    visited[y][x] = 1; 



    while (!q.empty())

    {

        int curY = q.front().first;

        int curX = q.front().second;

        q.pop();


        // 상하좌우에 대해서
        for (int i = 0; i < 4; i++)

        {

            int nextY = curY + moveDir[i].y;

            int nextX = curX + moveDir[i].x;



            if (0 <= nextY && nextY < N && 0 <= nextX && nextX < N) //1. 범위안에 있고

            {

                if (colorBlind == false) //2. 적록색맹이 아니라면

                {

                    if (graph[nextY][nextX] == search && !visited[nextY][nextX]) //3. 같은 색깔이고 방문 안 한칸을 찾는다.

                    {

                        visited[nextY][nextX] = true; // 4. 방문 표시하고

                        q.push(make_pair(nextY, nextX)); // 5. 큐에 넣고

                    }

                }

                else if (colorBlind == true) //2.적록색맹이라면

                {

                    if (search == 'R' || search == 'G') //3.빨간색과 초록색의 경우

                    {

                        if (!visited[nextY][nextX] && (graph[nextY][nextX] == 'R' || graph[nextY][nextX] == 'G')) // 방문 안 했고 빨간색과 초록색을 같이 인색 

                        {

                            visited[nextY][nextX] = true; //4. 방문 표시하고 큐에 넣음

                            q.push(make_pair(nextY, nextX));

                        }

                    }

                    else if (search == 'B') //3-1. 파란색은 

                    {

                        if (!visited[nextY][nextX] && (graph[nextY][nextX] == search)) // 3-1. 적록색맹이 아닌 경우랑 똑같이 처리

                        {

                            visited[nextY][nextX] = true;

                            q.push(make_pair(nextY, nextX));

                        }

                    }

                }

            }

        }

    }

}



int main(void)

{

    cin >> N;



    for (int i = 0; i < N; i++)

        cin >> graph[i];



    int cnt = 0;

    //1번째
    
    for (int i = 0; i < N; i++)

        for (int j = 0; j < N; j++)

            if (visited[i][j] == false)

            {

                BFS(i, j, false);

                cnt++; 

            }

    cout << cnt << " ";


    //2번째 돌리기 전에 visited 초기화
    memset(visited, false, sizeof(visited));

    cnt = 0;
    //2번째
    for (int i = 0; i < N; i++)

        for (int j = 0; j < N; j++)

            if (visited[i][j] == false)

            {

                BFS(i, j, true);

                cnt++;

            }

    cout << cnt << endl;



    return 0;

}
