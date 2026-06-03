class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if ( s.length != t.length) return false;

        let sortedS= s.split('').sort().join('');
        let sortedT= t.split('').sort().join('');

    return sortedS === sortedT;
    }
}
let obj = new Solution();
console.log(obj.isAnagram("silent","listen"))
console.log(obj.isAnagram("car","tar"))