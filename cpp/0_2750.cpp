#include <iostream>
#include <algorithm>
using namespace std;
// 첫줄에 받은 갯수만큼 둘째줄부터 한줄씩 수를 입력받고 그 수들을 정렬해서 한줄에 하나씩 보여줌

int num[1000]; 

int main() {
	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> num[i];
	}

	sort(num, num + N);

	for (int i = 0; i < N; i++) {
		cout << num[i] << "\n";
	}
    
	return 0;
}