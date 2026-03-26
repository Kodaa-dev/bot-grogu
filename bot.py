import discord
import random
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if random.randint(1, 5) == 1:
        reponses = [
            "Wouaf !",
            "Ouaf ouaf !",
            "Grr...",
            "🐾",
            "*agite la queue*",
            "*renifle le message*",
            "*aboie dans le lointain*",
            "Ouaf ? 🐕",
            "*tourne en rond*",
            "WOUAF WOUAF WOUAF !",
            "*mordille le message*",
            "*pose sa patte sur l'écran*",
            "Wuf.",
            "*regarde avec de grands yeux*",
            "*cherche une balle*",
            "Ouaf... 😴",
            "*creuse un trou dans le serveur*",
            "*rapporte le message fièrement*",
            "🦴",
            "*s'étire et bâille*",
            "*lèche l'écran*",
            "Grouaf !",
            "*dresse les oreilles*",
            "*court dans tous les sens*",
            "Waf waf waf 🐾",
            "Wouaf... ou ne pas Wouaf. Telle est la question.",
            "*vole la collection de cartes et court*",
            "Wouaf ! J'ai banished ton personnage. Désolé pas désolé. 🃏",
        ]
        await message.channel.send(random.choice(reponses))

client.run(os.environ['TOKEN'])