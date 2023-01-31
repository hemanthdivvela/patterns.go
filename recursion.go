// WAP to find the sum of digits of a number, using recursion
package main

import "fmt"

func sumOfDigits(n int) int {

	if n == 0 {
		return 0
	}
	return (n % 10) + sumOfDigits(n/10)
}

func main() {
	num := 153
	result := sumOfDigits(num)
	fmt.Println(result)

}
