import re

string = 'abc 12de 23 \n f45 6'

#matches all whitespace characters
pattern = '\s+'

replace = '-'

new_string = re.sub(pattern, replace, string)
print(new_string)