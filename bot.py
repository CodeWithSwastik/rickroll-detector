import discord
from discord.ext import commands
from rickroll_detector import find_rickroll

BOT_TOKEN = ""
RICKROLL_FOUND_MESSAGE = "⚠️Rickroll Alert⚠️"

bot = commands.Bot(command_prefix = ">", intents = discord.Intents.default())

@bot.event
async def on_message(msg):
    for i in msg.content.split(" "):
        i = i.replace("<","").replace(">", "") #Removes <> that could be used to hide embeds
        if "https://" in i and find_rickroll(i):
            await msg.reply(RICKROLL_FOUND_MESSAGE)
            break

    await bot.process_commands(msg)

bot.run(BOT_TOKEN)
