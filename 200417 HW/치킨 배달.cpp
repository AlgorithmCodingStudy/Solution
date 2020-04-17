#include <iostream>
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;

int N, M,a[54][54],INF=987654321;
vector<pair<int,int>> chickList, homeList;
vector<vector<int>> realChick;
vector<int> v,ans; 

void combi(int start, vector<int>& v) {
	if (v.size() == M) {
		realChick.push_back(v);
		return;
	}
	for (int i = start + 1; i < chickList.size(); i++) {
		v.push_back(i);
		combi(i, v);
		v.pop_back();
	}
}
int main() {
	cin >> N >> M;
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> a[i][j];
			if (a[i][j] == 1) homeList.push_back({ i,j });
			if (a[i][j] == 2) chickList.push_back({ i,j });
		}
	}
	combi(-1,  v);
	for (vector<int> c : realChick) {
		int sum = 0;		
			for (pair<int, int> h : homeList) {
				int y = h.first;
				int x = h.second;
				int MIN = INF;
				for (int idx : c) {
					int cy = chickList[idx].first;
					int cx = chickList[idx].second;					
					int d=abs(y-cy) + abs(x-cx);
					MIN = min(MIN, d);
				}
			sum += MIN;
		}
		ans.push_back(sum);
	}
	sort(ans.begin(), ans.end());
	cout << ans[0];	
}
