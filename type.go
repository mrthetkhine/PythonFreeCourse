package main

import "fmt"

func main() {
	a := 10 //type inferencing
	fmt.Println("A is ", a)
	//a = "Hello"
	b := true
	c := a + b //invalid type operation

	fmt.Println("C is ", c)
}
