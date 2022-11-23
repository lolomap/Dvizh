import asyncio
import pyrogram as tg

from secret import api_id, api_hash


async def main():
	async with tg.Client('account', api_id, api_hash) as app:
		await app.send_message('me', 'Hello World')



if __name__ == '__main__':
	asyncio.run(main())
