# -*- coding: utf-8 -*-
# discord.py 2.0 미만
import discord, random, datetime, pytz, openpyxl, asyncio, os
from discord import DMChannel
#from discord import app_commands,ui,utils
from captcha.image import ImageCaptcha

#필수변수

#class aclient(discord.Client):
    #def __init__(self):
        #super().__init__(intents=discord.Intents.default())
        #self.synced = False #we use this so the bot doesn't sync commands more than once

    #async def on_ready(self):
        #await self.wait_until_ready()
        #if not self.synced: #check if slash commands have been synced
            #await tree.sync(guild = discord.Object(id=848128376643911700)) #guild specific: leave blank if global (global registration can take 1-24 hours)
            #self.synced = True
        #print(f"We have logged in as {self.user}.")

#bclient = aclient()
#tree = app_commands.CommandTree(bclient)
client = discord.Client(intents=discord.Intents.default())

#Global에 필요한 변수
code = random.randrange(10000, 99999)
a = False # 도배변수
today = datetime.date.today() # 사용법 : today.year, today.month, today.day, today.weekday()

async def bt(games):
    await client.wait_until_ready()
    while not client.is_closed():
        for g in games:
            await client.change_presence(activity=discord.Streaming(name=g, url='https://www.twitch.tv/alvinbank1'))
            await asyncio.sleep(5)

#클래스들


@client.event
async def on_ready():
    y = today.year
    m = today.month
    d = today.day
    print(client.user.id)
    print("ready")
    game = discord.Game(";?도움")
    await bt([";?도움","DM = 문의","방탈출 서버 감시중 👀",str(y) + "년 " + str(m) + "월 " + str(d) + "일"])
    #await client.change_presence(activity=discord.Streaming(name=";?도움", url='https://www.twitch.tv/alvinbank1'))

@client.event
async def on_message(message):
    global code
    global a
    if message.content.startswith(";?도움"):
        embed = discord.Embed(title="명령어", description="명령어 목록", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00a2ff)

        embed.add_field(name=";?도움", value="명령어를 보여줍니다.", inline=False)
        embed.add_field(name=";?게임링크", value="한국인이 만든 방탈출 Roblox 게임 링크를 보여줍니다.", inline=False)
        embed.add_field(name=";?도배시작 & ;?도배그만", value="도배를 시작하거나 중단합니다.", inline=True)
        embed.add_field(name=";?규칙", value="규칙을 봅니다.", inline=True)
        embed.set_footer(text="Codder : alvinbank1#5412", icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
        await message.author.send(embed=embed)
        await message.add_reaction("✅")
    if message.content.startswith(";?게임링크"):
        await message.author.send("https://www.roblox.com/games/4963463689/unnamed")
        await message.add_reaction("✅")
    if message.content == ";?인증":
        if message.channel.id == 960454707120312350:
            Image_Captcha = ImageCaptcha()
            a = ""
            for i in range(6):
                a += str(random.randint(0,9))
            name = str(message.author.id) + ".png"
            Image_Captcha.write(a, name)
            await message.author.send(file=discord.File(name))
            await message.author.send("인증방법 : ;?인증법")
            await message.channel.send("DM을 확인해주세요.")
            def check(msg):
                return msg.author == message.author and msg.channel == message.channel

            try:
                msg = await client.wait_for("message", timeout=20, check=check)
            except:
                await message.channel.send("실패 : 시간초과")
                return
            print(";?인증 " + a)
            if msg.content == ";?인증 " + a:
                user = message.author
                role = discord.utils.get(message.guild.roles, name='BotVerifyed')
                await user.add_roles(role)
                channel = client.get_channel(873088054825463828)
                await channel.send("인증로그 : " + message.author.mention + "님이 인증함. 인증에 사용된 코드 : ||" + a + "||")
                await message.add_reaction("✅")
                await message.channel.send("인증이 완료되었습니다.✅ <#857501980834529292>로 가주세요!")
            else:
                await message.channel.send("실패 : 캡챠가 틀렸습니다.")
        else:
            await message.channel.send("<#960454707120312350>에서 명령어를 사용해주세요.")
    if message.content.startswith(";?공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(848128451890380821)
            embed = discord.Embed(title="*한국인이 만든 방탈출 공지*",description="\n공지사항 내용은 항상 숙지 해주시기 바랍니다\n\n{}\n\n――――――――――――――――――――――――".format(notice), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xf24444)
            embed.set_footer(text="Bot Made by. alvinbank1#5412 | 담당 관리자 : {}".format(message.author), icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
            commander = discord.utils.get(message.guild.roles, name="공지알림")
            await channel.send(commander.mention, embed=embed)
            #await channel.send("@everyone", embed=embed)
            await message.author.send(
                "*[ 한국인이 만든 방탈출 봇 ]* | 정상적으로 공지가 채널에 작성이 완료되었습니다.\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(
                    channel, message.author, notice))

        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))
    if message.content.startswith(";?인증법"):
        await message.author.send("인증법은 아레 GIF를 참고해주세요.")
        await message.author.send("https://i.ibb.co/jMkTNgp/howtoverify.gif")
        await message.add_reaction("✅")
    if message.content.startswith(";?도배시작"):
        a = True
        await message.add_reaction("✅")
        while a == True:
            await message.author.send(message.author.mention)
    if message.content.startswith(";?도배그만"):
        a = False
        await message.add_reaction("✅")
    if message.content.startswith(";?스테프신청"):
        channel = client.get_channel(960848181049049158)
        await channel.send(message.author.mention + " 스테프 신청")
        await message.channel.send("인증이 완료되었습니다.✅")
    if message.content.startswith(";?보안팀신청"):
        channel = client.get_channel(960848181049049158)
        await channel.send(message.author.mention + " 보안팀 신청")
        await message.channel.send("인증이 완료되었습니다.✅")
    if message.content == ";?규칙":  # 메세지 감지
        embed = discord.Embed(title="한국인이 만든 방탈출 규칙", description="규칙을 꼭 읽어주시고 서버활동을 시작해주세요.", timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                              color=0x00ff00)

        embed.add_field(name="규칙", value="욕설 금지 (경고 2), 한국인이 만든 방탈출 플레이 필수!!! 한국인이 만든 방탈출 외 채팅 금지( <#871690167436587039> 제외), 부계정 금지(의심되면 부계정 추방, 확실하면 본계정 과 부계정 모두 차단), 반말(경고 1),  홍보 금지 (경고1, <#857508231651000360> 제외), <#871691509035049000> 에서 바이러스(핵 등)을 올리기 금지 (차단, 삭제), 링크 (메세지 삭제), 알트계정 금지(밴), 기타(경고 또는 차단) (수정이 될 수도 있습니다.) <#854309387500912641>  채널에선 대부분의 규칙이 적용되지 않습니다! (2022/4/6 수정) ", inline=False)
        embed.add_field(name="안내", value="*여기에 없다고 해도 되는거 아닙니다. 스테프 또는 보안팀이 판단하기에 경고 또는 밴이 필요하다 싶을땐 규칙에 없더라고 경고 또는 밴을 당할수 있습니다.", inline=False)
        embed.set_footer(text="규칙 작성자 : alvinbank1#5412", icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
        await message.author.send(embed=embed)
        await message.add_reaction("✅")
    if message.channel.id == 960454707120312350:
        if message.content == ";?인증법" or message.content.startswith(";?인증") or message.author == client.user:
            return
        else:
            await message.delete()
            await message.author.send("<#960454707120312350>에선, `;?인증` 또는 `;?인증법` 명령어 이외엔 사용이 불가합니다.")
    if message.channel.id == 850944602722926604 and message.author.id != 426537812993638400:
        try:
            await message.delete()
        except:
            return
        finally:
            await message.author.send("<#850944602722926604>에선, `/verify` 명령어 이외엔 사용이 불가합니다.")
    if message.content.startswith(";?경고"):
        if message.author.guild_permissions.administrator == True:
            author = await client.fetch_user(int(message.content[7:25]))
            file = openpyxl.load_workbook("warning.xlsx")
            sheet = file.active
            i = 1
            while True:
                if sheet["A" + str(i)].value == str(message.content[7:25]):
                    sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                    file.save("warning.xlsx")
                    if sheet["B" + str(i)].value > 2:
                        try:
                            await author.send("당신은 한국인이 만든 방탈출 서버에서 영구적으로 밴당하셨습니다. 사유 : 경고 총 누적 3회\n밴 취소 요청 : https://forms.gle/GUzhi5CAgf9FJDye6")
                        except:
                            try:
                                await message.guild.ban(user=author)
                            except:
                                await message.channel.send(":x: 관리자를 밴할수 없습니다!")
                            else:
                                await message.channel.send("경고 3회 누적으로, <@" + str(message.content[7:25]) + "> 님이 영구 밴당하셨습니다.")
                                channel = client.get_channel(1007522175122669658)
                                embed = discord.Embed(title=message.author.name + "님이 서버에서 영구적으로 밴당하셨습니다.",
                                                      description=message.author.mention,
                                                      timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                                      color=0x00ff00)
                                embed.add_field(name="사유", value="경고 총 누적 3회", inline=True)
                                await channel.send(embed=embed)
                        else:
                            try:
                                await message.guild.ban(user=author)
                            except:
                                await message.channel.send(":x: 관리자를 밴할수 없습니다!")
                            else:
                                await message.channel.send("경고 3회 누적으로, <@" + str(message.content[7:25]) + "> 님이 영구 밴당하셨습니다.")
                                channel = client.get_channel(1007522175122669658)
                                embed = discord.Embed(title=message.author.name + "님이 서버에서 영구적으로 밴당하셨습니다.",
                                                      description=message.author.mention,
                                                      timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                                      color=0x00ff00)
                                embed.add_field(name="사유", value="경고 총 누적 3회", inline=True)
                                await channel.send(embed=embed)
                    else:
                        await message.channel.send("<@" + str(message.content[7:25]) + "> 님이 " + message.author.mention + " 님에게 경고를 1개 받았습니다.")
                        await author.send("당신은 한국인이 만든 방탈출 서버에서 경고 1개를 받았습니다.")
                        channel = client.get_channel(1007522175122669658)
                        embed = discord.Embed(title=message.author.name + "님이 경고를 1개 받았습니다.",
                                              description=message.author.mention,
                                              timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                        await channel.send(embed=embed)
                    break
                if sheet["A" + str(i)].value == None:
                    sheet["A" + str(i)].value = str(message.content[7:25])
                    sheet["B" + str(i)].value = 1
                    file.save("warning.xlsx")
                    await message.channel.send("<@" + str(message.content[7:25]) + "> 님이 " + message.author.mention + " 님에게 경고를 1개 받았습니다.")
                    await author.send("당신은 한국인이 만든 방탈출 서버에서 경고 1개를 받았습니다.")
                    channel = client.get_channel(1007522175122669658)
                    embed = discord.Embed(title=message.author.name + "님이 경고를 1개 받았습니다.",
                                          description=message.author.mention,
                                          timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    await channel.send(embed=embed)
                    break
                i += 1
    if message.content.startswith(";?밴"):
        if message.author.guild_permissions.administrator == True:
            author = await client.fetch_user(int(message.content[6:24]))
            try:
                await author.send("당신은 한국인이 만든 방탈출 서버에서 영구적으로 밴당하셨습니다. 사유 : " + message.content[25:] + "\n밴 취소 요청 : https://forms.gle/GUzhi5CAgf9FJDye6")
            except:
                try:
                    await message.guild.ban(user=author, reason=message.content[25:])
                except:
                    await message.channel.send(":x: 관리자를 밴할수 없습니다!")
                else:
                    await message.channel.send("<@" + str(message.content[6:24]) + "> 님이 " + message.author.mention + "에 의하여 영구 밴당하셨습니다.")
                    channel = client.get_channel(1007522175122669658)
                    embed = discord.Embed(title=message.author.name + "님이 서버에서 영구적으로 밴당하셨습니다.",
                                          description=message.author.mention,
                                          timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.add_field(name="사유", value=message.content[25:], inline=True)
                    await channel.send(embed=embed)
            else:
                try:
                    await message.guild.ban(user=author, reason=message.content[25:])
                except:
                    await message.channel.send(":x: 관리자를 밴할수 없습니다!")
                else:
                    await message.channel.send("<@" + str(message.content[6:24]) + "> 님이 " + message.author.mention + "에 의하여 영구 밴당하셨습니다.")
                    channel = client.get_channel(1007522175122669658)
                    embed = discord.Embed(title=message.author.name + "님이 서버에서 영구적으로 밴당하셨습니다.",
                                          description=message.author.mention,
                                          timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.add_field(name="사유", value=message.content[25:], inline=True)
                    await channel.send(embed=embed)
        else:
            await message.channel.send(":x: 당신은 관리자가 아닙니다!")
    if message.content.startswith(";?킥"):
        if message.author.guild_permissions.administrator == True:
            author = await client.fetch_user(int(message.content[6:24]))
            try:
                await author.send("당신은 한국인이 만든 방탈출 서버에서 킥당하셨습니다. 사유 : " + message.content[25:])
            except:
                try:
                    await message.guild.kick(user=author, reason=message.content[25:])
                except:
                    await message.channel.send(":x: 관리자를 킥할수 없습니다!")
                else:
                    await message.channel.send("<@" + str(message.content[6:24]) + "> 님이 " + message.author.mention + "에 의하여 킥당하셨습니다.")
                    channel = client.get_channel(1007522175122669658)
                    embed = discord.Embed(title=message.author.name + "님이 서버에서 영구적으로 밴당하셨습니다.",
                                          description=message.author.mention,
                                          timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.add_field(name="사유", value=message.content[25:], inline=True)
                    await channel.send(embed=embed)
            else:
                try:
                    await message.guild.kick(user=author, reason=message.content[25:])
                except:
                    await message.channel.send(":x: 관리자를 킥할수 없습니다!")
                else:
                    await message.channel.send("<@" + str(message.content[6:24]) + "> 님이 " + message.author.mention + "에 의하여 킥당하셨습니다.")
                    channel = client.get_channel(1007522175122669658)
                    embed = discord.Embed(title=message.author.name + "님이 서버에서 킥당하셨습니다.",
                                          description=message.author.mention,
                                          timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.add_field(name="사유", value=message.content[25:], inline=True)
                    await channel.send(embed=embed)
        else:
            await message.channel.send(":x: 당신은 관리자가 아닙니다!")
    if message.content == "<@960096117842923553>":
        await message.author.send(message.author.mention + "\nhttps://bit.ly/3jC2CmS")
        await message.add_reaction("🎉")
    if message.content.startswith(";?정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title=message.author.name+"님의 정보", description=message.author.mention + "님의 정보입니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name="닉네임", value=message.author.name, inline=True)
        embed.add_field(name="서버 닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일 " + str(date.hour) + "시 " + str(date.minute) + "분", inline=True)
        embed.add_field(name="아이디", value=message.author.id)
        embed.set_footer(text="Coder : alvinbank1#5412", icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.author.send()
        await message.add_reaction("✅")
    if message.content.startswith("http"):
        channel = client.get_channel(1007519970382589992)
        embed = discord.Embed(title=message.author.name + "님이 방금 보낸 메세지가 삭제되었습니다.", description=message.author.mention,
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name="사유", value="링크 사용", inline=True)
        embed.add_field(name="원본 메세지", value=message.content, inline=True)
        await channel.send(embed=embed)
        await message.delete()
        await message.author.send("당신이 방금 보낸 메세지가 삭제되었습니다. 사유 : 링크 사용")
    if message.content.startswith("www."):
        channel = client.get_channel(1007519970382589992)
        embed = discord.Embed(title=message.author.name + "님이 방금 보낸 메세지가 삭제되었습니다.", description=message.author.mention,
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name="사유", value="링크 사용", inline=True)
        embed.add_field(name="원본 메세지", value=message.content, inline=True)
        await channel.send(embed=embed)
        await message.delete()
        await message.author.send("당신이 방금 보낸 메세지가 삭제되었습니다. 사유 : 링크 사용")
    #if message.content.startswith("<@"):
        #channel = client.get_channel(1007519970382589992)
        #embed = discord.Embed(title=message.author.name + "님이 방금 보낸 메세지가 삭제되었습니다.", description=message.author.mention,
        #                      timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        #embed.add_field(name="사유", value="사용자 맨션", inline=True)
        #embed.add_field(name="원본 메세지", value=message.content, inline=True)
        #await channel.send(embed=embed)
        #await message.delete()
        #await message.author.send("당신이 방금 보낸 메세지가 삭제되었습니다. 사유 : 사용자 맨션")
    if message.content.startswith("discord."):
        channel = client.get_channel(1007519970382589992)
        embed = discord.Embed(title=message.author.name + "님이 방금 보낸 메세지가 삭제되었습니다.", description=message.author.mention,
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name="사유", value="초대 링크 사용", inline=True)
        embed.add_field(name="원본 메세지", value=message.content, inline=True)
        await channel.send(embed=embed)
        await message.delete()
        await message.author.send("당신이 방금 보낸 메세지가 삭제되었습니다. 사유 : 초대 링크 사용")
    #modmail
    empty_array = []
    modmail_channel = client.get_channel(961195825306951700)
    if message.channel.id == 961195825306951700:
        if message.content.startswith(";?답변"):
            user = await client.fetch_user(message.content[5:23])
            msg = message.content[24:]
            await DMChannel.send(user, "[ 답변 " + message.author.mention + "] " + str(msg))
        if message.content.startswith(";?종료"):
            user = await client.fetch_user(message.content[5:23])
            await DMChannel.send(user, "문의가 종료되었습니다. 사유 : " + message.content[24:])
    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + str(message.author.id) + ", " + message.author.mention + " ||@here|| ]")
            await message.channel.send("[ 문의 " + message.author.mention + "]")
            for file in files:
                await modmail_channel.send(file.url)
                await message.channel.send(file.url)
        else:
            await modmail_channel.send("[" + str(message.author.id) + ", " + message.author.mention + " ||@here|| ] " + message.content)
            await message.channel.send("[ 문의 " + message.author.mention + "] " + message.content)

    elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + str(message.author.id) + ", " + message.author.mention + " ||@here|| ]")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("[" + str(message.author.id) + ", " + message.author.mention + " ||@here|| ]" + mod_message)

#@tree.command(guild=discord.Object(id=848128376643911700),name="규칙",description="서버 규칙을 봅니다")
#async def slash(interaction: discord.Interaction):
    #embed = discord.Embed(title="한국인이 만든 방탈출 규칙", description="서버 규칙 : https://docs.google.com/document/d/1tAcK39XXV6YXDFlcEynNkOSWDvM2nD_OyHi0d1Hvkmo/edit?usp=sharing",
                          #timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                          #color=0x00ff00)
    #await interaction.response.send_message(embed=embed)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
