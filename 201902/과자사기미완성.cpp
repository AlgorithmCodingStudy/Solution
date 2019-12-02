#include <iostream>

using namespace std;



int main(){
    
    //int weight[3];
    //int price[3];
    int gsb[3];
    for(int i=0;i<3;i++){
        int weight=0, price=0, whap=0, phap=0;
        
        cin>> price >> weight;
        
        whap = weight * 10;
        phap = price *10;
        if(phap > 5000) phap -= 500;
        gsb[i] = whap/phap;
    }
    /*
    for(int j=0;j<3;j++){
        
        int whap = weight[j] * 10;
        int phap = price[j] *10;
        if(phap > 5000) phap -= 500;
        gsb[j] = whap/phap;
        
    }
    */
    int index=0;
    for(int k=0;k<2;k++){
        
        if(gsb[k]>gsb[k+1]) index = k;
    }
    char answer;
    if(index == 0) answer='S';
    else if(index == 1) answer = 'N';
    else answer = 'U';
    
    cout << answer;
    return 0;
}