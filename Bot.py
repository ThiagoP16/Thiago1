import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def roll(ctx, dice: str):
    "Formato NdN, por ejemplo 2d6"
    try:
        rolls, limit = map(int, dice.lower().split('d'))
    except Exception:
        await ctx.send("Formato debe ser NdN (ejemplo: 2d6)")
        return

    result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
    await ctx.send(result)

@bot.command()
async def ahorcados(ctx):
    palabras = ["avion", "python", "piloto", "computadora", "caribe", "hangar"]
    palabra = random.choice(palabras)
    palabra_oculta = ["."] * len(palabra)
    intentos = 6
    usadas = set()

    def mostrar():
        return "  ".join(palabra_oculta)

    await ctx.send(f"Juego del ahorcado iniciado!\nPalabra: {mostrar()}\nIntentos: {intentos}")

    def revisar(m):
        return m.author == ctx.author and len(m.content) == 1 and m.content.isalpha()

    while intentos > 0 and "." in palabra_oculta:
        try:
            msg = await bot.wait_for("message", check=revisar, timeout=60.0)
            letra = msg.content.lower()

            if letra in usadas:
                await ctx.send(f"Ya probaste la letra '{letra}'")
                continue

            usadas.add(letra)

            if letra in palabra:
                for i, c in enumerate(palabra):
                    if c == letra:
                        palabra_oculta[i] = letra
                await ctx.send(f"La letra {letra} está.\n{mostrar()}")
            else:
                intentos -= 1
                await ctx.send(f"La letra {letra} no está. Te quedan {intentos} intentos.\n{mostrar()}")

        except asyncio.TimeoutError:
            await ctx.send("Se acabó el tiempo.")
            return

    if "." not in palabra_oculta:
        await ctx.send(f"Felicidades! Adivinaste la palabra: {palabra}")
    else:
        await ctx.send(f"Perdiste! La palabra era: {palabra}")

bot.run("tu clave")
