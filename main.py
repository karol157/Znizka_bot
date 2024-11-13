import discord
import random
import string
import config

# Wprowadź swój token bota poniżej
TOKEN = config.TOKEN

# Inicjalizacja klienta bota
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Funkcja generująca losowy kod zniżkowy o długości 6 znaków
def generuj_kod_znizkowy():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Funkcja losująca zniżkę od 20% do 30%
def losuj_znizke():
    return random.randint(20, 30)

# Reakcja na event on_ready
@client.event
async def on_ready():
    print(f'Bot {client.user} jest gotowy.')

# Reakcja na wiadomości
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Sprawdza, czy wiadomość to komenda .znizka
    if message.content == '.znizka':
        kod = generuj_kod_znizkowy()
        znizka = losuj_znizke()

        # Tworzenie embeda
        embed = discord.Embed(
            title="🎉 Twój kod zniżkowy 🎉",
            description=f"Otrzymujesz **{znizka}%** zniżki!",
            color=discord.Color.blue()
        )
        # Zwiększenie czcionki kodu poprzez zastosowanie podwójnych gwiazdek i backticków
        embed.add_field(name="Kod zniżkowy", value=f"**`{kod}`**", inline=False)
        embed.set_footer(text="Wykorzystaj kod, aby skorzystać z oferty!")

        # Wysyłanie embeda
        await message.channel.send(embed=embed)

# Uruchomienie bota
client.run(TOKEN)