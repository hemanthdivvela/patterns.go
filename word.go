package main

import (
	"fmt"
	"strings"
)

func ConvertUpperAndLowerLetters(Word string) {
	result := ""
	for _, c := range Word {
		if c >= 65 && c <= 90 {
			let := strings.ToLower(string(c))
			result += let
		} else if c >= 97 && c <= 122 {
			let := strings.ToUpper(string(c))
			result += let
		} else {
			result += string(c)
		}
	}
	fmt.Println(result)
}

func main() {
	input1 := "HellO WorLd"
	input2 := "hELLo wORlD"
	input3 := "1a& F"
	ConvertUpperAndLowerLetters(input1)
	ConvertUpperAndLowerLetters(input2)
	ConvertUpperAndLowerLetters(input3)
}

// func toggleCase(s string) string {

// 	var result strings.Builder

// 	for _, h := range s {
// 		if h >= 'A' && h <= 'Z' {
// 			result.WriteRune(h + 32)
// 		} else if h >= 'a' && h <= 'z' {
// 			result.WriteRune(h - 32)
// 		} else {
// 			result.WriteRune(h)
// 		}
// 	}

// 	return result.String()
// }

// func main() {
// 	inputStr := "HellO WorLd"
// 	outputStr := toggleCase(inputStr)
// 	fmt.Println(outputStr)

// }
