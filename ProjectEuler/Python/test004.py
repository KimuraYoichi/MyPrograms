import re

pattern = pattern = '^(?=.*83).*$'
text = "999983"

# pattern = r"ca"
# text = "caabsacasca"
repatter = re.compile(pattern)
matchOB = repatter.match(text)
matchALL = repatter.findall(text)

print(matchOB)
print(matchALL)