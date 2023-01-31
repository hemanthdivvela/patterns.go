//display 1 to 100 prime numbers

package main

import "fmt"

func main() {
	fmt.Println("Prime numbers from 1 to 100:")
	var nums int
	fmt.Println("Enter the value of nums.")

	fmt.Scanln(&nums)

	for num := 2; num <= nums; num++ {
		isPrime := true
		for i := 2; i < num; i++ {
			if num%i == 0 {
				isPrime = false
				break
			}
		}
		if isPrime {
			fmt.Println(num)
		}
	}
}
