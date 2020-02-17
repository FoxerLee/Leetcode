class Solution {
public:
    int reverse(int x) {
        int res = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (res > INT_MAX/10)
                return 0;
            if (res < INT_MIN/10)
                return 0;
            int temp = res * 10 + pop;
            res = temp;
        }
        
        return res;
    }
};
