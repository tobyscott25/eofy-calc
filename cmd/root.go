package cmd

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "pfc",
	Short: "Personal Finance Calculator",
	Long:  `A fast, CLI personal finance calulator for Australians, written in Go by Toby Scott.`,
}

func StartPFC() {

	rootCmd.AddCommand(CmdCalculateTax)

	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
