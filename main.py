import os
import discord
import requests
import json
import random
from replit import db

# To keep the bot alive, go to [uptimerobot.com] and create new monitor
# Running the bot you will see the domain in the website part
# This monitor will ping the url from every interval time set

from keep_alive import keepAlive

token = os.environ['discord_bot_token']
client = discord.Client()


def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	author = json_data[0]['a']
	quote = json_data[0]['q'] + " - " + author
	return quote


def add_encouragements(message):
	if "encouragements" in db.keys():
		encouragements = db["encouragements"]
		encouragements.append(message)
		db["encouragements"] = encouragements
	else:
		db["encouragements"] = [message]


def delete_encouragement(index):
	encouragements = db["encouragements"]
	if len(encouragements) > index:
		del encouragements[index]
		db["encouragements"] = encouragements


sad_words = [
	"sad", "unhappy", "sorrow", "dejected", "regret", "depress", "miserable",
	"down", "despondent", "despair", "disconsolate", "desolate", "wretched",
	"glum", "gloomy", "doleful"
]

encourage = [
	"Cheer up!", "Hang in there.", "Never give up.",
	"You are a great person! ><",
	"Don't worry there's always someone thinking about you."
]

if "responding" in db.keys():
	db["responding"] = True
else:
	db["responding"] = True


@client.event
async def on_ready():
	print('\nThe bot logged in as {0.user}'.format(client))
	print('Response status is', db["responding"])


@client.event
async def on_message(msg):
	if msg.author == client.user:
		return

	msgContent = msg.content

	if msgContent.startswith('!help'):
		await msg.channel.send('''
This bot is used to encourage you by using a quote when you tell it if you are feeling down. It\'s not the best but it will try.
List of command:
[+] "!inspire" - print a inspire statement
[+] "!list" - print quote list
[+] "!add {string}" - add a quote
[+] "!del {index}" - delete a quote
[+] "!response {boolean}" - add a quote
		''')


	if msgContent.startswith('!hello'):
		await msg.channel.send('Hello there. Hope you have a great day.')

	if msgContent.startswith('!inspire'):
		quote = get_quote()
		await msg.channel.send(quote)

	if db["responding"]:
		options = encourage
		if "encouragements" in db.keys():
			options = options + list(db["encouragements"])

	if any(word in msgContent for word in sad_words):
		await msg.channel.send(random.choice(options))

	if msgContent.startswith('!add'):
		message = msgContent.split("!add ", 1)[1]
		add_encouragements(message)
		await msg.channel.send("New encouraging message added!")

	if msgContent.startswith("!del"):
		encouragements = []
		if "encouragements" in db.keys():
			index = int(msgContent.split("!del", 1)[1])
			delete_encouragement(index)
			encouragements = db['encouragements']
		await msg.channel.send("An encouraging deleted!")
		await msg.channel.send(list(encouragements))

	if msgContent.startswith("!list"):
		encouragements = []
		if "encouragements" in db.keys():
			encouragements = list(db["encouragements"]) + encourage
		await msg.channel.send(encouragements)

	if msgContent.startswith("!response"):
		try:
			value = msgContent.split("!response ", 1)[1]
		except:
			await msg.channel.send(db["responding"])
			return

		if value.lower() == "true" or value.lower() == "1":
			db["responding"] = True
			await msg.channel.send("Responding set to TRUE")
		elif value.lower() == "false" or value.lower() == "0":
			db["responding"] = False
			await msg.channel.send("Responding set to False")
		else:
			await msg.channel.send("True or False only!")


keepAlive()
client.run(token)
