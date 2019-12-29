#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int N,M;
int maxValue;
int cnt;
int hackingCount[10001];
int visit[10001];
int startNumber;
vector<int> relationadjList[10001];
set<int> hackingCase;

void printAnswer(){
	for(int num=1;num<=N;num++){
		if(hackingCount[num]==maxValue){
		cout<<num<<" ";
		}
	}
};

void updateHackingCount(int computherNumber){
	hackingCount[computherNumber] = cnt;
	maxValue = max(maxValue,hackingCount[computherNumber]);
};

void dfs(int currentComputerNumber){
	int caseSize = relationadjList[currentComputerNumber].size();
	for(int target=0;target<caseSize;target++){
		int targetNumber = relationadjList[currentComputerNumber].at(target);
		if(visit[targetNumber]!=startNumber){
			cnt++;
			visit[targetNumber]=startNumber;
			dfs(targetNumber);
		}
	}
};
void hacking(){
	for(std::set<int>::iterator it=hackingCase.begin();it!=hackingCase.end();++it){
		cnt =0;
		startNumber = *it;
		visit[*it] = *it;
		dfs(*it);
		updateHackingCount(*it);
	}//해킹케이스들에 대해서 
};
int main(void){
	cin>>N>>M;
	for(int i=0;i<M;i++){
		int A,B;
		cin>>A>>B;
		relationadjList[B].push_back(A);
		hackingCase.insert(B);
	}//입력

	hacking();

	printAnswer();
}
