#include <iostream>
#include <vector>
using namespace std;

int N, M, K,R,C,sticker[10][10],arr[40][40],sticker_r[10][10];
vector<pair<int, int>> v;

bool rangeCheck(int r,int c) {
    
    int cnt = 0;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (i < 0 || i >= N || j < 0 || j >= M) return false;
                if (sticker[i][j] == 1) {
                    cnt++;
                    if (arr[i][j] == 0) {
                        v.push_back({ i,j });
                    }
                }
            
        }
    }
    if (cnt == v.size())return true;
    else return false;
}
void rotate(int r,int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            sticker_r[j][r-1-i] = sticker[i][j];
        }
    }
    /*
    for (int i = 0; i < c; i++) {
        for (int j = 0; j < r; j++) {
            cout << sticker_r[i][j] << " ";
        }
        cout << "\n";
    }
    */
}
void printArr() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
}

int main()
{
    int t = 3;
    cin >> N >> M >> K;
    for (int i = 0; i < K; i++) {
        cin >> R >> C;
        
        for (int j = 0; j < R; j++) {
            for (int k = 0; k < C; k++) {
                cin >> sticker[j][k];
            }
        }
        if (rangeCheck(R, C)) {
            for (auto a : v) {
                arr[a.first][a.second] = 1;
            }
            //printArr();
        }
        else {
            while (t--) {
                rotate(R, C);

            }
            

        }
    }
}
