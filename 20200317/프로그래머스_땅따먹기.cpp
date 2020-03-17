#include <iostream>
#include <vector>
#include<algorithm>
#include<cstring>

using namespace std;

int MMax = -999999;
int result = -99999;
int memo[5];
bool flag;

void Go_eating(int curcol, int currow, int start,vector<vector<int> > land);

int solution(vector<vector<int> > land)
{
     int answer = 0;

    for (int row = 0; row < 4; row++) {

        memset(memo, 0, sizeof(memo));
        memo[row] = land[0][row];
        flag = false;
        Go_eating(1, row,row,land);
    }

    answer = result;

    return answer;
}


void Go_eating(int curcol, int currow,int start, vector<vector<int> > land)
{
  
    if (curcol == land.size()) {
        result = max(result, MMax);
        MMax = 0;
        flag = true;
        return;
    }

    for (int j = 0; j < 4; j++)
    {
        if (j == currow)continue;
        memo[j] = memo[currow] + land[curcol][j];
    }

    MMax = *max_element(memo, memo + 4);
  
    for (int j = 0; j < 4; j++)
    {
        if (memo[j] == MMax) {
            Go_eating(curcol + 1, j, start, land);
            if (flag) return;
        }
    }
    
}
