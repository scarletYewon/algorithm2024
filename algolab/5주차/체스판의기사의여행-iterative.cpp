#include <iostream>
#include <stack>

using namespace std;

const int MAX_N = 8; // 보드 최대 크기 8x8로 가정
const int knight_moves[8][2] = {
    {-2, -1}, {-1, -2}, {1, -2}, {2, -1},
    {2, 1}, {1, 2}, {-1, 2}, {-2, 1}
};

struct State {
    int x, y, move_num, direction;
    State(int x, int y, int move_num, int direction) : x(x), y(y), move_num(move_num), direction(direction) {}
};

// 보드 크기를 넘지 않고, 해당 위치에 말이 아직 방문하지 않았는지 체크하는 함수
bool isValid(int x, int y, int m, int n, int board[MAX_N][MAX_N]) {
    return x >= 0 && x < m && y >= 0 && y < n && board[x][y] == 0;
}

bool knightTourIterative(int m, int n, int start_x, int start_y, int board[MAX_N][MAX_N]) {
    stack<State> s;
    s.push(State(start_x, start_y, 1, 0)); // 첫 번째 위치를 스택에 넣음
    board[start_x][start_y] = 1; // 첫 번째 위치는 이미 방문한 상태로 처리
    
    while (!s.empty()) {
        State& current = s.top(); // 현재 위치 확인
        if (current.move_num == m * n) {
            return true; // 모든 셀을 방문한 경우
        }

        bool moved = false; // 이동 여부를 추적
        while (current.direction < 8) { // 8방향 탐색
            int next_x = current.x + knight_moves[current.direction][0];
            int next_y = current.y + knight_moves[current.direction][1];
            current.direction++; // 방향을 하나씩 증가
            
            if (isValid(next_x, next_y, m, n, board)) { // 유효한 이동인지 확인
                s.push(State(next_x, next_y, current.move_num + 1, 0)); // 새로운 위치로 이동
                board[next_x][next_y] = current.move_num + 1; // 보드에 이동 기록
                moved = true;
                break;
            }
        }

        if (!moved) {
            // 더 이상 갈 곳이 없을 때 백트랙킹
            board[current.x][current.y] = 0; // 방문 취소
            s.pop(); // 이전 상태로 돌아감
        }
    }

    return false;
}

void printBoard(int board[MAX_N][MAX_N], int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

void knightTour(int m, int n, int start_x, int start_y) {
    int board[MAX_N][MAX_N] = {0};  // 배열을 0으로 초기화
    if (knightTourIterative(m, n, start_x, start_y, board)) {
        cout << "1" << endl;
        printBoard(board, m, n);  // 해결된 보드를 출력
    } else {
        cout << "0" << endl;
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int m, n, a, b;
        cin >> m >> n >> a >> b;
        knightTour(m, n, a - 1, b - 1);  // 0-based index로 변환
    }
    return 0;
}
