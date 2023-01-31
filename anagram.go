package main

import "fmt"

func Anagram(s string, t string) bool {
	string1 := len(s)
	string2 := len(t)
	fmt.Println("Letter 1 =", s, "\nLetter 2 =", t)
	if string1 != string2 {
		fmt.Print("strings are not equal")
	}

	anagramMap := make(map[string]int)

	for i := 0; i < string1; i++ {
		anagramMap[string(s[i])]++
	}

	for i := 0; i < string2; i++ {
		anagramMap[string(t[i])]--
	}

	for i := 0; i < string1; i++ {
		if anagramMap[string(s[i])] != 0 {

			return false
		}
	}

	return true
}

func main() {
	fmt.Println("Program to check if given two strings are anagram or not")

	output := Anagram("coal", "caol")
	fmt.Println(output)

	output = Anagram("hello", "heelo")
	fmt.Println(output)

}
