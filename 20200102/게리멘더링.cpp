#include<iostream>
#include<algorithm>
 
#define endl "\n"
#define MAX 20
using namespace std;
 
struct COORD
{
    int x;
    int y;
};
 
int N, Answer = 987654321;
int MAP[MAX][MAX];
int Label[MAX][MAX];
COORD Pos[4];
 
int Min(int A, int B) { if (A < B) return A; return B; }
 
void Input()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> MAP[i][j];
        }
    }
}
 
bool CanMakeLine(int x, int y, int d1, int d2)
{
    
    
    if (x + d1 >= N || y - d1 < 0) return false;
    if (x + d2 >= N || y + d2 >= N) return false;
    if (x + d1 + d2 >= N || y - d1 + d2 >= N) return false;
    if (x + d2 + d1 >= N || y + d2 - d1 < 0) return false;
 
    return true;
}
 
void Calculate()
{
    
    
    int Sum[6] = { 0, 0, 0, 0, 0, 0};
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            Sum[Label[i][j]] = Sum[Label[i][j]] + MAP[i][j];
        }
    }
    sort(Sum, Sum + 6);
    int Diff = Sum[5] - Sum[1];
    Answer = Min(Answer, Diff);
}
 
 
void Labeling(int a, int b, int c, int d)
{
    
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            Label[i][j] = 5;
        }
    }
 
    
    
    int SubArea = 0;
    for (int i = 0; i < Pos[1].x; i++)
    {
        if (i >= Pos[0].x) SubArea++;
        for (int j = 0; j <= Pos[0].y - SubArea; j++)
        {
            Label[i][j] = 1;
        }
    }
 
  
  
    int PlusArea = 0;
    for (int i = 0; i <= Pos[2].x; i++)
    {
        if (i > Pos[0].x) PlusArea++;
        for (int j = Pos[0].y + 1 + PlusArea; j < N; j++)
        {
            Label[i][j] = 2;
        }
    } 
 
   
   
    SubArea = 0;
    for (int i = N - 1; i >= Pos[1].x; i--)
    {
        if (i < Pos[3].x) SubArea++;
        for (int j = 0; j < Pos[3].y - SubArea; j++)
        {
            Label[i][j] = 3;
        }
    }
 
    
    
    PlusArea = 0;
    for (int i = N - 1; i > Pos[2].x; i--)
    {
        if (i <= Pos[3].x) PlusArea++;
        for (int j = Pos[3].y + PlusArea; j < N; j++)
        {
            Label[i][j] = 4;
        }
    }
 
    Calculate();
}
 
void Solution()
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 1; j < N; j++)
        {
            for (int D1 = 1; D1 <= j; D1++)           
            
            {
                for (int D2 = 1 ; D2 < N - j; D2++)    
                
                {
                    if (CanMakeLine(i, j, D1, D2) == true)        
                   
                   
                    {
                        Pos[0].x = i; Pos[0].y = j;
                        Pos[1].x = i + D1; Pos[1].y = j - D1;
                        Pos[2].x = i + D2; Pos[2].y = j + D2;
                        Pos[3].x = i + D1 + D2; Pos[3].y = j - D1 + D2;
                        Labeling(i, j, D1, D2);
                    }
                }
            }
        }
    }
    cout << Answer << endl;
}
 
void Solve()
{
    Input();
    Solution();
}

 
int main(void)
{
    
    Solve();
 
  
  
  
  
  
}


