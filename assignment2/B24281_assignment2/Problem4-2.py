#Problem 4-2
string = "In a Democracy, the government is of the people, by the people, and for the people, still people don’t go out and vote"

i = string.find("people")
string = string[:i] + "PEOPLE" + string[i+6:]
print(string)

i = string.find("people")
string = string[:i] + "pEOPLE" + string[i+6:]
i = string.find("people")
string = string[:i] + "pEOPLE" + string[i+6:]
print(string)

i = string.find("people")
string = string[:i] + "peoPLE" + string[i+6:]
print(string)