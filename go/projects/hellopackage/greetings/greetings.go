package greetings

import "fmt"

func SayHello(name string) string {
	message := fmt.Sprintf("Hello, friend %v.!", name)
	return message
}