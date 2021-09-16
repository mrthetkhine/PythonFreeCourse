package main

import (
	"errors"
	"fmt"
)

func division(num int, divisor int) (error, int) {
	if divisor == 0 {
		return errors.New("Divisor is zero"), 0
	} else {
		return nil, num / divisor
	}

}
func main() {
	err, result := division(13, 0)
	if err != nil {
		fmt.Println("Error ", err)
	} else {
		fmt.Println("Result ", result)
	}

}
