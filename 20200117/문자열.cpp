#include <iostream>
using namespace std;

int main() {
	string A, B;
	cin >> A >> B;
	int alen = A.length();
	int blen = B.length();
	int diff = blen - alen + 1;
	int right = 0, min = 100;
	

	for (int i = 0; i < diff; i++) {
		right = 0;
		for (int a = 0; a < alen; a++) {
			if (A[a] != B[a + i]) right++;
		}
		if (min > right) min = right;
	}
	cout << min;
}
