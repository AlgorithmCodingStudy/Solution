#include <iostream>

#include <vector>

#include <algorithm>

using namespace std;



const int MAX = 100;



typedef struct

{

    int y, x;

}Dir;



Dir moveDir[4] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };



int graph[MAX][MAX];

bool visited[MAX][MAX];



int M, N, K;

int cnt; 




void DFS(int y, int x)

{

    visited[y][x] = true; //방문 처리

    cnt++; // 넓이 계산


    //상하좌우에 대해서
    for (int i = 0; i < 4; i++)

    {

        int nextY = y + moveDir[i].y;

        int nextX = x + moveDir[i].x;

        // M*N을 벗어나지 않고

        if (0 <= nextY && nextY < M && 0 <= nextX && nextX < N)
            
            //빈칸이면서 방문 안 했으면

            if (graph[nextY][nextX] == 0 && !visited[nextY][nextX])
                //다시 DFS 호출

                DFS(nextY, nextX);

    }

}



int main(void)

{

    cin >> M >> N >> K;



    for (int i = 0; i < K; i++)

    {

        int x1, y1, x2, y2;

        cin >> x1 >> y1 >> x2 >> y2;



        //영역 표시

        for (int y = y1; y < y2; y++)

            for (int x = x1; x < x2; x++)

                graph[y][x] = 1;

    }



    vector<int> result;



    for (int y = 0; y < M; y++)

        for (int x = 0; x < N; x++)
            //빈칸이고 방문 안 했으면

            if (graph[y][x] == 0 && !visited[y][x])

            {

                cnt = 0; //초기화

                DFS(y, x);

                //넓이 계산 끝난 거 넣기

                result.push_back(cnt);

            }

    //갯수 출력

    cout << result.size() << endl;



    sort(result.begin(), result.end()); //정렬

    for (int i = 0; i < result.size(); i++)

        cout << result[i] << " ";// 각각 넓이 출력

    cout << endl;



    return 0;

}
