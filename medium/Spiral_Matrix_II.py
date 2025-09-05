class Solution {
    public int[][] generateMatrix(int n) {
        int[][] array = new int[n][n];
        int left = 0, right = n - 1;
        int top = 0, bottom = n - 1;
        int num = 1;
        
        while (num <= n*n){
            // 左到右
            for (int j = left; j<= right; j++){
                array[top][j] = num;
                num++;
            }
            top++;
            // 上到下
            for (int i = top; i<= bottom; i++){
                array[i][right] = num;
                num++;
            }
            right--;
            // 右到左
            if (top <= bottom){
                for (int j = right; j >= left; j--){
                    array[bottom][j] = num;
                    num++;
                }
                bottom--;
            }
            // 下到上
            if (left <= right){
                for (int i = bottom; i >= top; i--){
                    array[i][left] = num;
                    num++;
                }
                left++;  
            }
        }
        return array;
    }
}
