#include <iostream>
using namespace std;
// 첫줄에 받은 갯수만큼 둘째줄에 수를 입력받고 받은 값들을 모두 더해 출력함

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