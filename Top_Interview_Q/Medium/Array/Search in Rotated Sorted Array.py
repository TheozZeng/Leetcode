class Solution:
	def binary_search(self,nums,target):
		print(nums)
		l=0
		r=len(nums)-1
		while(l<=r):
			m=(l+r)//2
			m_val = nums[m]
			print(nums[l],"|",m_val,"|",nums[r])
			if(m_val==target):
				return m
			elif(m_val > target):
				r = m -1
			else:
				l = m +1
		return None


	def find_pivot(self, nums):
		l = 0
		r = len(nums)-1
		while(l<=r):
			mid = (l+r)//2
			mid_val = nums[mid]
			print(nums[l],"|",mid_val,"|",nums[r])

			if(mid_val < nums[r]):
				r = mid
			else:
				l = mid + 1
		return mid


	def search(self, nums, target):
		p = self.find_pivot(nums)
		print(p)
		print("_________________")
		l = 0
		r = len(nums)-1
		if(target <= nums[r]):
			index = self.binary_search(nums[p:],target)
			if(index == None):
				return -1
			else:
				return p+index
		else:
			index = self.binary_search(nums[0:p],target)
			if(index == None):
				return -1
			else:
				return index



nums = [4,5,6,7,8,9,0,1,2,3]
sol = Solution()
print(sol.search(nums,0))