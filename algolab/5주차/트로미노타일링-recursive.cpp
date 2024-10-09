#include <iostream>
#include <vector>

using namespace std;

class TrominoTiling {
private:
    int tile;  // 타일 번호
    vector<vector<int> > board;  // 보드
    int size;  // 보드의 크기

public:
    TrominoTiling(int k) {
        size = k;
        tile = 1;
        board = vector<vector<int> >(size, vector<int>(size, 0));
    }

    // 보드를 출력하는 함수
    void printBoard() {
        for (int i = 0; i < size; ++i) {
            for (int j = 0; j < size; ++j) {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
    }

    // 트로미노 타일링 함수 (분할 정복)
    void tromino(int x, int y, int holeX, int holeY, int n) {
        if (n == 1) return;

        int t = tile++;  // 새로운 타일 번호
        int half = n / 2;

        // 중앙에 트로미노 타일을 놓기 위한 준비
        // 4개의 사분면에 대해 재귀적으로 수행
        // 빈칸(hole)이 어디 있는지에 따라 사분면을 다르게 처리
        if (holeX < x + half && holeY < y + half) {
            // 빈칸이 1사분면에 있을 경우
            tromino(x, y, holeX, holeY, half);  // 1사분면
        } else {
            // 1사분면에 타일을 놓고 재귀적으로 진행
            board[x + half - 1][y + half - 1] = t;
            tromino(x, y, x + half - 1, y + half - 1, half);
        }

        if (holeX < x + half && holeY >= y + half) {
            // 빈칸이 2사분면에 있을 경우
            tromino(x, y + half, holeX, holeY, half);  // 2사분면
        } else {
            // 2사분면에 타일을 놓고 재귀적으로 진행
            board[x + half - 1][y + half] = t;
            tromino(x, y + half, x + half - 1, y + half, half);
        }

        if (holeX >= x + half && holeY < y + half) {
            // 빈칸이 3사분면에 있을 경우
            tromino(x + half, y, holeX, holeY, half);  // 3사분면
        } else {
            // 3사분면에 타일을 놓고 재귀적으로 진행
            board[x + half][y + half - 1] = t;
            tromino(x + half, y, x + half, y + half - 1, half);
        }

        if (holeX >= x + half && holeY >= y + half) {
            // 빈칸이 4사분면에 있을 경우
            tromino(x + half, y + half, holeX, holeY, half);  // 4사분면
        } else {
            // 4사분면에 타일을 놓고 재귀적으로 진행
            board[x + half][y + half] = t;
            tromino(x + half, y + half, x + half, y + half, half);
        }
    }

    // 시작 함수 (n x n 보드에서 빈칸을 지정하고 타일링 시작)
    void startTiling(int holeX, int holeY) {
        tromino(0, 0, holeX, holeY, size);
    }
};

int main() {
    int k, holeX, holeY;
    int t;
    cin >> t;
    while (t--) {
      cin >> k;
      cin >> holeX >> holeY;

      TrominoTiling tt(k);
      tt.startTiling(holeX, holeY);
      tt.printBoard();
    }

    return 0;
}
