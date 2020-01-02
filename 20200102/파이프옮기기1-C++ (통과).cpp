#include<iostream>
#include<queue>
#include <algorithm>
#include <vector>

using namespace std;
int N;
int house[16][16];
int dr[] = {0,1,1};
int dc[] = {1,1,0};
struct data{
	int row;
	int col;
	int position;
	data(int r, int c, int p){
		row = r;
		col = c;
		position = p;
	};
};
queue<data> q;
int caseCount;
bool rangeCheck(int nr, int nc) {
		if(nr>=0 && nr<N && nc>=0 && nc<N) return true;
		return false;
	};
void pushRight(data currentPipe) {//오른쪽으로 밀기
	int cr = currentPipe.row;
	int cc = currentPipe.col;
		int nr = cr+dr[0];
		int nc = cc+dc[0];
		if(rangeCheck(nr,nc) && house[nr][nc]!=1){//경계 만족하고 벽도 아니고
			q.push(data(nr,nc,0));//다음칸으로 전진
		}		
	};
void pushRightBottom(data currentPipe) { //대각선으로 밀기
	int cr = currentPipe.row;
	int cc = currentPipe.col;
		int nr = cr+dr[1];
		int nc = cc+dc[1];
		if(rangeCheck(nr,nc) && house[nr][nc]!=1){//경계 만족하고 벽도 아니면 
			if(house[cr+1][cc]!=1 && house[cr][cc+1]!=1){//오른쪽,아래가 벽이 아니면				
				q.push(data(nr,nc,1));//다음칸으로 전진
			}
		}
	};
void pushBottom(data currentPipe) { //아래방향으로 밀기
	int cr = currentPipe.row;
	int cc = currentPipe.col;
		int nr = cr+dr[2];
		int nc = cc+dc[2];
		if(rangeCheck(nr,nc) && house[nr][nc]!=1){//경계 만족하고 벽도 아니고
				q.push(data(nr,nc,2));//다음칸으로 전진
		}	
	};

void push(data currentPipe) {
	int position = currentPipe.position;

	if(currentPipe.row==(N-1) && currentPipe.col==(N-1)) {//끝에 도달 했으면
			caseCount++;
			return;
		}
		switch (position) {//현재 파이프 상태가
		case 0://오른쪽으로 누워있는 상태
			pushRight(currentPipe);
			pushRightBottom(currentPipe);
			break;
		case 1://오른쪽아래로로 누워있는 상태
			pushRight(currentPipe);
			pushRightBottom(currentPipe);
			pushBottom(currentPipe);
			break;
		case 2://아래방향으로 누워있는 상태		
			pushBottom(currentPipe);
			pushRightBottom(currentPipe);
			break;
		}
	};


void bfs(){
	q.push(data(0,1,0));//head의 row,col,누워있는 상태(우)
	while(!q.empty()){
			int size = q.size();
			for(int i=0;i<size;i++) {
				data currentPipe = q.front();//현재 파이프에 대해서
				q.pop();
				push(currentPipe);
			}
		}
};


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    cin >> N;
	for(int row=0;row<N;row++)
		for(int col=0;col<N;col++)cin>>house[row][col];
	bfs();

	cout<<caseCount;
    return 0;
}