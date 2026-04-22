#include <algorithm> 
class Solution {
public:
    int missingNumber(vector<int>& nums) {

        int sum = std::accumulate(nums.begin(), nums.end(), 0);
        int n = nums.size(); 

        return ((n * (n+1)) / 2) - sum; 

        
    }
};
