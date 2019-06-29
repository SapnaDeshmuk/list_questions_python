


question_list = ["1.How many continents are there?", "2.What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
first_options=["1.Four", "1.chandigarh", "1.software engineering"]
second_options=["2.Nine", "2.Bhopal", "2.Counseling"]
third_options=["3.Seven", "3.Chennai", "3.Tourism"]
fourth_options=["4.Eight","4.Delhi","4.Agriculture"]
all_options=["first_options","second_options","third_options","fourth_options"]
ans_key=[3,4,1]
life_line=[["1.Nine","2.Seven"],["1.bhopal","2.Delhi"],["1.software engineering","2.Agricultur"]]
life_line_key=[2,2,1]
i=0
while i<len(question_list):
	print question_list[i]
	print first_options[i]
	print second_options[i]
	print third_options[i]
	print fourth_options[i]
	user=int(raw_input("your answer aur 5050"))
	if (ans_key[i]==user):
		print "congrates!!apka answer sahi hai"
	elif user == 5050:
		j=0
		print question_list [i]

		while j<len(life_line[i]):
			print life_line[i][j]
			j=j+1
		user=int(raw_input("your answer"))
		if user==(life_line_key[i]):
			print "you win"
		else:
			print"you lose"
			break
	i=i+1