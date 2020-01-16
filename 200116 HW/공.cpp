#include <iostream>
#include <vector>

using namespace std;

int main() {
    int M = 0;
    cin >> M;
    //vector<int> arr{ 1,2,3 };
    int arr[3] = { 1,2,3 };
    for (int i = 0; i < M; i++) {
        int a=0, b = 0;
        cin >> a >> b;
        int ap = 0, bp = 0;
        for (int j = 0; j < 3; j++) {
            if (arr[j] == a) ap = j;
            if (arr[j] == b) bp = j;
        }
        int temp = 0;
        temp = arr[ap];
        arr[ap] = arr[bp];
        arr[bp] = temp;
    }
    cout << arr[0];
}
