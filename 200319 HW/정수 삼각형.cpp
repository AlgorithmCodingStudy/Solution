#include <iostream>
#include <algorithm>
using namespace std;
int n,ans, a[504][504],dp[504][504];
int go() {
    
    dp[0][0] = a[0][0];
    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            if (j == 0) dp[i][j] = dp[i - 1][j] + a[i][j];
            if (j == i)dp[i][j] = dp[i - 1][j - 1] + a[i][j];
            dp[i][j] = max(dp[i - 1][j - 1] + a[i][j], dp[i - 1][j] + a[i][j]);
            if (i == n - 1) ans = max(dp[i][j], ans);
        }
    }
    return ans;
}
int main()
{
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i + 1; j++) {
            cin >> a[i][j];
        }
    }
    cout<<go();
}
