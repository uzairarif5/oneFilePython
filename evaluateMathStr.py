def getTopSubExpression(mathStr):
	'''
		Get indices of top subexpressions.
		For example 4 + 5 (6 + 1 - (3 * 2)) + (3 - 1) would return {6:22, 26:32}
	'''
	indices = dict()
	innerBrackets = -1
	openingIdx = None
	for idx in range(len(mathStr)):
		if (mathStr[idx] == '('):
			if(innerBrackets == -1):
				openingIdx = idx
			innerBrackets += 1
		if (mathStr[idx] == ')'):
			innerBrackets -= 1
			if (innerBrackets == -1):
				indices[openingIdx] = idx
	return indices

def evaluateMathString(mathStr: str):
	operands = [] # 4 + 2 / 5 - 6 * 3 will store [4.0, 2.0, 5.0, -6.0, 3.0]
	operators = [] # 4 + 5 - 6 * 3 will store ["+", "/", "+", "*"]
	curNumStr = ""
	digitEncountered = False
	topBracketIndices = getTopSubExpression(mathStr)
	idx = 0
	while idx < len(mathStr):
		if(mathStr[idx].isdigit() or mathStr[idx] == "."):
			curNumStr += mathStr[idx]
			digitEncountered = True
		elif mathStr[idx] in "+*/-()":
			if(curNumStr != "" and curNumStr != "-"):
				operands.append(float(curNumStr))
				curNumStr = ""
			if(mathStr[idx] == "-"):
				curNumStr = "-"
				operators.append("+")
			elif(mathStr[idx] == "+"):
				operators.append("+")
			elif(mathStr[idx] == "*"):
				operators.append("*")
			elif(mathStr[idx] == "/"):
				operators.append("/")
			elif idx in topBracketIndices.keys():
				subExpr = evaluateMathString(mathStr[idx+1:topBracketIndices[idx]]) #-(5 + 2) will store -7
				if curNumStr == "-":
					operands.append(subExpr * -1) 
					curNumStr = ""
				else:
					operands.append(subExpr)
					#number of operands should be one more than the number of operators
					if len(operators)+1 != len(operands):
						operators.append("*")
				idx = topBracketIndices[idx]
		elif mathStr[idx] != " ":
			raise ValueError(f"Invalid character: {mathStr[idx]}")
		elif digitEncountered:
			#the current value is a space
			digitEncountered = False
			#now check if next non-space is also a digit
			while idx+1 < len(mathStr) and mathStr[idx+1] == " ":
				idx += 1
			if(idx+1 < len(mathStr) and (mathStr[idx+1].isdigit() or mathStr[idx] == ".")):
				raise RuntimeError("Don't add spaces between numbers")
		idx += 1

	#incase if last number wasn't added
	if(curNumStr != ""):
		operands.append(float(curNumStr))

	#do all the multiplication and division
	for i in range(len(operators)):
		if operators[i] == "*":
			operands[i+1] = operands[i] * operands[i+1]
			operands[i] = 0
		elif operators[i] == "/":
			operands[i+1] = operands[i] / operands[i+1]
			operands[i] = 0

	#addition is the only operation left
	return sum(operands)	

print(evaluateMathString("3+5(6+(1-3.5)*(2+3))-1+.5"))