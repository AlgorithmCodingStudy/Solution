#include <iostream>
using namespace std;

int main() {
	int L = 0, A = 0, B = 0, C = 0, D = 0;
	cin >> L >> A >> B >> C >> D;
	int aday = 0, bday = 0;
	if (A % C != 0) {
		aday += 1;
	}
	aday += A / C;
	if (B % D != 0) {
		bday += 1;
	}
	bday += B / D;
	if (aday > bday) cout << L - aday;
	else cout << L - bday;
}
