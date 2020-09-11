from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "!"
OWNER_IDS = [298598074194853889]


class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()

		super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)
	
	def run(self, version):
		self.VERSION =version

		with open ("./lib/bot/token.0", "r", encoding="utf-8") as tf:
			self.TOKEN = tf.read()

		print("Logging In...")
		super().run(self.TOKEN, reconnect=True)

	async def on_connect(self):
		print("User Logged In.")

	async def on_disconnect(self):
		print("Logging Out.")

	async def on_ready(self):
		if not self.ready:
			self.ready = True
			self.guild = self.get_guild(298599568608591872)
			print("bot ready")

		else:
			print("bot reconnected")

	async def on_message(self,message): #saving for if I want to do a levelling system
		pass

bot = Bot()
