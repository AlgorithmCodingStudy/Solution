#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

int dp[3][1004][34], t, w, a[1004];

int go(int here_tree, int idx, int cnt) {
    
    if (idx == t) return 0;

    if (dp[here_tree][idx][cnt] != -1) return dp[here_tree][idx][cnt];

    int& ret = dp[here_tree][idx][cnt];
    ret = 0;

    int value = (a[idx] == here_tree) ? 1 : 0;
    int next_tree = (here_tree == 1) ? 2 : 1;

    if (cnt < w) ret = max(go(next_tree, idx + 1, cnt + 1) + !value, go(here_tree, idx + 1, cnt) + value);
    else ret = go(here_tree, idx + 1, cnt) + value;
    return ret;
}

int main() {
    cin >> t >> w;
    for (int i = 0; i < t; i++) {
        cin >> a[i];
    }
    memset(dp, -1, sizeof(dp));
    cout << go(1, 0, 0);
}
