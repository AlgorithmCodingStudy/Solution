#include <iostream>
#include <deque>
using namespace std;

int main() {
	//1.덱 선언
	//하나 남을 때까지 반복
	//2. 제일 앞에거 팝
	//3. 제일 앞에거 front로 확인해서 뒤에서 푸시
	//4. 제일 앞에거 리턴
	deque<int> dq;
	int N = 0;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		dq.push_back(i);
	}
	while (dq.size() != 1) {

		dq.pop_front();		
		int num = dq.front();
		dq.push_back(num);
		dq.pop_front();
		
	}
	cout << dq.front()<<"\n";
	return 0;

}
