#!/usr/bin/env python3
# Z3R0NET Public Profile Analyzer Bot
# Termux Compatible
# Author: Z3R0NET

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Sunucudaki izinli üyeleri görmek için
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    print("Z3R0NET Public Profile Analyzer is ready!")

# --- Kendi Profil Analizi ---
@bot.command()
async def myprofile(ctx):
    user = ctx.author
    embed = discord.Embed(title=f"{user.name}'s Profile", color=0x00ff00)
    embed.set_thumbnail(url=user.avatar.url)
    embed.add_field(name="Username", value=user.name, inline=True)
    embed.add_field(name="Discriminator", value=user.discriminator, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Bot?", value=user.bot, inline=True)
    embed.add_field(name="Top Role", value=getattr(ctx.author.top_role, "name", "None"), inline=True)
    await ctx.send(embed=embed)

# --- Public Profile Analysis ---
@bot.command()
async def profile(ctx, member: discord.Member):
    embed = discord.Embed(title=f"Public Profile: {member.name}", color=0x3498db)
    embed.set_thumbnail(url=member.avatar.url if member.avatar else None)
    embed.add_field(name="Username", value=member.name)
    embed.add_field(name="Discriminator", value=member.discriminator)
    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Bot?", value=member.bot)
    embed.add_field(name="Top Role", value=getattr(member.top_role, "name", "None"))
    embed.add_field(name="Mutual Servers", value=len([g for g in bot.guilds if member in g.members]))
    # Connected accounts (public info only)
    connections = [c.name for c in getattr(member, "activities", []) if c.type == discord.ActivityType.custom]
    embed.add_field(name="Public Connections", value=", ".join(connections) if connections else "None")
    await ctx.send(embed=embed)

# --- Server Info ---
@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f"Server Info: {guild.name}", color=0x00ffff)
    embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
    embed.add_field(name="Server ID", value=guild.id)
    embed.add_field(name="Members", value=guild.member_count)
    embed.add_field(name="Roles", value=len(guild.roles))
    embed.add_field(name="Channels", value=len(guild.channels))
    await ctx.send(embed=embed)

# --- Members List ---
@bot.command()
async def members(ctx):
    members = [f"{m.name}#{m.discriminator}" for m in ctx.guild.members]
    await ctx.send(f"👥 Members ({len(members)}):\n" + ", ".join(members[:50]) + ("..." if len(members) > 50 else ""))

bot.run("YOUR_DISCORD_BOT_TOKEN")
