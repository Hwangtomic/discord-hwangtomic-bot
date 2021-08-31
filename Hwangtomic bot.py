import discord, asyncio 
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!조기 멍청이'):
        await message.channel.send('맞음 조기는 멍청이임 ㅇㅇ')

    if message.content.startswith('!로그 멍청이'):
        await message.channel.send('흠.... ')
        await message.channel.send('.....내가 생각하기에 로그는 안멍청함')

    if message.content.startswith('!도배'):
        await message.channel.send('나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇')
        await message.channel.send('나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇')
        await message.channel.send('나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇')
        await message.channel.send('나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇')
        await message.channel.send('나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇')
        await message.channel.send('나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇')
        await message.channel.send('나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇')
        await message.channel.send('나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇 나는야 황토믹 봇')
        await message.channel.send('....')  
        await message.channel.send('정말 이래도 도배를 원해?')

    if message.content.startswith('!우월이 멍청이'):
        await message.channel.send('와 너 어떻게 알았냐 ;; 그거 국가 기밀인데 ;;')
        await message.channel.send('쨌든 우월이 멍청이')

    if message.content.startswith('!파파봇 멍청이'):
            await message.channel.send('흠....')
            await message.channel.send('뭔 소리야! _cos_를 곱하라니까!!!')
    
    if message.content.startswith('!토믹 멍청이'):
        await message.channel.send("{}, 내가 너보단 나아".format(message.author.mention))

    if message.content.startswith('!테스트'):
        ch = client.get_channel(816281959830913027)
        await ch.send ("{},와 안녕 테스트".format(message.author.mention))

    if message.content.startswith('!임배드'):
        embed = discord.Embed(title="임배드",description="에ㅔ에에ㅔ에", color=0x00ff00)


        embed.add_field(name="황토믹", value="이거 만드느라 황토믹 겁나 고생함", inline=False)
        embed.add_field(name="조기", value="먼가 조기는 맛있음", inline=False)

        embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AKedOLTuoIeuazWptHPaxGLQ1zQjH8gR9lSWdT5RjXWmpQ=s900-c-k-c0x00ffffff-no-rj")
        await message.channel.send (embed=embed)

    if message.content.startswith ("!오호라"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.send_messages)
        if i is True:
            notice = message.content[4:]
        embed = discord.Embed(title="**오호라**", description="오호오오오오라\n________________\n\n흠\n________________", color=0x00ff00)
        embed.set_footer(text="....오호라")
        await message.channel.send ("@everyone", embed=embed)
        await message.channel.send("_이예에에에에에_")

        if i is False:
            await message.channel.send("{}, 넌 못함 ㅅㄱ".format(message.author.mention))


    if message.content.startswith ("!청소"):
        q = (message.author.guild_permissions.administrator)
        
        if q is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메세지 삭제 알림", description="관리자 {}님의 요청으로 메세지가 삭제되었습니다.\n\n삭제된 메세지의 갯수 :{} ".format(message.author.mention, amount), color=0x00ff00)
            await message.channel.send (embed=embed)

        if q is False:
            await message.channel.send("{} , 넌 권한 없어서 못함 ㅅㄱ".format(message.author.mention))





access_token = os.environ["bot_token"]
client.run(access_token)
