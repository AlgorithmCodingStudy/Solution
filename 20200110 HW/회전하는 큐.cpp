#include <iostream>
#include <deque>
using namespace std;

int main() {
    int N = 0, M=0,cnt=0,idx=0;
    deque<int> arr;
    cin >> N >> M ;
    for (int i = 1; i <= N; i++) {
        arr.push_back(i);
    }    
    for (int j = 0; j < M; j++) {
        int num = 0;
        cin >> num;       
        for (int k = 0; k < arr.size(); k++) {
            idx = 0;
            if (arr[k] == num) {
                idx = k;
                break;
            }
        }
        int size = arr.size();
        if (idx < size - idx) {
            while (arr[0] != num) {
                int temp = arr.front();
                arr.pop_front();
                arr.push_back(temp);
                cnt++;
            }
            arr.pop_front();
        }
        else {
            //찾는 원소는 처음에서 찾았어야함
            while (arr[0] != num) {
                int temp = arr.back();
                arr.pop_back();
                arr.push_front(temp);
                cnt++;
            }
            arr.pop_front();
        }   
    }
    cout << cnt;
}
