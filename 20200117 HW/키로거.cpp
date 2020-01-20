#include <iostream>
#include <list>


using namespace std;
int main() {

	int T = 0;
	cin >> T;

	for (int i = 0; i < T; i++) {
		string st = "";
		cin >> st;
		list<char> character;
		list<char>::iterator cursor = character.begin();

		for (int j = 0; j < st.length(); j++) {
			if (st[j] == '<') {
				if (cursor != character.begin()) cursor--;
				else continue; //1. break x 2. continue
			}

			else if (st[j] == '>') {
				if (cursor != character.end()) cursor++;
				else continue;
			}

			else if (st[j] == '-') {
				if (cursor != character.begin()) {
					cursor=character.erase((--cursor));
				}
				else continue;
			}
			else {
				character.insert(cursor, st[j]);			
			}
		}
		list<char>::iterator it;
		for (it = character.begin(); it != character.end(); it++) {
			cout << *it;
		}
		cout << "\n";
	}
}
