import discord
import os
import requests
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix=commands.when_mentioned_or("if.", "If.", "IF.", "iF."))

bot.remove_command("help")

@bot.command(name="help")
async def _help(ctx):
	"""Shows this help."""
	return await ctx.send(embed=discord.Embed(
		title="Help", description=f"""
		{ctx.prefix}help - Show this help.
		{ctx.prefix}about - About InfinityFree.
		{ctx.prefix}ping - Checks the latency of the bot.
		{ctx.prefix}requeststest - NO description.
		{ctx.prefix}user - Returns user info.
		"""
		).set_thumbnail(url="https://infinityfree.net/assets/apple-touch-icon-90bec27bc0c23919f97f101fb88b861f63ecd026e638acc76da2691db1b82af0.png").set_author(name="InfinityFree",url="https://infinityfree.net/",icon_url="https://infinityfree.net/assets/apple-touch-icon-90bec27bc0c23919f97f101fb88b861f63ecd026e638acc76da2691db1b82af0.png"))

@bot.command(name="about")
async def _about(ctx):
	"""About InfinityFree."""
	return await ctx.send(embed=discord.Embed(
		title="About InfinityFree", description="""
		InfinityFree is a fully-featured unlimited completely free web hosting platform for your projects. It offers 99.9% uptime, doesn't have any ad on your website, and you can host hundreds and thousands of domain types (except .tk ones because of spam)!
		It offers Softaculous, which you can use to install apps easily and quickly, PHP from 5.4 to 7.3, MySQL 5.6 with 400 MySQL databases to use, free subdomains, free SSL on your own domains, a DNS service which you can use to manage DNS records, and more!
		
		Check it out [here](https://infinityfree.net/).
		""").set_thumbnail(url="https://infinityfree.net/assets/apple-touch-icon-90bec27bc0c23919f97f101fb88b861f63ecd026e638acc76da2691db1b82af0.png").set_author(name="InfinityFree", url="https://infinityfree.net/", icon_url="https://infinityfree.net/assets/apple-touch-icon-90bec27bc0c23919f97f101fb88b861f63ecd026e638acc76da2691db1b82af0.png"))

@bot.command(name="ping")
async def _ping(ctx):
	"""Checks the latency of the bot."""
	return await ctx.send(embed=discord.Embed(title="Pong!", description=f"""
		Total time took: **{round(bot.latency * 1000)} ms**
		""").set_thumbnail(url="https://infinityfree.net/assets/apple-touch-icon-90bec27bc0c23919f97f101fb88b861f63ecd026e638acc76da2691db1b82af0.png").set_author(name="InfinityFree", url="https://infinityfree.net", icon_url="https://infinityfree.net/assets/apple-touch-icon-90bec27bc0c23919f97f101fb88b861f63ecd026e638acc76da2691db1b82af0.png"))

@bot.command(name="requeststest")
async def _requeststest(ctx):
	"""NO description."""
	uri="https://github.com/timeline.json"
	rgthjk=requests.get(uri)
	return await ctx.send(embed=discord.Embed(
		title="Request Info", description=f"""
		Request URI: `{uri}`
		Status code: `{rgthjk.status_code}`
		Content:
		```{rgthjk.text}```
		""").set_thumbnail(url="https://infinityfree.net/assets/apple-touch-icon-90bec27bc0c23919f97f101fb88b861f63ecd026e638acc76da2691db1b82af0.png").set_author(name="InfinityFree", url="https://infinityfree.net", icon_url="https://infinityfree.net/assets/apple-touch-icon-90bec27bc0c23919f97f101fb88b861f63ecd026e638acc76da2691db1b82af0.png"))

@bot.command(name="user")
async def _user(ctx, user):
	"""Returns user info."""
	jsonreq=requests.get(f"https://zpet.ml/ifUser.php?user={user}")
	try:
		req=json.loads(jsonreq)
	except ValueError as e:
		return await ctx.send(embed=discord.Embed(title=f"No user found with {user}!", description=f"""
			I couldn't find the user specified! Check to make sure the username is correct.
			""").set_thumbnail(url="https://infinityfree.net/assets/apple-touch-icon-90bec27bc0c23919f97f101fb88b861f63ecd026e638acc76da2691db1b82af0.png").set_author(name="InfinityFree", url="https://infinityfree.net", icon_url="https://infinityfree.net/assets/apple-touch-icon-90bec27bc0c23919f97f101fb88b861f63ecd026e638acc76da2691db1b82af0.png"))
	
	return await ctx.send(embed=discord.Embed(title=f"Info for {req['user']}", description=f"""
		{req["description"] if req["description"] != None else "No detailed information about this user."}
		""").set_thumbnail(url=req["avatar"]).set_author(name="InfinityFree", url="https://infinityfree.net", icon_url="https://infinityfree.net/assets/apple-touch-icon-90bec27bc0c23919f97f101fb88b861f63ecd026e638acc76da2691db1b82af0.png"))

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="people using InfinityFree | Type if.help for help."), status=discord.Status.online)
	print("{0.user} is now online!".format(bot))

bot.run(token)
