from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def get_json(url):
  try:
    http_reply = urlopen(url)
  except HTTPError:
    return None
  try:
    html = BeautifulSoup(http_reply.read(), features = "html.parser")
    json = html.body.find("script", {"type":"text/javascript"})
    json = json.get_text()
  except AttributeError:
    return None
  return json
def get_likes_count(name):
  string = get_json("https://www.instagram.com/{}/".format(name))
  start_index = 0
  index_list = []
  itens = []
  count_list = []
  count = []
  while start_index < len(string):
    resultado = string.find('"edge_liked_by"', start_index)
    if resultado == -1: 
        break
    else:
      index_list.append(resultado)
      start_index = resultado + 1
  for iteration in index_list:
    item = string[iteration:iteration+35]
    itens.append(item)
  for c in itens:
    for character in c:
      if(character.isdigit()):
        count.append(character)
      else:
        continue
    ct = ''.join(count)
    count_list.append(ct)
    count.clear()
  for i in count_list:
    count_list[count_list.index(i)] = "A {0}ª foto/video de @{1} tem {2} curtidas\n".format(count_list.index(i)+1, name, i)
  return count_list