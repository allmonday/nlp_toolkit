import re
def getWords():
    lines = open('out.data','r', encoding= "gbk").readlines()
    words = []
    for line in lines:
        words.append(re.split(r'\s+', line)[0])
    return words
        
