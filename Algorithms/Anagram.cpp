#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>

using namespace std;

int getChangesToAnagram(string s1, string s2) {
    int size1 = s1.size();
    int size2 = s2.size();
    if (size1 != size2)
        return -1;

    map<char, int> charCount;
    for (int i = 0; i < size2; i++)
        charCount[s2[i]]++;

    int total = size1;
    for (int i = 0; i < size1; i++) {
        if (charCount[s1[i]] > 0) {
            total--;
            charCount[s1[i]]--;
        }
    }

    return total;
}

int main() {
    int size;
    cin >> size;
    for (int i = 0; i < size; i++) {
        string s;
        cin >> s;
        cout << getChangesToAnagram(s.substr(0, s.size() / 2),
                                    s.substr(s.size() / 2)) << endl;
    }
}
