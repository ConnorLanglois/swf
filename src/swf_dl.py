import re
from urllib import parse, request, error

url = 'http://www.coolmath-games.com'
html = str(request.urlopen(f'{url}/1-complete-game-list?title=All').read())
swfs = re.findall('<span class="game-title"><a href="/0-(.+?)"', html)

# print(str(request.urlopen(f'http://www.coolmath-games.com/sites/cmatgame/files/games/3pandas_coolmath-games.com__0.swf').read()))

for swf in swfs:
	html = str(request.urlopen(f'{url}/0-{swf}').read())
	urls = re.findall('"url":"(.+?)",', html)
	
	if len(urls) > 0:
		obj = urls[0][30:].replace('\\', '')
		flash = request.urlopen(f'{url}/{obj}').read()

		with open(f'swfs/{swf}.swf', 'wb') as file:
			file.write(flash)
