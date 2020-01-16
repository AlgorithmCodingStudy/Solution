#include <iostream>

using namespace std;

int arr[14] = { 0 };
int arr2[14] = { 0 };
int K=0;
void DFS(int Start, int Depth)
{
    int i;
    if (Depth == 6)
    {
        for (i = 0; i < 6; i++)
        {
            cout << arr2[i]<<" ";
        }
        cout << "\n";
    }
    else
    {
        for (i = Start; i < K; i++)
        {
            arr2[Depth] = arr[i];
            DFS(i + 1, Depth + 1);
        }

    }
}

int main()
{
    int i;

    while (1)
    {
        cin >> K;
        if (K == 0)
            break;
        for (i = 0; i < K; i++)
            cin >> arr[i];
        DFS(0, 0);
        cout << "\n";
    }
}
