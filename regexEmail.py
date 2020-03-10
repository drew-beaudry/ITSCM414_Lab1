import re
email_pattern = '\w*@\w*\.com'
email_pattern2 = '\w+@\w+\.[com|edu|org|ca]'

s1="alana@classmunity.com"
s2="platta@uww.edu"
s3="@uww.com"

print("test pattern 1")
print(re.match(email_pattern, s1, flags=re.IGNORECASE))
print(re.match(email_pattern, s2, flags=re.IGNORECASE))
print(re.match(email_pattern, s3, flags=re.IGNORECASE))

print("test pattern 2")

print(re.match(email_pattern2, s1, flags=re.IGNORECASE))
print(re.match(email_pattern2, s1, flags=re.IGNORECASE))
print(re.match(email_pattern2, s1, flags=re.IGNORECASE))
