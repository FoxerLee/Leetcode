class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> row, col;
		// Row - Col repetition check
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				if (board[i][j] != '.') {
					if (!row.count(board[i][j])) row.insert(board[i][j]);
					else return false;
				}
				if (board[j][i] != '.') {
					if (!col.count(board[j][i])) col.insert(board[j][i]);
					else return false;
				}
			}
			row.clear();
			col.clear();
		}

		//// 3x3 subgrid check
		 row.clear();
		 for (int i = 0; i < 9; i+=3) {
		 	for (int j = 0; j < 9; j+=3) {
		 		for (int k = i, kleft = 3; k < 9 && kleft>0; k++, kleft--) {
		 			for (int m = j, mleft = 3; m < 9 && mleft>0; m++, mleft--) {
		 				if(board[k][m] != '.') {
		 					if (!row.count(board[k][m])) row.insert(board[k][m]);
		 					else return false;
		 				}
		 			}
		 		}
		 		row.clear();
		 	}
		 }
		return true;
    }
};
