#include <iostream>
#include<vector>
using namespace std;

class Solution{
public:
    vector<int> twoSum(vector<int> &num, int target){
        int len = num.size();
        vector<int> result;
        int i = 0;
        int j = len - 1;

        while(i < j){
            int x = num[i] + num[j];
            if(x == target){
                result.push_back(num[i]);
                result.push_back(num[j]);
                i++;
                j++;
            }
            else if(x > target)
                j--;
            else
                i++;
        }
        return result;
    }
};

int main() {
    cout << "Hello, World!" << endl;
    vector<int> n({2, 7, 11, 17});
    int target = 9;
    Solution s;
    vector<int> result;
    result = s.twoSum(n, target);
    vector<int>::iterator it;
    for(it=result.begin(); it != result.end(); it++)
        cout << *it << endl;
    return 0;
}