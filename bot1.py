import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='&', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def zar(ctx):
    sayi = random.randint(1, 6)
    await ctx.send(f"Zar sonucu: {sayi}!")

@bot.command()
async def futbol(ctx):
    futbolcular = ["Mbappe", "Yamal", "Vinicius", "Haaland"]
    secilen_futbolcu = random.choice(futbolcular)
    await ctx.send(f"Seçtiğin futbolcu: {secilen_futbolcu}!")


@bot.command()
async def renk(ctx):
    renkler = ["kırmızı", "mavi", "yeşil", "sarı"]
    secilen_renk = random.choice(renkler)
    await ctx.send(f"Seçtiğin renk: {secilen_renk}!")

@bot.command()
async def oyun(ctx):
    oyunlar = ["Fortnite", "Minecraft", "Roblox", "FC 27"]
    secilen_oyun = random.choice(oyunlar)
    await ctx.send(f"Seçtiğin oyun: {secilen_oyun}!")

@bot.command()
async def topla(ctx, sayi1: int, sayi2: int):
    sonuc = sayi1 + sayi2
    await ctx.send(f"Sonuç: {sonuc}")

@bot.command()
async def kare(ctx, sayi: int):
    sonuc = sayi * sayi
    await ctx.send(f"{sayi} sayısının karesi: {sonuc}")

@bot.command()
async def cikar(ctx, sayi1: int, sayi2: int):
    sonuc = sayi1 - sayi2
    await ctx.send(f"Sonuç: {sonuc}")

@bot.command()
async def carp(ctx, sayi1: int, sayi2: int):
    sonuc = sayi1 * sayi2
    await ctx.send(f"Sonuç: {sonuc}")

@bot.command()
async def bol(ctx, sayi1: int, sayi2: int):
    if sayi2 == 0:
        await ctx.send("Sıfıra bölme yapılamaz!")
    else:
        sonuc = sayi1 / sayi2
        await ctx.send(f"Sonuç: {sonuc}")

@bot.command()
async def tekcift(ctx, sayi: int):
    if sayi % 2 == 0:
        await ctx.send(f"{sayi} çift sayıdır!")
    else:
        await ctx.send(f"{sayi} tek sayıdır!")

@bot.command()
async def kesir(ctx, pay: int, payda: int):
    sonuc = pay / payda
    await ctx.send(f"{pay}/{payda} = {sonuc}")













bot.run("TOKEN")