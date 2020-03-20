#include <iostream>

using namespace std;

int a[304][304],dp[304][304],N,M,rt,i,j,x,y;

int printSum(int i, int j, int x, int y) {

    return dp[x-1][y-1]-dp[i][j-2];
}

void saveDp() {
    dp[0][0] = a[0][0];
    for (int j = 0; j < M;j++) {
        for (int i = 0; i < N; i++) {
            if (i == 0 && j == 0) continue;
            if (i == 0) dp[i][j] = dp[N-1][j-1]+ a[i][j];
            else dp[i][j] = dp[i - 1][j] + a[i][j];
        }
    }
    /*
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << dp[i][j] << " ";
        }
        cout << "\n";
    }
    */
}

int main()
{
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> a[i][j];
        }
    }
    saveDp();
    
    cin >> rt;
    for (int i = 0; i < rt; i++) {
        cin >> i >> j >> x >> y;
        cout << printSum(i, j, x, y) << "\n";
    }
    
    
}
