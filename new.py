# -*- coding: utf-8 -*-
import discord, datetime, pytz, os
from discord import app_commands

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced
            await tree.sync(guild = discord.Object(id=848128376643911700)) #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = "명령어", description= "명령어를 보여줍니다", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction):
    embed = discord.Embed(title="도움", description="명령어 목록을 봅니다", timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                          color=0x00a2ff)

    embed.add_field(name="/명령어", value="명령어를 보여줍니다.", inline=False)
    embed.add_field(name="/게임링크", value="한국인이 만든 방탈출 Roblox 게임 링크를 보여줍니다.", inline=False)
    embed.add_field(name="/규칙", value="규칙을 봅니다.", inline=True)
    embed.add_field(name="/", value=".", inline=True)
    embed.set_footer(text="Codder : alvinbank1#5412",
                     icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
    await interaction.response.send_message(embed=embed, ephemeral = True)

@tree.command(name = "게임링크", description= "한국인이 만든 방탈출 Roblox 게임 링크를 보여줍니다.", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("https://www.roblox.com/games/4963463689/unnamed", ephemeral = True)

@tree.command(name = "인증-1", description= "인증을 완료합니다.", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction):
    if interaction.channel.id == 960454707120312350:
        try:
            embed = discord.Embed(title="인증", description="인증이 진행중 입니다. 잠시 기다려주세요",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x00a2ff)
            await interaction.user.send(embed=embed)
        except:
            await interaction.response.send_message("DM을 활성화해주세요!\n활성화 방법 : https://discord.com/channels/848128376643911700/848128451890380821/963361216410046507")
        else:
            await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name='BotVerifyed'))
            await interaction.response.send_message(interaction.user.mention + "님, 인증이 완료되었습니다.✅ <#857501980834529292>로 가주세요!")
            embed = discord.Embed(title="인증", description="인증이 완료되었습니다 ✅ <#857501980834529292>로 가주세요",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x93C54B)
            await interaction.user.send(embed=embed)
    else:
        await interaction.response.send_message("<#960454707120312350> 에서 이 명령어를 실행해 주세요!")

@tree.command(name = "공지", description= "공지를 작성합니다. (스테프만 가능)", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, content: str):
    await interaction.channel.purge(limit=1)
    i = (interaction.user.guild_permissions.administrator)
    if i is True:
        notice = content
        channel = client.get_channel(848128451890380821)
        embed = discord.Embed(title="*한국인이 만든 방탈출 공지*",
                              description="\n공지사항 내용은 항상 숙지 해주시기 바랍니다\n\n{}\n\n――――――――――――――――――――――――".format(notice),
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xf24444)
        embed.set_footer(text="Bot Made by. alvinbank1#5412 | 담당 관리자 : {}".format(interaction.user),
                         icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
        commander = discord.utils.get(interaction.guild.roles, name="공지알림")
        await channel.send(commander.mention, embed=embed)
        # await channel.send("@everyone", embed=embed)
        await interaction.user.send(
            "*[ 한국인이 만든 방탈출 봇 ]* | 정상적으로 공지가 채널에 작성이 완료되었습니다.\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(
                channel, interaction.user, notice))
        await interaction.response.send_message("공지가 작성되었습니다. ✅", ephemeral = True)

    if i is False:
        await interaction.response.send_message("{}, 당신은 관리자가 아닙니다".format(interaction.user.mention))

@tree.command(name = "밴", description= "유저를 밴 합니다.", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, user: discord.Member, reason: str):
    if interaction.user.guild_permissions.administrator:
        embed = discord.Embed(title="당신은 한국인이 만든 방탈출 서버에서 영구적으로 밴 당했습니다!",
                              description="밴 반성/항소 : https://forms.gle/Ko9vMgLesJg4u4A38",
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                              color=0x00ff00)
        embed.add_field(name="밴 담당자", value=interaction.user.mention, inline=True)
        embed.add_field(name="사유", value=reason, inline=True)
        await user.send(embed=embed)
        try :
            await user.ban(reason=reason)
        except:
            await interaction.response.send_message(user.mention + "님은 관리자 입니다!")
        else:
            embed = discord.Embed(title=user.name + "님이 서버에서 영구적으로 밴당하셨습니다.",
                                  description=user.mention,
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x00ff00)
            embed.add_field(name="밴 담당자", value=interaction.user.mention, inline=True)
            embed.add_field(name="사유", value=reason, inline=True)
            await client.get_channel(1007522175122669658).send(embed=embed)
            await interaction.response.send_message(user.mention + "님을 밴 했습니다!")
    else:
        await interaction.response.send_message("당신은 관리자가 아닙니다!")

@tree.command(name = "킥", description= "유저를 킥합니다", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, user: discord.Member, reason: str):
    if interaction.user.guild_permissions.administrator:
        embed = discord.Embed(title="당신은 한국인이 만든 방탈출 서버에서 킥 당했습니다!",
                              description="억울하다면 서버에 다시 접속해 주세요.",
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                              color=0x00ff00)
        embed.add_field(name="킥 담당자", value=interaction.user.mention, inline=True)
        embed.add_field(name="사유", value=reason, inline=True)
        await user.send(embed=embed)
        try :
            await user.kick(reason=reason)
        except:
            await interaction.response.send_message(user.mention + "님은 관리자 입니다!")
        else:
            embed = discord.Embed(title=user.name + "님이 킥이 되었습니다.",
                                  description=user.mention,
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x00ff00)
            embed.add_field(name="킥 담당자", value=interaction.user.mention, inline=True)
            embed.add_field(name="사유", value=reason, inline=True)
            await client.get_channel(1007522175122669658).send(embed=embed)
            await interaction.response.send_message(user.mention + "님을 킥 했습니다!")
    else:
        await interaction.response.send_message("당신은 관리자가 아닙니다!")

@tree.command(name = "developertestcommand", description= "개발자 테스트 커맨드 입니다. 절대 실행하지 마세요", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, string: str):
    if interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(string, ephemeral = True)
    else:
        await interaction.user.send("실행하지 말랬지")
        await interaction.user.kick()

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
