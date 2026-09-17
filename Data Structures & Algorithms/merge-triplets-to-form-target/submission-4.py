class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_first = False
        found_second = False
        found_last = False

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            if triplet[0] == target[0]:
                found_first = True
            if triplet[1] == target[1]:
                found_second = True
            if triplet[2] == target[2]:
                found_last = True
            
        return found_first and found_second and found_last