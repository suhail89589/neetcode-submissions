class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let seen = new Set();
      for(let num of nums){
        if(seen.has(num)){
            return true;
        }
        seen.add(num);
          
        }
          return false;
      }
    }

let obj = new Solution();
console.log(obj.hasDuplicate([1, 2, 3, 4]));     
console.log(obj.hasDuplicate([1, 2, 3, 4, 4])); 
