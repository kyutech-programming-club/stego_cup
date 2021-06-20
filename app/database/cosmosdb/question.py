q1 = {
  "id": "1",
  "question": "”Hello World!”を出力してください",
  "answer": "print(\"Hello World!\")",
  "temp_ans": "???(\"???!\")",
  "choice_ans": "print, hoge, Hello World"
}
q2 = {
  "id": "2",
  "question": "入力値に1足して出力してください",
  "answer": "n = input() \nprint(n + 1)",
  "temp_ans": "n = ???() \nprint(n ? 1)",
  "choice_ans": "print, input, ahi, +"
}
q3 = {
  "id": "3",
  "question": "円の半径を入力し、その円の面積を出力してください",
  "answer": "r = input() \nprint(r * r * 3.14)",
  "temp_ans": "r = ???() \nprint(r ? r ? 3.14)",
  "choice_ans": "input, +, -, *, /"
}
q4 = {
  "id": "4",
  "question": "整数の入力値が偶数だったら1、奇数だったら0を出力してください",
  "answer": "num = input() \nprint(num % 2 == 0)",
  "temp_ans": "num = input() \nprint(num ? 2 ?? 0)",
  "choice_ans": "==, %, !=, /"
}
q5 = {
  "id": "5",
  "question": "入力値の絶対値を出力してください",
  "answer": "num = input() \nf num > 0: print(num)\n else: print(num * -1)",
  "temp_ans": "num = input() \nif num ? 0: print(num)\n else: print(num ? ??)",
  "choice_ans": "<, >, =, +, -, *, /, +1, -1"
}
q6 = {
  "id": "6",
  "question": "身長[m]、体重[kg]を入力して、BMIが18.5未満で「痩せ」18.5以上25未満で「普通」、25以上で「肥満」を出力してください",
  "answer": "height = input() \nweight = input() \nbmi = weight / (height * height) \nif bmi < 18.5: print(\"痩せ\")\n elif bmi >= 25: print(\"肥満\")\n else: print(\"普通\")",
  "temp_ans": "height = input() \nweight = input() \nbmi = weight / (height ? height) \nif bmi ? 18.5: print(\"痩せ\")\n elif bmi ?? 25: print(\"肥満\")\n else: print(\"普通\")",
  "choice_ans": "*, /, <, >, >=, <="
}
q7 = {
  "id": "7",
  "question": "1つ目の入力値から2つ目の入力値までの総和を出力してください",
  "answer": "a = input() \nb = input() \nsum = 0 \nfor i in range(a, b + 1): sum += i",
  "temp_ans": "a = input() \nb = input() \nsum = 0 \nfor i in range(?, ? ? ?): sum ?? i",
  "choice_ans": "a, b, +, -, 1, 2, +=, -=,"
}
q8 = {
  "id": "8",
  "question": "入力値の約数の総和を出力してください",
  "answer": "a = input() \nsum = 0 \nfor i in range(a):\n if a % i == 0: sum += i",
  "temp_ans": "a = input() \nsum = 0 \nfor i in range(a):\n if a ? i == 0: sum += ?",
  "choice_ans": "/, %, *, a, i, sum"
}
q10 = {
  "id": "9",
  "question": "入力値が素数であれば1、そうでなければ0を出力してください",
  "answer": "n = input() \nfor p in range(2, n):\n if n % p == 0:\n print(0)\n else: print(1)",
  "temp_ans": "n = input() \nfor p in range(?, ?):\n if n % p == 0:\n print(?)\n else: print(?)",
  "choice_ans": "0, 1, 2, 3, n, p"
}
q11= {
  "id": "10",
  "question": "フィボナッチ数列の入力値番目の項の値を出力してください",
  "answer": "n = input() \na, b = 1, 0 \nfor i in range(n):\n a, b = a + b, a \nprint(b)",
  "temp_ans": "n = input() \na, b = 1, 0 \nfor i in range(n):\n a, b = ? ? ?, ? \nprint(?)",
  "choice_ans": "a, b, n, +, -, *, /"
}
= {
  "id": "",
  "question": "",
  "answer": "",
  "temp_ans": "",
  "choice_ans": ""
}
