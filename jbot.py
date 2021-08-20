import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

client = discord.Client()

@client.event
async def on_message(message):
    if message.content == "!려예서":
    	msg = await message.channel.send('[바드]려예서 숙제했니?\n\n\n◼️ 카오스던전\n\n☀️ 가디언토벌\n\n♻️ 에포나의뢰\n\n💘 호감도\n\n✅ 어비스ㅣ던전 : 오레하\n\n☑️ 어비스ㅣ레이드 : 아르고스\n\n🍬 다 했다!\n\n')
    if message.content == "!차예서":
    	msg = await message.channel.send('[배틀마스터]차예서 숙제했니?\n\n\n◼️ 카오스던전\n\n☀️ 가디언토벌\n\n♻️ 에포나의뢰\n\n💘 호감도\n\n✅ 어비스ㅣ던전 : 오레하\n\n☑️ 어비스ㅣ레이드 : 아르고스\n\n🟥 군단장ㅣ발탄\n\n🟧 군단장ㅣ비아키스\n\n🟨 군단장ㅣ쿠크세이튼\n\n🟪 군단장ㅣ아브렐슈드\n\n🍬 다 했다!\n\n')
    if message.content == "!닻비야":
    	msg = await message.channel.send('[리퍼]닻비야 숙제했니?\n\n\n◼️ 카오스던전\n\n☀️ 가디언토벌\n\n♻️ 에포나의뢰\n\n💘 호감도\n\n✅ 어비스ㅣ던전 : 오레하\n\n☑️ 어비스ㅣ레이드 : 아르고스\n\n🍬 다 했다!\n\n')
    if message.content == "!라예서":
    	msg = await message.channel.send('[데모닉]라예서 숙제했니?\n\n\n◼️ 카오스던전\n\n☀️ 가디언토벌\n\n♻️ 에포나의뢰\n\n💘 호감도\n\n✅ 어비스ㅣ던전 : 오레하\n\n☑️ 어비스ㅣ레이드 : 아르고스\n\n🍬 다 했다!\n\n')
    if message.content == "!체사티":
    	msg = await message.channel.send('[소서리스]체사티 숙제했니?\n\n\n◼️ 카오스던전\n\n☀️ 가디언토벌\n\n♻️ 에포나의뢰\n\n💘 호감도\n\n✅ 어비스ㅣ던전 : 오레하\n\n☑️ 어비스ㅣ레이드 : 아르고스\n\n🍬 다 했다!\n\n')
    if message.content == "!새벽닻":
    	msg = await message.channel.send('[스트라이커]새벽닻 숙제했니?\n\n\n◼️ 카오스던전\n\n☀️ 가디언토벌\n\n♻️ 에포나의뢰\n\n💘 호감도\n\n✅ 어비스ㅣ던전 : 오레하\n\n🍬 다 했다!\n\n')
    	
    await msg.add_reaction("◼")
    await msg.add_reaction("☀️")
    await msg.add_reaction("♻️")
    await msg.add_reaction("💘")
    await msg.add_reaction("✅")
    await msg.add_reaction("☑️")
    await msg.add_reaction("🟥")
    await msg.add_reaction("🟧")
    await msg.add_reaction("🟨")
    await msg.add_reaction("🟪")
    await msg.add_reaction("🍬")



    
client.run('ODc3ODc0ODk4OTMwOTIxNDkz.YR4-tg.ulKTo52xETPTRtbjLKByEhaqUYM')
