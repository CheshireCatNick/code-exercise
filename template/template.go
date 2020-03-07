package main

import "fmt"

func ws(args ...string) {
	for i, s := range args {
		if i == 0 {
			fmt.Print(s)
		} else {
			fmt.Printf(" %s", s)
		}
	}
	fmt.Println()
}
func wi(args ...int) {
	for i, n := range args {
		if i == 0 {
			fmt.Print(n)
		} else {
			fmt.Printf(" %d", n)
		}
	}
	fmt.Println()
}
func ri(args ...*int) {
	for _, p := range args {
		fmt.Scanf("%d", p)
	}
}
func rs(args ...*string) {
	for _, p := range args {
		fmt.Scanf("%s", p)
	}
}
func main() {

}
