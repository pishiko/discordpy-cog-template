from your_cog import YourCog
from discord.ext.commands import Bot

#テスとりくんのトークンをもらうか，自分で取得してください．
TOKEN = ""

bot = Bot(command_prefix=["."])
bot.add_cog(YourCog(bot))

@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))

bot.run(TOKEN)