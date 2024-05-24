########## EXERCISE: PASSWORD VALIDATION ##########
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'Simon'
pattern2 = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password = 'hdjk'


a = pattern.search(string)
check = pattern2.fullmatch(password)
print(check)