class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> combination;
        recursion(candidates, res, combination, target, 0);
        return res;
    }
    
    void recursion(vector<int> &candidates, vector<vector<int>> &res, vector<int> &combination, int target, int opp) {
        if (target == 0) {
                res.push_back(combination);
                //combination.clear();
        }
        
        for (int i = opp; i < candidates.size() && target >= candidates[i]; i++) {
            combination.push_back(candidates[i]);
            recursion(candidates, res, combination, target - candidates[i], i);
            combination.pop_back();
        }
    }
};
