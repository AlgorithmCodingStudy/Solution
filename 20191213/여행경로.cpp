#include <string> 
#include <vector> 
#include <algorithm> 
#include <iostream>

using namespace std; 

bool dfs(string from, vector<vector<string>>& tickets, vector<bool>& visit, vector<string>& temp, vector<string>& answer, int cnt) { 
	temp.push_back(from); 
	if (cnt == tickets.size()) {
		answer = temp; 
		return true; 
	} 
	for (int i=0 ; i<tickets.size() ; i++) { 
		if (tickets[i][0] == from && visit[i] == false) { 
			visit[i] = true; 
			bool success = dfs(tickets[i][1], tickets, visit, temp, answer, cnt+1); 
			if (success) return true; 
			visit[i] = false; 
		} 
	} 
	temp.pop_back(); 
	return false; 
} 


int main() {
	vector<vector<string>> tickets = { {"ICN", "SFO"},{"ICN", "ATL"},{"SFO", "ATL"} ,{"ATL", "ICN"},{"ATL","SFO"} };
	vector<string> answer, temp;
	vector<bool> visit(tickets.size(), false);
	sort(tickets.begin(), tickets.end());
	dfs("ICN", tickets, visit, temp, answer, 0);
	


}
