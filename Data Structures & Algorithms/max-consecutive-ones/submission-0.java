class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0, res = 0;
        for(int i = 0;i < nums.length;i++){
            if(nums[i] == 1){
                count += 1;
            }else{
            if(count > res){
                res = count;
                count = 0;
            }else{
                count = 0;
            }
            }
        }
        if (res<count){
            return count;
        }
        return res;
    }
}