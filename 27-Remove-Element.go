package main

import "fmt"

func main() {
	nums := []int{3,2,2,3}
	k := removeElement(nums, 3)
	fmt.Println(k)
	fmt.Println(nums)

}

func removeElement(nums []int, val int) int {
	k := 0
	for i := 0; i < len(nums); i++{
		if nums[i] != val {
			nums[k], nums[i] = nums[i], nums[k]			
			k++
		}
	}
	return k
}
