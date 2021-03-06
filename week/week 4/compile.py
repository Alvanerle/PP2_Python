import re

sentence = 'Start a sentence and then bring it to the end'

pattern = re.compile(r'Start')

matches = re.finditer(pattern, sentence)

for match in matches:
    print(match.group(0))