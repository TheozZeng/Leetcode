#include <iostream>
#include <string>
using namespace std;


class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int m = strs.size();
        if(m == 0){
            return "";
        }
        if(m == 1){
            return strs[0];
        }
        
        string conmon_str = strs[0];
        
        for(i=0;i<m;i++){
            string str_i = strs[i];
            int len_i = str_i.size();
        }
        
    }
};


int main(){
    cout << "xxxxxxxxxxxxxxxxx"<< endl;
}