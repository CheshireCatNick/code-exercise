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
func cl() {
	if clearLine {
		var n int
		fmt.Scanf("%d", &n)
	}
}

const clearLine = true

func main() {
	var n, m, p int
	var ai int
	fn := -1
	fm := -1
	fmt.Scanf("%d%d%d", &n, &m, &p)
	cl()
	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &ai)
		if ai%p != 0 && fn == -1 {
			fn = i
		}
	}
	cl()
	for i := 0; i < m; i++ {
		fmt.Scanf("%d", &ai)
		if ai%p != 0 && fm == -1 {
			fm = i
		}
	}
	cl()
	wi(fn + fm)
}
