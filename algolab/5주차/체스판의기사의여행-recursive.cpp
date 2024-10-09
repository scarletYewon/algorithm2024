#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int knight_moves[8][2] = {
    {-2, -1}, {-1, -2}, {1, -2}, {2, -1},
    {2, 1}, {1, 2}, {-1, 2}, {-2, 1}
};

bool isValid(int x, int y, int m, int n, vector<vector<int> >& board) {
    return x >= 0 && x < m && y >= 0 && y < n && board[x][y] == 0;
}

bool solve(int x, int y, int move, int m, int n, vector<vector<int> >& board) {
    if (move == m * n) {
        return true;
    }

    for (int i = 0; i < 8; ++i) {
        int next_x = x + knight_moves[i][0];
        int next_y = y + knight_moves[i][1];

        if (isValid(next_x, next_y, m, n, board)) {
            board[next_x][next_y] = move + 1;
            if (solve(next_x, next_y, move + 1, m, n, board)) {
                return true;
            }
            board[next_x][next_y] = 0;  // Backtrack
        }
    }
    return false;
}

void knightTour(int m, int n, int start_x, int start_y) {
    vector<vector<int> > board(m, vector<int>(n, 0));
    board[start_x][start_y] = 1;

    if (solve(start_x, start_y, 1, m, n, board)) {
        cout << "1" << endl;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
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
        knightTour(m, n, a - 1, b - 1);  // Convert to 0-based index
    }
    return 0;
}
