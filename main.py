import discord
import random
import string
import config

TOKEN = config.TOKEN

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def generuj_kod_znizkowy():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def losuj_znizke():
    return random.randint(20, 30)

@client.event
async def on_ready():
    print(f'Bot {client.user} jest gotowy.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '.znizka':
        kod = generuj_kod_znizkowy()
        znizka = losuj_znizke()

        embed = discord.Embed(
            title="🎉 Twój kod zniżkowy 🎉",
            description=f"Otrzymujesz **{znizka}%** zniżki!",
            color=discord.Color.blue()
        )
        embed.add_field(name="Kod zniżkowy", value=f"**`{kod}`**", inline=False)
        embed.set_footer(text="Wykorzystaj kod, aby skorzystać z oferty!")

        # Wysyłanie embeda
        await message.channel.send(embed=embed)

client.run(TOKEN)
