#include <iostream>
#include <vector>
#include <queue>

using namespace std;
//괄호를 제대로 보자
//[]임
vector<int> people[101];
int relation[101] = { 0 };

int bfs(int people1, int people2) {

	queue<int> q;
	q.push(people1);

	while (!q.empty()) {
		int currentPeople=q.front();
		q.pop();

		if (currentPeople == people2) {
			return relation[currentPeople];
		}
			

		for (int i = 0; i < people[currentPeople].size(); i++) {
			int nextPeople = people[currentPeople][i];
			if (relation[nextPeople] == 0) {
				relation[nextPeople] = relation[currentPeople] + 1;
				q.push(nextPeople);

			}
		
		}

	}
	return -1;

}

int main() {

	int n = 0,p1=0,p2=0,m=0;

	cin >> n;
	cin >> p1 >> p2; 
	cin>> m;

	for (int i = 0; i < m; i++) {
		int x = 0, y = 0;
		cin >> x >> y;
		
		//인덱스는 []로 접근 push_back은 ()로 접근
		people[x].push_back(y);
		people[y].push_back(x);

		
	}

	cout << bfs(p1, p2) << endl;



	
}
