#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int calculate_weight(const string& s) {
  int weight = 0;
  for (int i = 0; i < s.size(); i++) {
    weight += ((i % 2 == 0 ? 1 : -1) * (s[i] - 'a'));
  }
  return weight;
}

int stringPermutation(string s) {
  int positive_count = 0;
  sort(s.begin(), s.end());
  do {
    if (calculate_weight(s) > 0) {
      positive_count++;
    }
  } while (next_permutation(s.begin(), s.end()));
  
  return positive_count;
}

int main() {
    int t;
    cin >> t;  
    while (t--) {
      string s;
      cin >> s;  
      int result = stringPermutation(s);
      cout << result << endl;
    }
    
    return 0;
}
