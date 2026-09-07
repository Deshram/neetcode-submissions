class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        q = deque()
        output = []
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if (r - l + 1) >= k:
                output.append(nums[q[0]])
                l+=1
                if l > q[0]:
                    q.popleft()
        return output
        