/*
처음에 문제 잘못이해했는데 석현쓰가 잘못이해했다고 알려줬따!!!
예제3번 답 0 맞는데, 빠꾸짓하느라 한시간날림....ㅎ
*/

#include<iostream>
#include<queue>
#include<vector>
#include<algorithm> //abs헤더

/*
 0: 빈칸, 1: 벽
*/

using namespace std;

int N;
int house[20][20] = { 0 };
struct Pipe { int x1, y1, x2, y2; };
queue <Pipe>Q;
vector<int>V;

void BFS()
{
    while (!Q.empty())
    {
        int cx1 = Q.front().x1;
        int cy1 = Q.front().y1;
        int cx2 = Q.front().x2;
        int cy2 = Q.front().y2;
        Q.pop();
        

        if (cx2 == N && cy2 == N) 
        {
            V.push_back(1); //여기서 리턴해버리면 계속 답이 1, 도착하는방법이 여러경우가 있을수도 있으니까 여기서 리턴하면안됨
        }


        if (cx1 == cx2) // 가로
        {
            // 1. '->' 인 경우
            int nx1 = cx2;
            int ny1 = cy2;
            int nx2 = cx2;
            int ny2 = cy2+1;
           
            if (nx2 > 0 && ny2 > 0 && nx2 <= N && ny2 <= N){ //원래는 continue이용해서 범위처리 하려했지만, continue처리하면 '->'경우만보고 '대각선'인경우는 넘어가버림 continue처리하면 안됨!
                if (house[nx2][ny2] == 0)
                {
                  Q.push({ nx1,ny1,nx2,ny2 });
                }
            }
          
          
            //2.'대각선' 인 경우
            nx1 = cx2;
            ny1 = cy2;
            nx2 = cx2 + 1;
            ny2 = cy2 + 1;
            if (nx2 > 0 && ny2 > 0 && nx2 <= N && ny2 <= N) {
                if (house[nx2][ny2] == 0 && house[nx1][ny2] == 0 && house[nx2][ny1] == 0)
                {
                    Q.push({ nx1,ny1,nx2,ny2 });
                }
            }
        }


        else if (cy1 == cy2) //세로
        {
        
            // 1. ↓
            int nx1 = cx2;
            int ny1 = cy2;
            int nx2 = cx2 + 1;
            int ny2 = cy2;

            if (nx2 > 0 && ny2 > 0 && nx2 <= N && ny2 <= N) {
                if (house[nx2][ny2] == 0)
                {
                    Q.push({ nx1,ny1,nx2,ny2 });
                }
            }


            // 2. 대각선
            nx1 = cx2;
            ny1 = cy2;
            nx2 = cx2 + 1;
            ny2 = cy2 + 1;

            if (nx2 > 0 && ny2 > 0 && nx2 <= N && ny2 <= N) {

                if (house[nx2][ny2] == 0 && house[nx1][ny2] == 0 && house[nx2][ny1] == 0)
                {
                    Q.push({ nx1,ny1,nx2,ny2 })
                }
            }
        }



        else if(abs(cx1-cx2) > 0 && abs(cy1 - cy2) > 0) //대각선
        {
        
            // 1. ->
            int nx1 = cx2;
            int ny1 = cy2;
            int nx2 = cx2;
            int ny2 = cy2 + 1;

            if (nx2 > 0 && ny2 > 0 && nx2 <= N && ny2 <= N) {
                if (house[nx2][ny2] == 0)
                {
                    Q.push({ nx1,ny1,nx2,ny2 });
                }
            }
             
             
            // 2. ↓
            nx1 = cx2;
            ny1 = cy2;
            nx2 = cx2 + 1;
            ny2 = cy2;

            if (nx2 > 0 && ny2 > 0 && nx2 <= N && ny2 <= N) {
                if (house[nx2][ny2] == 0)
                {
                    Q.push({ nx1,ny1,nx2,ny2 });
                }
            }

            // 3. 대각선
            nx1 = cx2;
            ny1 = cy2;
            nx2 = cx2 + 1;
            ny2 = cy2 + 1;

            if (nx2 > 0 && ny2 > 0 && nx2 <= N && ny2 <= N) {
                if (house[nx2][ny2] == 0 && house[nx1][ny2] == 0 && house[nx2][ny1] == 0)
                {
                    Q.push({ nx1,ny1,nx2,ny2 });
                }
            }       
        }
        
        
    }   
}


int main()
{

    //입력
    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            cin>>house[i][j];
        }
    }
    
    //동작
    Q.push({1,1,1,2}); //초기값
    BFS();
    
    //출력
    cout << V.size();
    
    return 0;
}
