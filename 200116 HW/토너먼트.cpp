#include <iostream>
using namespace std;

int main() {
    int N = 0, K = 0, L = 0,cnt=0;
    cin >> N >> K >> L;
    while (K != L) {   
        K = (K + 1) / 2;
        L = (L + 1) / 2;
        cnt++;
    }
    cout << cnt;
}
