# -*- coding: utf-8 -*-


import asyncio
import os

import pyrogram as tg

from secret import api_id, api_hash

app = tg.Client('account', api_id, api_hash)

channels = [-1001217105316, -1001164999973, -1001738063152, -1001751595273, -1001572748754, -1001437814721]

messages_count = 0
pages_num = len(os.listdir('./pages/'))
page = str(pages_num)+'.html'

@app.on_message()
async def msg(client, message):
	if not message.chat.id in channels:
		return
	global messages_count, page, pages_num

	messages_count += 1
	if messages_count > 30:
		messages_count = 1
		pages_num += 1
		page = str(pages_num) + '.html'

	txt = ''
	if message.text:
		txt = message.text.html
	content = '<div class="Message"><p>' + message.chat.title + '</p><p>' + txt + '</p></div>\n'

	data = ''
	with open('pages/'+page, 'r', encoding="utf-8") as f:
		data = f.read()
	with open('pages/'+page, 'w', encoding="utf-8") as f:
		parts = data.split('<body>')
		data = parts[0] + '<body>\n' + content + parts[1]
		f.write(data)

	print('m')

app.run()
