class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size(); ) {
            int s = i + 1;
            int e = nums.size() - 1;
            
            while (s < e) {
                int sum = nums[i] + nums[s] + nums[e];
                if (sum == 0) {
                    res.push_back({nums[i], nums[s], nums[e]});
                    s += 1;
                    e -= 1;
                    while (s < e && nums[s] == nums[s-1]) s += 1;
                    while (s < e && nums[e] == nums[e+1]) e -= 1;
                }
                if (sum > 0) {
                    e -= 1;
                    while (s < e && nums[e] == nums[e+1]) e -= 1;
                }
                if (sum < 0) {
                    s += 1;
                    while (s < e && nums[s] == nums[s-1]) s += 1;
                }
            }
            i += 1;
            while (i < nums.size() && nums[i] == nums[i-1]) 
                i += 1;
        }
        
        return res;
    }
};
