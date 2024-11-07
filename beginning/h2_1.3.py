print("My name is %s and my age is %d and my profession is %s"%('lk',18,'chifan,shuijiao,dadoudou'))
print('====================================================================================================')
s=input()
com=s.split(' ')
news=[lie[::-1] for lie in com]
outcome=' '.join(news)
print(outcome)

