package helpers

import (
	"fmt"
	"strconv"
)

// Loops until a valid integer value is given.
func IntInputLoop(prompt string, autofill string) int {

	var input int
	var err error

	for {

		if autofill != "" {
			fmt.Println(prompt + autofill)
			num, err := strconv.Atoi(autofill)

			if err != nil {
				fmt.Println("Autofill value invalid. Please provide a valid integer value.")
			} else {
				return num
			}
		}

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
func BoolInputLoop(prompt string, autofill string) bool {
	var input bool
	var err error

	for {

		if autofill != "" {
			fmt.Println(prompt + autofill)
			boolean, err := strconv.ParseBool(autofill)

			if err != nil {
				fmt.Println("Autofill value invalid. Please provide a valid integer value.")
			} else {
				return boolean
			}
		}

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
