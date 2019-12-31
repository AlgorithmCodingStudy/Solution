#include<iostream>
#include<queue>
using namespace std;
priority_queue<pair<int, int>> pq;
int N, L, A;
void slidingWindow(){
	    for (int i = 1; i <= N; ++i) {
        int value;
			cin >> value;
        pq.push({ -value, i });//마이너스로 넣으면 역순으로 나온다.
        while (pq.top().second < i - L + 1) pq.pop();//왼쪽 제거
        cout << -pq.top().first << ' ';
    }
};
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    cin >> N >> L;
	slidingWindow();

    return 0;
}