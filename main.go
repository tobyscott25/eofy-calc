package main

import (
	"fmt"

	"github.com/joho/godotenv"
	"github.com/tobyscott25/eofy-calc/cmd"
)

func main() {

	// fmt.Println("Welcome to Personal Finance Calculator!")

	// Load environment variables from .env file
	err := godotenv.Load()
	if err != nil {
		fmt.Println("Hint: You can create a .env file to auto-answer these questions!")
	}

	cmd.StartPFC()
}
