#include <iostream>
#include <algorithm>
#include <vector>

using namespace std; 
#pragma warning(disable:4996)
#define INF 987654321
int main() {
    int n;
    int n_idx = 1;
    cin >> n;

    vector<int> num_vec(n + 1, 987654321), ascend_vec;
    
  for (int n_idx = 1; n_idx <= n; n_idx++)
      cin >> num_vec[n_idx];
        
    
  
    ascend_vec.push_back(num_vec[n_idx++]);
  
    for (n_idx = 2; n_idx <= n; n_idx++){
        auto idx = lower_bound(ascend_vec.begin(), ascend_vec.end(), num_vec[n_idx]);
       
        if (idx == ascend_vec.end())
            ascend_vec.push_back(num_vec[n_idx]);
      
        else
            *idx = num_vec[n_idx];
    }
    cout << ascend_vec.size()<<endl;
    
    return 0;
}

