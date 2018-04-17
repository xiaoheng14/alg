#include<iostream>
#include<vector>
using namespace std;

class Solution
{
	public:
		void FindNumsAppearOnce(vector<int> data)
		{
			int res = data[0];
			for(int i = 1; i < data.size(); i++)
			{
				res = res ^ data[i];
			}
			int cnt = 0;
			while(res % 2 !=1)
			{
				res = res >> 1;
				cnt += 1;
			}
			
			int num1 = 0, num2 = 0;
			for(int i = 0; i < data.size(); i++)
			{
				if((data[i] >> cnt) & 1){
					num1 ^= data[i];
				}
				else
				{
					num2 ^= data[i];
				}
			}
			cout << "num1 = " << num1 << endl;
			cout << "num2 = " << num2 << endl;
		}
};

int main()
{
	Solution s;
	vector<int> data = {1,2,3,4,3,4};
	s.FindNumsAppearOnce(data);
	return 0;
}
