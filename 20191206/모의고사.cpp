#include <cstring>
#include <string>
#include <vector>
using namespace std;

int a[5] = { 1, 2, 3, 4, 5 };
int b[8] = { 2, 1, 2, 3, 2, 4, 2, 5 };
int c[10] = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };

vector<int> solution(vector<int> answers) {
	vector<int> answer;
	int score[3];
	
  memset(score, 0, sizeof(score));
/*
  for (int i = 0; i < answers.size(); i++)
	{
		for (int j = 0; j < 3; j++) {
			if (answers[i] == v[j][i%v[j].size()]){
				cnt[j]++;
				m = max(m, cnt[j]);
			}
		}
	}
  
  */
	for (int i = 0; i < answers.size(); i++) {
		if (answers[i] == a[i % 5]) {
			score[0] += 1;
		}
	}

	for (int i = 0; i < answers.size(); i++) {
		if (answers[i] == b[i % 8]) {
			score[1] += 1;
		}
	}

	for (int i = 0; i < answers.size(); i++) {
		if (answers[i] == c[i % 10]) {
			score[2] += 1;
		}
	}

	int maxv = -1;
	for (int i = 0; i < 3; i++) {
		if (maxv == -1 || score[i] > maxv) {
			maxv = score[i];
		}
	}

	for (int i = 0; i < 3; i++) {
		if (score[i] == maxv) {
			answer.push_back(i + 1);
		}
	}

	return answer;
}
