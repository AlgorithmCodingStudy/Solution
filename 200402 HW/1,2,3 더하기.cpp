#include <iostream>
using namespace std;
int n,T,dp[11];

int go(int num) {
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    for (int i = 4; i <= num; i++) {
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1];
    }
    return dp[n];
}
int main()
{
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> n;
        cout << go(n)<<"\n";
    }
}
