s=input()
com=s.split(' ')
news=[lie[::-1] for lie in com]
outcome=' '.join(news)
print(outcome)