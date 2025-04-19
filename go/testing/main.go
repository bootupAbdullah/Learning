package main


import "fmt" 

func main() {
	// chew := "I like to eat my food"
	// calln := two()
	// call_ten := ten()
	fmt.Println(takeTwo(4, 4))
	practice("Abdullah")
}

// func two() string {
// 	food := "is this working?"
// 	return food
// }

// func ten() int {
// 	example_ten := 10
// 	return example_ten
// }

func addTen (num int) int {
	return num + 10
}

func takeTwo (num int, num2 int) int {
	return num + num2
}

func practice (name string) {
	user := name
	fmt.Printf("Hello, you person, your name is %s\n", user)
}
