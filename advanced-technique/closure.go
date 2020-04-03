package main

import "fmt"

func createCounter() func() int {
	count := 0
	return func() int {
		count++
		return count
	}
}

func main() {
	c := createCounter()
	fmt.Println(c(), c(), c())
}