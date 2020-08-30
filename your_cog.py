from discord.ext import commands

class YourCog(commands.Cog):

    #初期化処理
    def __init__(self,bot):
        self.bot = bot


    #sample command
    # .add 3 5
    @commands.command()
    async def add(self,ctx,num1,num2):
        n = int(num1) + int(num2)
        await ctx.send("{0} + {1} = {2}".format(num1,num2,n))