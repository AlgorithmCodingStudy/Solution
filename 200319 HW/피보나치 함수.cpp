#include<iostream>
#include<cstring>

using namespace std;
int N,rt,dp[44];

int fibonacci(int n) {
    
    if (n == 0) return dp[0] = 0;  
    if (n == 1) return dp[1] = 1;
    
    if (dp[n] != -1) return dp[n];
    else return dp[n] = fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    memset(dp, -1, sizeof(dp));
    cin >> rt;
    
    for (int i = 0; i < rt; i++) {       
        cin >> N;
        if (N == 0) {
            cout << 1 << " " << 0 << "\n";
        }
        else if (N == 1) {
            cout << 0 << " " << 1 << "\n";
        }
        else {
            fibonacci(N);
            cout << dp[N-1] << " " << dp[N] << "\n";
        }
    }  
}
