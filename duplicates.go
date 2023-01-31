package main

func main() {

	a := []int{17, 19, 18, 18, 21}

	b := map[int]int{}

	for _, i := range a {
		_, ok := b[i]

		if !ok {
			b[i] = 1
		} else {
			b[i] += 1
		}
	}
}
