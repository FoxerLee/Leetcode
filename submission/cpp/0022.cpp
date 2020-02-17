class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        miao(res, "", n, 0);
        
        return res;
    }
    
    void miao(vector<string> &v, string s, int n, int m) {
        if (n == 0 && m == 0) {
            v.push_back(s);
        }
        if (n > 0) {
            miao(v, s+"(", n-1, m+1);
        }
        if (m > 0) {
            miao(v, s+")", n, m-1);
        }
        
    }
};
