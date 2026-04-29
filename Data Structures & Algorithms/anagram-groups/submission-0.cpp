#include <unordered_map>
#include <algorithm>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string, vector<string>> freqMap{}; 

        for (auto& s : strs)
        {
            string sortedS = s; 
            sort(sortedS.begin(), sortedS.end());
            freqMap[sortedS].push_back(s);
        }

        vector<vector<string>> output = {}; 


        for (const auto& [_, value] : freqMap)
        {
            output.push_back(value);
        }

        return output; 


        
    }

    // Store the frequencies in arrays

};
