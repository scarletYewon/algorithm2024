#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int calculate_weights(const vector<int>& pebbles) {
    int left = pebbles[0];
    int right = pebbles[1];

    for (size_t i = 2; i < pebbles.size(); ++i) {
        if (left <= right) {
            left += pebbles[i];
        } else {
            right += pebbles[i];
        }
    }

    int diff = abs(left - right);

    vector<int> weights = {100, 50, 20, 10, 5, 2, 1}; // 리스트 초기화
    int count = 0;
    for (int weight : weights) {
        if (diff == 0) break;
        count += diff / weight;
        diff %= weight;
    }

    return count;
}

int main() {
    int t;
    cin >> t;

    vector<int> results;
    for (int test = 0; test < t; ++test) {
        int n;
        cin >> n;

        vector<int> pebbles(n);
        for (int i = 0; i < n; ++i) {
            cin >> pebbles[i];
        }

        results.push_back(calculate_weights(pebbles));
    }

    for (int result : results) {
        cout << result << endl;
    }

    return 0;
}
