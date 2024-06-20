#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    char arr[n];
    cin >> arr;

    int sum = 0;

    for (int i=0; i<n; i++){
        // 아스키코드 48번이 0이라서 48을 빼거나 0을 뺴야함
        // sum += arr[i]-48;
        sum += arr[i] - '0';
    }

    cout << sum << endl;

}