class remove_dupes_sorted_array:
    def rmDups(self, nums: list[int]) -> int:
        for i in nums:
            if nums.count(i) > 1:  # this is probably slow
                nums.remove(i)
        return nums
