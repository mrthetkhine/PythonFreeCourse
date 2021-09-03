package main

import "fmt"

func main() {

	i := 0
	fmt.Println("Here is the start")
loop:
	fmt.Println("Hello")
	if i < 5 {
		i += 1
		goto loop
	}
	fmt.Println("Last")
}
