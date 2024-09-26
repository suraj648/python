import re

string = "the thermometer read the human temperature"

result = re.findall(r"the",string)
print(result)


string = "color colour which color do you choose"

result = re.findall(r"colou?r",string)
print(result)


string = "grey was actually gray before grey become gray"

result = re.findall(r"gr[ea]y",string)
print(result)


string = "willsmith is not a blackSmith"

result = re.findall(r"[Ss]mith",string)
print(result) 


string = "10 bottles of wine cost 1000 each"

result = re.findall("\d+",string)
print(result)


# TO GET VOWELS IN A STRING
string = "The cat in the hat sat on the flat mat to avoid cold floor "

result = re.findall("[aeiou]",string)
print(result)


# TO GET CONSONANTS IN A STRING
string = "The cat in the hat sat on the flat mat to avoid cold floor "

result = re.findall("[^aeiou]",string)
print(result)


string = "anna and annaaaa are same person"

result = re.findall("anna+",string)
print(result)