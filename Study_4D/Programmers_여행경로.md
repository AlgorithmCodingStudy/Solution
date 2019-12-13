```c
#include <string>
#include <vector>
#include<iostream>

using namespace std;

bool C[10000][10000] = {false};
bool can[10000] = {false};

string check(vector<vector<string>>tickets, string S)
{
    string start = "";
    for(int i = 0; i < tickets.size(); i++)
    { 
        if(C[i][0] == false) start = C[i][0];
        if(S == tickets[i][1]){
            if(C[i][1]==false){
                C[i][1] = true;
                C[i][0] = true;
            }
        }
    }
    return start;
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    
    for(int i = 0; i < tickets.size(); i++)
    {
        string S = tickets[i][0];
        string start = check(tickets,S);
        cout<<start;
    }
    
    string standard = "";
    
    for(int i = 0; i < tickets.size(); i++)
    {
        
        if(C[i][0] == false && can[i] == false)
        {
                answer.push_back(tickets[i][0]);
                answer.push_back(tickets[i][1]);
                standard = tickets[i][1];
                can[i] = true;
        }
        
        for(int j = 0; j < tickets.size(); j++)
        {
            if(can[j] == false){
                if(standard == tickets[j][0])
                {
                    can[i] = true;
                    standard = tickets[j][1];
                    answer.push_back(tickets[j][0]);
                    answer.push_back(tickets[j][1]);
                }
            }
        }
    }
    return answer;
}
```
