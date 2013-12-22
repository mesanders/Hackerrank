#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

/* Separate the string into a vector such that input 0 hello world comes out 
   example vector<string> i::: i[0] = 0; i[1]  = hello; i[2] = world;
*/
vector<string> split(string &str, char c = ' ')
{
    vector<string> result;
    int start = 0, end = 0;
    for (int i = 0; i <= str.size(); i++) {
        end++;
        if (str[i] ==  ' ') {
            result.push_back(str.substr(start, end - 1));
            start = end + start;
            end = 0;
        }
    }
    result.push_back(str.substr(start, end)); // Add the last one to the string

    return result;
} 

int longestRangeMinSub(string P,string Q, int posP, int posQ, int sliceSize, int maxSum) {
    int longest = 0, i = 0, runningSum = 0;
    while (i + longest < sliceSize) {
        if (P[posP + i + longest] != Q[posQ + i + longest]) {
            runningSum++;
        }
        if (runningSum > maxSum) {
            if (P[posP + i] != Q[posQ + i]) {
                runningSum--;
            }
            i++;
        } else {
            longest++;
        }
    }
    return longest;
}

int compareMissMatches(const vector<string> &data) {
    int maxMissMatches  = atoi(data[0].c_str());
    string P = data[1], Q = data[2];
    int longest = 0, sliceSize = 0;;
    int m = P.length(), n = P.length();
    int end1, end2, posP, posQ, longestInSub;
    
    for(int i = 0; i < m + n + 1; i++) {
        if (i > n) {
            sliceSize = m - (i - n);
        } else {
            sliceSize = min(i, m);
        }
        
        if (sliceSize == 0) {
            continue;
        }
        end1 = max(m, m - i);
        
        if (i > n) {
            end1 = m - (i - n);
        }
        
        posP = end1 - sliceSize;
        end2 = min(i, n);
        posQ = end2 - sliceSize;
        longestInSub = longestRangeMinSub(P, Q, posP, posQ, sliceSize, maxMissMatches);
        longest = max(longest, longestInSub);
    }
    
    return longest;
    
}

int main() {
    int numberOfTests;
    vector<string> tests;
    
    cin >> numberOfTests;
    
    for (int i = 0;i <= numberOfTests; i++) {
        string testLine;
        getline(cin, testLine);
        if (testLine != "") { 
            tests.push_back(testLine);
        }
    }
    
    for (string& test: tests) {
        vector<string> delimitedTest = split(test);
        cout << compareMissMatches(delimitedTest) << endl;
    }
    
    return 0;
}
