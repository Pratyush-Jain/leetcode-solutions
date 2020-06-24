class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int row = dungeon.length;
        int col = dungeon[0].length;
        int[][] dp = new int[row][col];
        
        
        //last element 
            dp[row-1][col-1] = dungeon[row-1][col-1]>0? 1:1-dungeon[row-1][col-1];

        // last row
            for(int i=col-2;i>=0;--i){
                dp[row-1][i] = Math.max(dp[row-1][i+1]-dungeon[row-1][i] ,1);

            }
        // last col
            for(int i = row-2;i>=0;--i){
                dp[i][col-1] = Math.max(dp[i+1][col-1]-dungeon[i][col-1],1);

            }

            //rest elements
            for(int i = row-2;i>=0;--i){
                for(int j = col-2;j>=0;--j){
                    dp[i][j] = Math.max(Math.min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1);

                }
            }
    return dp[0][0];
    }
}
