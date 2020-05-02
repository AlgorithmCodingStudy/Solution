#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int ret,n, m, k,a[20][20],g[20][20];
vector<int> map[20][20];
int dy[8] = { -1,-1,-1,0,0,1,1,1 };
int dx[8] = { -1,0,1,-1,1,-1,0 ,1};

void spring() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (map[i][j].size() == 0)continue;
            sort(map[i][j].begin(), map[i][j].end());
            for (int tree : map[i][j]) {
                if (tree <= g[i][j]) {
                    g[i][j] -= tree;
               }
                else {
                    g[i][j] += tree / 2;

                }

            }
        }       
    }
}


void fall() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (map[i][j].size()) {
                for (int tree : map[i][j]) {
                    if (tree % 5 == 0) {
                        for (int k = 0; k < 8; k++) {
                            int ny = i + dy[k];
                            int nx = j + dx[k];
                            if (ny < 0 || ny >= n || nx < 0 || nx >= n)continue;
                            g[ny][nx] = 5;

                        }
                    }
                }
                
            }
        }
    }
}
void winter() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; k < n; j++) {
            g[i][j] += a[i][j];
        }
    }
}

int main()
{
    cin >> n >> m >> k;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
        }
    }
    for (int i = 0; i < m; i++) {
        int x = 0, y = 0, z = 0;
        cin >> x >> y >> z;
        map[x-1][y-1].push_back(z);
    }
    for (int i = 0; i < k; i++) {
        //spring(); 
        fall(); winter();
    }
    
    
    cout << ret;
}
