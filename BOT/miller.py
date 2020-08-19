#coding:utf-8

import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import sys, traceback
import asyncio
import time
import logging


bot = commands.Bot(command_prefix = "$", description = ".")
bot.remove_command("help")


@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("                                                                                  ")
    print("      ___  ____ _ _            ______  _____ _____                                ")
    print("      |  \/  (_) | |           | ___ \|  _  |_   _|                               ")
    print("      | .  . | | | | ___ _ __  | |_/ /| | | | | |                                 ")
    print("      | |\/| | | | |/ _ \ '__| | ___ \| | | | | |                                 ")
    print("      | |  | | | | |  __/ |    | |_/ /\ \_/ / | |                                 ")
    print("      \_|  |_/_|_|_|\___|_|    \____/  \___/  \_/                                 ")
    print("                                                                                  ")
    print("                                                                                  ")
    print("      Miller est connecté !                                                       ")
    print("                                                                                  ")
    print("      Bienvenue sur la première version du BOT                                    ")
    print("      Le créateur de ce BOT est Menthings                                         ")
    print("                                                                                  ")
    print("      Voici les coordonnées de Menthings                                          ")
    print("                                                                                  ")
    print("       - GitHub   : https://github.com/Menthings                                  ")
    print("       - Twitter  : https://twitter.com/Menthinqs                                 ")
    print("       - Facebook : https://facebook.com/Menthinqs                                ")
    print("       - YouTube  : https://youtube.com/c/Menthings                               ")
    print("       - Discord  : Menthings#1337                                                ")
    print("                                                                                  ")
    print("~ Écrivez \"$help\" afin de mieux comprendre et utiliser correctement ce BOT.     ")
    print("~ Le préfix du BOT est \"$\" par défaut.\n                                        ")
    print("                                                                                  ")
    print("NB : L'historique des commandes est ici, écrivez rien sur le bash/cmd !           ")
    print("                                                                                  ")


@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "**Commandes Miller**", color = 0xfafafa)
    embed.add_field(name = "**$aboutserver**", value = "Informations à propos du serveur", inline = True)
    embed.add_field(name = "**$ban**", value = "Bannir un membre du serveur", inline = True)
    embed.add_field(name = "**$clear**", value = "Effacer un nombre spécifique de messages", inline = True)
    embed.add_field(name = "**$clearhistory**", value = "Supprimer l'historique sur le terminal", inline = True)
    embed.add_field(name = "**$help**", value = "Afficher les commandes du BOT Miller", inline = True)
    embed.add_field(name = "**$info**", value = "Informations sur un membre du serveur", inline = True)
    embed.add_field(name = "**$infos**", value = "Informations plus précise sur un membre du serveur", inline = True)
    embed.add_field(name = "**$ping**", value = "Vérifier son propre ping", inline = True)
    embed.add_field(name = "**$purge**", value = "Efface ABSOLUMENT TOUS les messages du serveur", inline = True)
    embed.add_field(name = "**$kick**", value = "Exclure un membre du serveur", inline = True)    
    embed.add_field(name = "**$unban**", value = "Révoquer le bannissement d'un membre", inline = True)
    embed.add_field(name = "**$listbanid**", value = "Liste ID des membres bannis", inline = True)
    embed.add_field(name = "**$snake**", value = "Affiche ton texte avec des lettres à la forme d'un serpent", inline = True)
    embed.add_field(name = "**$russian**", value = "Affiche ton texte avec des lettres russes", inline = True)
    embed.add_field(name = "**$street**", value = "Affiche ton texte avec des lettres du ghetto", inline = True)
    embed.add_field(name = "**$italic**", value = "Affiche ton texte avec des lettres italiques", inline = True)
    embed.add_field(name = "**$rounded**", value = "Affiche ton texte avec des lettres rondes", inline = True)
    embed.add_field(name = "**$chinese**", value = "Affiche ton texte avec des lettres chinoises", inline = True)
    embed.add_field(name = "**$striped**", value = "Affiche ton texte avec des lettres barrées", inline = True)
    embed.add_field(name = "**$clearhistory**", value = "Effacer l'historique du terminal", inline = True)

    print("\n")
    print("Tu as exécuté(e) la commande \"help\"                                                 ")
    print("\n")

    await ctx.send(embed = embed)


@bot.command()
async def aboutserver(ctx):
    server = ctx.guild
    serverName = server.name
    serverDescription = server.description
    numberPerson = server.member_count
    numberTextChannel = len(server.text_channels)
    numberVoiceChannel = len(server.voice_channels)

    embed = discord.Embed(title = "**Informations du serveur**", color = 0xfafafa)
    embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/9375_Information.png")
    embed.add_field(name = "**Nom du serveur**", value = server.name, inline = True)
    embed.add_field(name = "**Description du serveur**", value = server.description, inline = True)
    embed.add_field(name = "**Membres**", value = server.member_count, inline = True)
    embed.add_field(name = "**Salons textuels**", value = len(server.text_channels), inline = True)
    embed.add_field(name = "**Salons vocaux**", value = len(server.voice_channels), inline = True)

    print("\nTu as exécuté(e) la commande \"$aboutserver\"\n")
    print("{} est le nom du serveur.".format(server))
    print("{} est la description du serveur".format(serverDescription))
    print("{} est le nombre de membres sur le serveur.".format(server.member_count))
    print("{} est le nombre de salons textuels du serveur.".format(numberTextChannel))
    print("{} est le nombre de salons vocaux du serveur.".format(numberVoiceChannel))
    print("\n")

    await ctx.send(embed = embed)


@bot.command()
async def ping(ctx):
    await ctx.send(f"**{round(bot.latency * 1000)}ms**...\nPas ouf, sale pédale.")
    print("Tu as exécuté(e) la commande \"$ping\"")
    print("Tu as {}ms\n".format(round(bot.latency * 1000)))


@bot.command()
async def purge(ctx, amount = 9999999999999999999999999999 * 66666666666666666666666666666 * 1337 * 212):
    await ctx.channel.purge(limit=amount)
    print("Tu as exécuté(e) la commande \"$purge\"\nPlus aucune trace de toi sur ce channel.\n")


@bot.command()
async def clear(ctx, nombre : int):
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for message in messages:
        await message.delete()


@bot.command()
async def kick(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    try:
        await ctx.guild.kick(user, reason = reason)
        await ctx.send(f"**{user}** a été exclu. La raison de cette exclusion est la suivante \"**{reason}**\".")
        print(f"{user} a été exclu(e) avec succès !")
    except:
        await ctx.send(f"Tu peux pas exclure **{user}**.")
        print(f"{user} ne peut pas être exclu(e).")
    finally:
        print("\n")


@bot.command()
async def ban(ctx, user : discord.User, *reason):
    reason = " ".join()
    try:
        await ctx.guild.ban(user, reason = reason)
        await ctx.send(f"**{user}** a été définitivement banni(e) de ce serveur. La raison de ce bannissement est la suivante \"**{reason}**\".")
        print(f"{user} a été banni(e) avec succès !")
    except:
        await ctx.send(f"Non, tu peux pas bannir **{user}**.")
        print(f"{user} ne peut pas être banni(e).")
    finally:
        print("\n")


@bot.command()
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userID = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for menthings in bannedUsers:
        if menthings.user.name == userName and menthings.user.id == userID:
            await ctx.guild.unban(menthings.user, reason = reason)
            print("**{}** a été unban.\nRaison : **{}**".format(user, reason))
        else:
            await ctx.send(f"**{user}** introuvable, sale zgueg.")


@bot.command()
async def info(ctx, user : discord.Member = None):
    Named = user.name
    IDed = user.id
    Statuted = user.status
    Roled = user.top_role
    Joined = user.joined_at

    if user is None:
        await ctx.send("Et l'utilisateur ? Je le devine ?\nSale zgueg.")
        print("\nTu as oublié(e) de spécifier un utilisateur.\n")
    else:
        embed = discord.Embed(title = "**Informations**", color = 0xfafafa)
        embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/9375_Information.png")
        embed.add_field(name = "Nom d'utilisateur", value = user.name, inline = True)
        embed.add_field(name = "ID d'utilisateur", value = user.id, inline = True)
        embed.add_field(name = "Statut", value = user.status, inline = True)
        embed.add_field(name = "Rôle", value = user.top_role, inline = True)
        embed.add_field(name = "Date de création du compte", value = user.joined_at, inline = True)

        print("{} = Nom".format(Named))
        print("{} = ID".format(IDed))
        print("{} = Statut".format(Statuted))
        print("{} = Rôle sur le serveur".format(Roled))
        print("{} = Création du compte".format(Joined))

        await ctx.send(embed = embed)


@bot.command()
async def infos(ctx, user : discord.Member = None):
    Named = user.name
    IDed = user.id
    Statuted = user.status
    Roled = user.top_role
    Joined = user.joined_at 

    if user is None:
        await ctx.send("Et l'utilisateur ? Je le devine ?\nSale zgueg.")
        print("\nTu as oublié(e) de spécifier un utilisateur.\n")
    else:
        embed = discord.Embed(title="**Informations**", color = 0xfafafa)
        embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/9375_Information.png")
        embed.add_field(name = "Nom d'utilisateur", value = "{}\n*NB : {} signifie \"Grosse salope\"*".format(user.name, user.name), inline = True)
        embed.add_field(name = "ID d'utilisateur", value = user.id, inline = True)
        embed.add_field(name = "Statut", value = "offline\n*car il/elle suce une grosse bite...*", inline = True)
        embed.add_field(name = "Rôle", value = user.top_role, inline = True)
        embed.add_field(name = "Date de création du compte", value = user.joined_at, inline = True)

        print("{} = Nom".format(Named))
        print("{} = ID".format(IDed))
        print("{} = Statut".format(Statuted))
        print("{} = Rôle sur le serveur".format(Roled))
        print("{} = Création du compte".format(Joined))

        await ctx.send(embed = embed)

@bot.command()
async def clearhistory(ctx):
    os.system('cls' if os.name == 'nt' else 'clear')
    await ctx.send("Bash/cmd effacé !")
            

@bot.command()
async def listbanid(ctx):
    ids = []
    bans = await ctx.guild.bans()
    for i in bans:
        ids.append(str(i.user.id))
    embed = discord.Embed(title = "Liste ID bannis sur le serveur", color=0xfafafa)
    embed.add_field(name = "ID", value = ids, inline = True)

    await ctx.send(embed = embed)


@bot.command()
async def snake(ctx, *text):
    snakeChar = "ԹՅՇԺȝԲԳɧɿʝƙʅʍՌԾρφՐՏԵՄעաՃՎՀ"
    snakeText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = snakeChar[index]
                snakeText.append(transformed)
            else:
                snakeText.append(char)
        snakeText.append(" ")
    await ctx.send("".join(snakeText))


@bot.command()
async def rounded(ctx, *text):
    roundedChar = "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"
    roundedText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = roundedChar[index]
                roundedText.append(transformed)
            else:
                roundedText.append(char)
        roundedText.append(" ")
    await ctx.send("".join(roundedText))


@bot.command()
async def russian(ctx, *text):
    russianChar = "ДБСĎЕҒĞНІЈКLМПОРϘГЅТЦѴШХЧZ"
    russianText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = russianChar[index]
                russianText.append(transformed)
            else:
                russianText.append(char)
        russianText.append(" ")
    await ctx.send("".join(russianText))


@bot.command()
async def chinese(ctx, *text):
    chineseChar = "凡乃ㄈ刀モ下G什ﾉﾌに乚州几ロ尸Q尺らイ凵レ山ㄨㄚ乙"
    chineseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText.append(char)
        chineseText.append(" ")
    await ctx.send("".join(chineseText))

@bot.command()
async def striped(ctx, *text):
    stripedChar = "A̷B̷C̷D̷E̷F̷G̷H̷I̷J̷K̷L̷M̷N̷O̷P̷Q̷R̷S̷T̷U̷V̷W̷X̷Y̷Z̷"
    stripedText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = stripedChar[index]
                stripedText.append(transformed)
            else:
                stripedText.append(char)
        stripedText.append(" ")
    await ctx.send("".join(stripedText))


@bot.command()
async def street(ctx, *text):
    streetChar = "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ"
    streetText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = streetChar[index]
                streetText.append(transformed)
            else:
                streetText.append(char)
        streetText.append(" ")
    await ctx.send("".join(streetText))


@bot.command()
async def italic(ctx, *text):
    italicChar = "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍"
    italicText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = italicChar[index]
                italicText.append(transformed)
            else:
                italicText.append(char)
        italicText.append(" ")
    await ctx.send("".join(italicText))


bot.run("") #Token