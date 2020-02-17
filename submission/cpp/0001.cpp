class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>obj;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target && i != j) {
                    obj.push_back(i);
                    obj.push_back(j);
                    return obj;
                }
                    
            }
        }      
    }
};
