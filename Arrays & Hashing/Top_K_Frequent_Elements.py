class Solution:

    # sort in decending and return k distinct, complexity - o(n^2)
    # hashmap to make a counter dict, the sort and get the number in dec order - o(n^2)
    # bucket sort - where index is count and value is list of values that that count index - o(n)
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}

        for num in nums:
            val = d.get(num, 0)
            d[num] = val + 1
        
        sorted_value = sorted(d, key = d.get, reverse = True)
        # print(sorted_value)
        return sorted_value[:k]