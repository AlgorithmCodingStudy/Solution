#include <cstdio>

/* 1번째 동전부터 n번째 동전까지 사용하는 경우
2번째 동전부터 n번째 동전까지 사용하는 경우
....
n번째 동전만 사용하는 경우
*/
int main() {
    int n, k;
    int coins[101];
    int d[10001] = {0};

    scanf("%d %d", &n, &k);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &coins[i]);
    }
    
    d[0] = 1;

    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            if (j >= coins[i]) {
                d[j] += d[j-coins[i]];
            }
        }
    }

    printf("%d\n", d[k]);

    return 0;
}
