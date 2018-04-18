class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int len = nums.size();
        vector<int> result;
        for(int i = 0; i < len; i++)
        {
            for(int j = i+1; j < len; j++)
            {
                int res = nums[i] + nums[j];
                if(res == target)
                {
                    result.push_back(i);
                    result.push_back(j);
                }
            }
        }
        return result;
    
    }
};


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result(2);
        unordered_map<int, int> hash;
        int len = nums.size();
        for(int i = 0; i < len; ++i)
            hash[nums[i]] = i;
        for(int i = 0; i < len; ++i)
        {
            int needNum = target - nums[i];
            if((hash.find(needNum) != hash.end()) and hash[needNum] != i)
            {
                result[0] = i;
                result[1] = hash[needNum];
            }
        }
        return result;
    }
};


