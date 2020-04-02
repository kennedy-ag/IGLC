import funcoes
profile = input()
like_list = funcoes.get_likes_count(profile)
for i in like_list:
  print(i)