// 输入切片 b 来获取数字
/*
func main() {
	a := make([]rune, 0)
	a = append(a, 'a', 'b', '1', '2', 'c', 'd')
	fmt.Println(a)
	i := 0
	for ; i < len(a) && !unicode.IsDigit(a[i]); i++ {
		fmt.Println(a[i])
	}
	fmt.Println(i)

	x := 0
	for ; i < len(a) && unicode.IsDigit(a[i]); i++ {
		x = x * 10 + int(a[i]) - '0'
	}
	fmt.Println(x)
}

*/

func nextInt(b []rune, i int) (int, int) {
	for ; i < len(b) && !unicode.IsDigit(b[i]); i++ {

	}
	x := 0
	for ; i < len(b) && unicode.IsDigit(b[i]); i++ {
		x = x * 10 + int(b[i]) - '0'
	}
	return x, i
}

func main() {
	var b = []rune{'a', 'b', 'c', '1', '2', '3', 'd', 'e', 'f', '4', '5', '6'}
	x := 0
	for i := 0; i < len(b); {
		x, i = nextInt(b, i)
		fmt.Println(x)
	}
}

