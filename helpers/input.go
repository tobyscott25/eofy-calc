package helpers

import "fmt"

// Loops until a valid integer value is given.
func IntInputLoop(prompt string) int {
	var input int
	var err error

	for {
		fmt.Print(prompt)
		_, err = fmt.Scanln(&input)
		if err != nil {
			fmt.Println("Please provide a valid integer value.")
		} else {
			break
		}
	}

	return input
}

// Loops until a valid bool value is given.
func BoolInputLoop(prompt string) bool {
	var input bool
	var err error

	for {
		fmt.Print(prompt)
		_, err = fmt.Scanln(&input)
		if err != nil {
			fmt.Println("Please provide a valid boolean value.")
		} else {
			break
		}
	}

	return input
}
