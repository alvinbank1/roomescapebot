# -*- coding: utf-8 -*-
import discord, datetime, pytz, asyncio, openpyxl, random, openai
from discord import app_commands, DMChannel, File
from discord.ui import Button, View
from captcha.image import ImageCaptcha
#from easy_pil import Editor, load_image_async, Font

class commands(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="기본 명령어", emoji="🤖", description="기본 명령어를 보여줍니다"),
            discord.SelectOption(label="특수 명령어", emoji="🔧", description="특수한 명령어를 보여줍니다"),
            discord.SelectOption(label="관리자 명령어", emoji="🛠", description="관리자 명령어를 보여줍니다"),
            discord.SelectOption(label="소유자 명령어", emoji="🔨", description="소유자 명령어를 보여줍니다"),
        ]
        super().__init__(placeholder="명령어 카테고리를 선택하세요", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
        if self.values[0] == "기본 명령어":
            embed = discord.Embed(title="도움", description="명령어 목록을 봅니다",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x00a2ff)

            embed.add_field(name="/명령어", value="명령어를 보여줍니다.", inline=False)
            embed.add_field(name="/게임링크", value="한국인이 만든 방탈출 Roblox 게임 링크를 보여줍니다.", inline=False)
            embed.add_field(name="/규칙", value="규칙을 봅니다.", inline=True)
            embed.add_field(name="/피드백", value="방탈출 게임 피드백을 보냅니다", inline=True)
            #embed.add_field(name="/내정보", value="자신의 정보를 보여줍니다", inline=True)
            embed.add_field(name="/chat-gpt", value="챗 GPT에게 물어보세요!", inline=True)
            embed.add_field(name="/credit", value="크레딧을 보여줍니다", inline=True)
            embed.set_footer(text="Codder : alvinbank1#5412",
                             icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
            await interaction.response.edit_message(embed=embed, view=SelectViewCommands())
        elif self.values[0] == "특수 명령어":
            embed = discord.Embed(title="도움", description="명령어 목록을 봅니다",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x00a2ff)

            embed.add_field(name="/스테프신청", value="스테프 신청 인증을 합니다", inline=False)
            embed.set_footer(text="Codder : alvinbank1#5412",
                             icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
            await interaction.response.edit_message(embed=embed, view=SelectViewCommands())
        elif self.values[0] == "관리자 명령어":
            if interaction.user.guild_permissions.manage_messages:
                embed = discord.Embed(title="도움", description="명령어 목록을 봅니다",
                                      timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                      color=0x00a2ff)

                embed.add_field(name="/경고", value="유저를 경고합니다", inline=False)
                embed.add_field(name="/킥", value="유저를 킥합니다", inline=False)
                embed.add_field(name="/밴", value="유저를 밴합니다", inline=True)
                embed.add_field(name="/잠구기", value="채널을 잠급니다 (메세지 작성 불가)", inline=True)
                embed.add_field(name="/잠금해제", value="채널 잠금을 해제합니다 (메세지 작성 가능)", inline=True)
                embed.add_field(name="/잠구기", value="채널을 잠급니다 (메세지 작성 불가)", inline=True)
                embed.add_field(name="/알림", value="유저에게 중요 알림을 보냅니다", inline=True)
                embed.set_footer(text="Codder : alvinbank1#5412",
                                 icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
                await interaction.response.edit_message(embed=embed, view=SelectViewCommands())
            else:
                await interaction.response.send_message(":x: 당신은 관리자가 아닙니다!", ephemeral=True)
        elif self.values[0] == "소유자 명령어":
            if interaction.user.guild_permissions.administrator:
                embed = discord.Embed(title="도움", description="명령어 목록을 봅니다",
                                      timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                      color=0x00a2ff)

                embed.add_field(name="/developertestcommand", value="개발자용 테스트 명령어 입니다", inline=False)
                embed.add_field(name="/셧다운", value="봇을 셧다운 합니다.", inline=False)
                embed.set_footer(text="Codder : alvinbank1#5412",
                                 icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
                await interaction.response.edit_message(embed=embed, view=SelectViewCommands())
            else:
                await interaction.response.send_message(":x: 당신은 소유자가 아닙니다!", ephemeral=True)

class SelectViewCommands(discord.ui.View):
    def __init__(self, *, timeout=30):
        super().__init__(timeout=timeout)
        self.add_item(commands())

class FeedbackModal(discord.ui.Modal, title="피드벡을 보내주세요"):
    fb_title = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="제목",
        required=True,
        max_length=30,
        placeholder="피드벡 제목을 입력해 주세요."
    )

    message = discord.ui.TextInput(
        style=discord.TextStyle.long,
        label="메세지",
        required=True,
        max_length=500,
        placeholder="피드벡을 입력해 주세요.",
    )
    async def on_submit(self, interaction: discord.Interaction):
        channel = interaction.guild.get_channel(1054331031395766286)
        embed = discord.Embed(title="새로운 피드벡", description="새로운 피드벡이 있습니다!")
        embed.add_field(name="유저", value=self.user.mention, inline=False) # 경고 무시
        embed.add_field(name="피드벡 제목", value=self.fb_title.value, inline=False)
        embed.add_field(name="메세지", value=self.message.value, inline=False)
        await channel.send(embed=embed)
        await interaction.response.send_message(":white_check_mark: 피드벡이 보내졌습니다. 피드벡 감사합니다!")
    async def on_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message(":x: 뭔가 잘못됐어요. 다시 시도해 주세요.\n만약 다시 시도했는데도 같은 오류가 발생한다면 문의해 주세요.")

class VerifyModal(discord.ui.Modal, title="인증을 완료해주세요"):
    code = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="인증코드",
        required=True,
        min_length=6,
        max_length=6,
        placeholder="인증코드를 입력해 주세요."
    )
    async def on_submit(self, interaction: discord.Interaction):
        if self.code.value == a:
            await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name='BotVerifyed'))
            embed = discord.Embed(title="인증", description="인증이 완료되었습니다 ✅ <#857501980834529292>로 가주세요!",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x93C54B)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            embed = discord.Embed(title="인증", description="인증이 완료되었습니다 ✅ <#857501980834529292>로 가주세요!",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x93C54B)
            await interaction.user.send(embed=embed)
            channel = client.get_channel(873088054825463828)
            embed = discord.Embed(title="인증 로그", description=interaction.user.mention + "님이 인증하였습니다!",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x93C54B)
            embed.add_field(name="인증 유저", value=interaction.user.mention, inline=True)
            embed.add_field(name="코드", value=self.code.value, inline=True)
            embed.add_field(name="맞는 코드", value=a, inline=True)
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(title="인증", description="코드가 맞지 않습니다.",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0xff0000)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            channel = client.get_channel(873088054825463828)
            embed = discord.Embed(title="인증 로그", description=interaction.user.mention + "님이 인증에 실패하였습니다",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="인증 유저", value=interaction.user.mention, inline=True)
            embed.add_field(name="코드", value=self.code.value, inline=True)
            embed.add_field(name="맞는 코드", value=a, inline=True)
            await channel.send(embed=embed)
    async def on_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message(":x: 뭔가 잘못됐어요. 다시 시도해 주세요.\n만약 다시 시도했는데도 같은 오류가 발생한다면 문의해 주세요.", ephemeral=True)

class NoticeModal(discord.ui.Modal, title="유저에게 중요 알림을 보냅니다"):

    ui_title = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="제목",
        required=True,
        max_length=30,
        placeholder="중요 알림 제목을 입력해 주세요"
    )

    message = discord.ui.TextInput(
        style=discord.TextStyle.long,
        label="메세지",
        required=True,
        max_length=1700,
        placeholder="중요 알림 메세지를 입력해 주세요.",
    )
    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title="중요 알림", description="Alvin 그룹 중요 알림이 있습니다",
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                              color=0xff0000)

        embed.add_field(name="제목", value=self.ui_title, inline=False)
        embed.add_field(name="내용", value=self.message, inline=False)
        embed.set_footer(text="작성자: " + interaction.user.name)
        await self.user.send(embed=embed)
        button1 = Button(label="알림 보기", style=discord.ButtonStyle.success, emoji="🔍")

        async def button_callback(interaction):
            await interaction.response.send_message(embed=embed, ephemeral=True)

        button1.callback = button_callback
        view = View()
        view.add_item(button1)
        await interaction.response.send_message("메세지를 성공적으로 보냈습니다 :white_check_mark:", view=view, ephemeral=True)
    async def on_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message(":x: 뭔가 잘못됐어요. 다시 시도해 주세요.\n만약 다시 시도했는데도 같은 오류가 발생한다면 문의해 주세요.")

class AnnouncmentModal(discord.ui.Modal, title="유저에게 중요 알림을 보냅니다"):
    message = discord.ui.TextInput(
        style=discord.TextStyle.long,
        label="메세지",
        required=True,
        max_length=2000,
        placeholder="공지 내용을 입력해 주세요.",
    )
    async def on_submit(self, interaction: discord.Interaction):
        notice = self.message
        channel = client.get_channel(848128451890380821)
        embed = discord.Embed(title="*Alvin 그룹 공지*",
                              description="\n공지사항 내용은 항상 숙지 해주시기 바랍니다\n\n{}\n\n――――――――――――――――――――――――".format(notice),
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xf24444)
        embed.set_footer(text="Bot Made by. alvinbank1#5412 | 담당 관리자 : {}".format(interaction.user),
                         icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
        commander = discord.utils.get(interaction.guild.roles, name="공지알림")
        if self.important == True:
            await channel.send("@everyone", embed=embed)
        else:
            await channel.send(commander.mention, embed=embed)
        await interaction.user.send(
            "*[ Alvin 그룹 봇 ]* | 정상적으로 공지가 채널에 작성이 완료되었습니다.\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(
                channel, interaction.user, notice))
        await interaction.response.send_message("공지가 작성되었습니다. ✅")
    async def on_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message(":x: 뭔가 잘못됐어요. 다시 시도해 주세요.\n만약 다시 시도했는데도 같은 오류가 발생한다면 문의해 주세요.")


class aclient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.synced = False  # we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:  # check if slash commands have been synced
            await tree.sync(guild=discord.Object(
                id=848128376643911700))  # guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")
        await client.get_channel(960443903251714068).send("리붓 완료 ✅")


client = aclient()
tree = app_commands.CommandTree(client)
today = datetime.date.today()
a = ""
count = 1
openai.api_key = 'YOUR_KEY_HERE'

# @client.event
# async def on_member_join(member):
#     background = Editor("black.png")
#     profile_image = await load_image_async(str(member.avatar.url))
#
#     profile = Editor(profile_image).resize((150,150)).circle_image()
#     poppins = Font.poppins(size=50, variant="bold")
#
#     poppins_small = Font.poppins(size=20, variant="light")
#
#     background.paste(profile, (325, 90))
#     background.ellipse((325, 90), 150, 150, outline="white",stroke_width=5)
#
#     background.text((400, 260), f"{member.guild.name}에 오신것을 환영합니다!", color="white", font=poppins, align="center")
#     background.text((400, 325), f"{member.name}#{member.discriminator}", color="white", font=poppins_small, align="center")
#
#     file = File(fp=background.image_bytes, filename="pic1.png")
#     guild = client.get_guild(848128376643911700)
#     channel = guild.get_channel(848417692939714570)
#     await channel.send(member.mention + "님, Alvin 그룹에 오신것을 환영해요!\n먼저 <#848132162972418079>부터 읽도록 해요!", file=file)
#     await member.send(member.mention + "님, Alvin 그룹에 오신것을 환영해요!\n먼저 <#848132162972418079>부터 읽도록 해요!", file=file)

@tree.context_menu(name="알림 보내기", guild=discord.Object(id=848128376643911700))
async def DM(interaction: discord.Interaction, message:discord.Message):
    if interaction.user.guild_permissions.manage_messages:
        noticemodal = NoticeModal()
        noticemodal.user = message.author
        await interaction.response.send_modal(noticemodal)
    else:
        await interaction.response.send_message(":x: 당신은 관리자가 아닙니다!")

# Commands
@tree.command(name="명령어", description="명령어를 보여줍니다", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction):
    embed = discord.Embed(title="도움", description="명령어 목록을 봅니다",
                          timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                          color=0x00a2ff)

    embed.add_field(name="/명령어", value="명령어를 보여줍니다.", inline=False)
    embed.add_field(name="/게임링크", value="한국인이 만든 방탈출 Roblox 게임 링크를 보여줍니다.", inline=False)
    embed.add_field(name="/규칙", value="규칙을 봅니다.", inline=True)
    embed.add_field(name="/피드백", value="방탈출 게임 피드백을 보냅니다", inline=True)
    embed.add_field(name="/내정보", value="자신의 정보를 보여줍니다", inline=True)
    embed.add_field(name="/credit", value="크레딧을 보여줍니다", inline=True)
    embed.set_footer(text="Codder : alvinbank1#5412",
                     icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
    await interaction.response.send_message(view=SelectViewCommands(), embed=embed, ephemeral=True)


@tree.command(name="규칙", description="규칙을 봅니다.", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction):
    button1 = Button(label="규칙 보기", style=discord.ButtonStyle.primary, emoji="▶", url="https://docs.google.com/document/d/1tAcK39XXV6YXDFlcEynNkOSWDvM2nD_OyHi0d1Hvkmo/edit?usp=sharing")
    view = View()
    view.add_item(button1)
    await interaction.response.send_message(view=view,ephemeral=True)
    # channel = client.get_channel(848132162972418079)
    # await channel.send("@everyone",view=view)

# @tree.command(name="내정보", description="내 정보를 보여줍니다", guild=discord.Object(id=848128376643911700))
# async def self(interaction: discord.Interaction):
#     background = Editor("black.png")
#     profile_image = await load_image_async(str(interaction.user.avatar.url))
#
#     profile = Editor(profile_image).resize((150, 150)).circle_image()
#     poppins = Font.poppins(size=50, variant="bold")
#
#     poppins_small = Font.poppins(size=20, variant="light")
#
#     background.paste(profile, (325, 90))
#     background.ellipse((325, 90), 150, 150, outline="white", stroke_width=5)
#
#     background.text((400, 260), f"{interaction.user.name}", color="white", font=poppins, align="center")
#     background.text((400, 325), f"{interaction.user.display_name}", color="white", font=poppins_small, align="center")
#     background.text((400, 350), f"{interaction.user.name}#{interaction.user.discriminator}", color="white", font=poppins_small,align="center")
#     file = File(fp=background.image_bytes, filename="pic1.png")
#     await interaction.response.send_message(file=file, ephemeral=True)

@tree.command(name="게임링크", description="한국인이 만든 방탈출 Roblox 게임 링크를 보여줍니다.", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction):
    button1 = Button(label="게임 하기", style=discord.ButtonStyle.primary, emoji="▶", url="https://www.roblox.com/games/4963463689/unnamed")
    view = View()
    view.add_item(button1)
    await interaction.response.send_message(view=view, ephemeral=True)

@tree.command(name="피드백", description="한국인이 만든 방탈출 Roblox 게임에 대하여 피드백을 주세요!", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction):
    feedback_modal= FeedbackModal()
    feedback_modal.user = interaction.user
    await interaction.response.send_modal(feedback_modal)

@tree.command(name="인증-1", description="인증을 완료합니다.", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction):
    if interaction.channel.id == 960454707120312350:
        try:
            embed = discord.Embed(title="인증", description="아래에 있는 숫자를 <#960454707120312350>에 있는 버튼을 클릭하여 똑같이 입력해 주세요.",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x00a2ff)
            await interaction.user.send(embed=embed)
            global a
            a = ""
            for i in range(6):
                a += str(random.randint(0,9))
            name = "captchaimages/" + str(interaction.user.id) + ".png"
            ImageCaptcha().write(a, name)
            await interaction.user.send(file=discord.File(name))
            channel = client.get_channel(873088054825463828)
            embed = discord.Embed(title="인증 로그", description=interaction.user.mention + "님이 인증코드를 생성하였습니다",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x002aff)
            embed.add_field(name="생성 유저", value=interaction.user.mention, inline=True)
            embed.add_field(name="생성한 코드", value=a, inline=True)
            await channel.send(embed=embed)
        except:
            embed = discord.Embed(title="인증", description="DM을 활성화 해주세요",timestamp=datetime.datetime.now(pytz.timezone('UTC')),color=0xff0000)
            embed.add_field(name="활성화 방법", value="https://discord.com/channels/848128376643911700/848128451890380821/963361216410046507", inline=False)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title="인증", description="인증코드는 DM을 확인해주세요.",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x00a2ff)
            button1 = Button(label="인증 코드 입력", style=discord.ButtonStyle.success, emoji="🔑")

            async def button_callback(interaction):
                verify_modal = VerifyModal()
                verify_modal.user = interaction.user
                await interaction.response.send_modal(verify_modal)

            button1.callback = button_callback
            view = View()
            view.add_item(button1)
            await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    else:
        await interaction.response.send_message("<#960454707120312350> 에서 이 명령어를 실행해 주세요!", ephemeral=True)


@tree.command(name="공지", description="공지를 작성합니다. (스테프만 가능)", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, important: bool):
    await interaction.channel.purge(limit=1)
    i = (interaction.user.guild_permissions.manage_messages)
    if i is True:
        announcmentmodal = AnnouncmentModal()
        announcmentmodal.interaction = interaction
        announcmentmodal.important = important
        await interaction.response.send_modal(announcmentmodal)

    if i is False:
        await interaction.response.send_message("{}, 당신은 관리자가 아닙니다".format(interaction.user.mention))


@tree.command(name="밴", description="유저를 밴 합니다.", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, user: discord.Member, reason: str):
    if interaction.user.guild_permissions.manage_messages:
        embed = discord.Embed(title="당신은 Alvin 그룹 서버에서 영구적으로 밴 당했습니다!",
                              description="밴 반성/항소 : https://forms.gle/Ko9vMgLesJg4u4A38",
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                              color=0xff0000)
        embed.add_field(name="밴 담당자", value=interaction.user.mention, inline=True)
        embed.add_field(name="사유", value=reason, inline=True)
        await user.send(embed=embed)
        try:
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

@tree.command(name="언밴", description="유저의 밴을 풉니다.", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, user: discord.Member, reason: str):
    if interaction.user.guild_permissions.manage_messages:
        try:
            await interaction.guild.unban(user=user,reason=reason)
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


@tree.command(name="킥", description="유저를 킥합니다", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, user: discord.Member, reason: str):
    if interaction.user.guild_permissions.manage_messages:
        embed = discord.Embed(title="당신은 Alvin 그룹 서버에서 킥 당했습니다!",
                              description="억울하다면 서버에 다시 접속해 주세요.",
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                              color=0xff0000)
        embed.add_field(name="킥 담당자", value=interaction.user.mention, inline=True)
        embed.add_field(name="사유", value=reason, inline=True)
        await user.send(embed=embed)
        try:
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

@tree.command(name="경고", description="유저를 경고 합니다", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, user:discord.Member, reason:str):
    if interaction.user.guild_permissions.manage_messages:
        author = user
        file = openpyxl.load_workbook("warning.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(user.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("warning.xlsx")
                if sheet["B" + str(i)].value > 2:
                    try:
                        embed = discord.Embed(title="당신은 Alvin 그룹 서버에서 영구적으로 밴 당했습니다!",
                                              description="밴 반성/항소 : https://forms.gle/Ko9vMgLesJg4u4A38",
                                              timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                              color=0xff0000)
                        embed.add_field(name="밴 담당자", value="<@960096117842923553> (자동 밴)", inline=True)
                        embed.add_field(name="사유", value="경고 총 누적 3회", inline=True)
                        await author.send(embed=embed)
                    except:
                        try:
                            await user.ban(reason="경고 총 누적 3회")
                        except:
                            await interaction.response.send_message(user.mention + "님은 관리자 입니다!")
                        else:
                            await interaction.response.send_message("경고 3회 누적으로, " + user.mention + "님이 영구 밴당하셨습니다.")
                            channel = client.get_channel(1007522175122669658)
                            embed = discord.Embed(title=user.name + "님이 서버에서 영구적으로 밴당하셨습니다.",
                                                  description=user.mention,
                                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                                  color=0x00ff00)
                            embed.add_field(name="밴 담당자", value="<@960096117842923553> (자동 밴)", inline=True)
                            embed.add_field(name="사유", value="경고 총 누적 3회", inline=True)
                            await channel.send(embed=embed)
                    else:
                        try:
                            await user.ban(reason="경고 총 누적 3회")
                        except:
                            await interaction.response.send_message(user.mention + "님은 관리자 입니다!")
                        else:
                            await interaction.response.send_message(
                                "경고 3회 누적으로," + user.name +"님이 영구 밴당하셨습니다.")
                            channel = client.get_channel(1007522175122669658)
                            embed = discord.Embed(title=user.name + "님이 서버에서 영구적으로 밴당하셨습니다.",
                                                  description=user.mention,
                                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                                  color=0x00ff00)
                            embed.add_field(name="밴 담당자", value="<@960096117842923553> (자동 밴)", inline=True)
                            embed.add_field(name="사유", value="경고 총 누적 3회", inline=True)
                            await channel.send(embed=embed)
                else:
                    await interaction.response.send_message(user.mention + "님이 " + interaction.user.mention + " 님에게 경고를 1개 받았습니다.")
                    embed = discord.Embed(title="당신은 Alvin 그룹 서버에서 경고를 받으셨습니다.",
                                          description="현재 경고: " + str(sheet["B" + str(i)].value),
                                          timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                          color=0xff0000)
                    embed.add_field(name="경고 담당자", value=interaction.user.mention, inline=True)
                    embed.add_field(name="사유", value=reason, inline=True)
                    await author.send(embed=embed)
                    channel = client.get_channel(1007522175122669658)
                    embed = discord.Embed(title=user.name + "님이 경고를 1개 받았습니다.",
                                          description=user.mention,
                                          timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.add_field(name="사유", value=reason, inline=True)
                    embed.add_field(name="현재 경고", value=str(sheet["B" + str(i)].value), inline=True)
                    await channel.send(embed=embed)
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(user.id)
                sheet["B" + str(i)].value = 1
                file.save("warning.xlsx")
                await interaction.response.send_message(user.mention + "님이 " + interaction.user.mention + "님에게 경고를 1개 받았습니다.")
                embed = discord.Embed(title="당신은 Alvin 그룹 서버에서 경고를 받으셨습니다.",
                                      description="현재 경고: " + str(sheet["B" + str(i)].value),
                                      timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                      color=0xff0000)
                embed.add_field(name="경고 담당자", value=interaction.user.mention, inline=True)
                embed.add_field(name="사유", value=reason, inline=True)
                embed.add_field(name="현재 경고", value=str(sheet["B" + str(i)].value), inline=True)
                await author.send(embed=embed)
                channel = client.get_channel(1007522175122669658)
                embed = discord.Embed(title=user.name + "님이 경고를 1개 받았습니다.",
                                      description=user.mention,
                                      timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.add_field(name="사유", value=reason, inline=True)
                await channel.send(embed=embed)
                break
            i += 1
    else:
        await interaction.response.send_message(":x: 당신은 관리자가 아닙니다!")

@tree.command(name="잠구기", description="채널을 잠급니다.", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, reason: str):
    if interaction.user.guild_permissions.manage_messages:

        await interaction.channel.set_permissions(discord.utils.get(interaction.guild.roles, name='맴버'), send_messages=False, view_channel=True)
        embed = discord.Embed(title="채널 잠김",
                              description=":lock: " + reason,
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(":x: 당신은 관리자가 아닙니다!")

@tree.command(name="잠금해제", description="채널을 잠금을 해제합니다.", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction):
    if interaction.user.guild_permissions.manage_messages:
        await interaction.channel.set_permissions(discord.utils.get(interaction.guild.roles, name='맴버'), send_messages=True, view_channel=True)
        embed = discord.Embed(title="채널 잠금 해제됨",
                              description=":unlock: 채널 잠금이 해제되었습니다",
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(":x: 당신은 관리자가 아닙니다!")

@tree.command(name="알림", description="유저에게 중요 알림을 보냅니다.", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, user: discord.Member):
    if interaction.user.guild_permissions.manage_messages:
        noticemodal = NoticeModal()
        noticemodal.user = user
        await interaction.response.send_modal(noticemodal)
    else:
        await interaction.response.send_message(":x: 당신은 관리자가 아닙니다!")

@tree.command(name="셧다운", description="봇을 끕니다 (셧다운)", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction):
    if interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("봇을 끄는중 입니다.")
        await client.get_channel(960443903251714068).send("봇을 셧다운(리붓) 합니다")
        print("셧다운중...")
        await client.get_channel(872396858729832518).edit(topic="다음 숫자: 0 (봇이 꺼져있습니다)")
        await client.get_channel(960443903251714068).send("셧다운 완료 ✅")
        await client.close()
    else:
        await interaction.response.send_message(":x: 당신은 소유자가 아닙니다!")

@tree.command(name="developertestcommand", description="개발자 테스트 커맨드 입니다.", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, string: str, button: bool):
    if interaction.user.guild_permissions.administrator:
        if button:
            button1 = Button(label="TestButton1", style=discord.ButtonStyle.green, emoji="🎈")
            async def button_callback(interaction):
                await interaction.response.send_message("test")

            button1.callback = button_callback
            view = View()
            view.add_item(button1)
            await interaction.response.send_message(string, ephemeral=True, view=view)
        else:
            await interaction.response.send_message(string, ephemeral=True)
    else:
        await interaction.response.send_message("오류! 당신은 소유자가 아닙니다!")

@tree.command(name="스테프신청", description="스테프 신청 인증을 합니다", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction):
    channel = client.get_channel(960848181049049158)
    await channel.send(interaction.user.mention + " 스테프 신청")
    await interaction.response.send_message("인증이 완료되었습니다.✅")

@tree.command(name="credit", description="크레딧을 보여줍니다", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction):
    embed = discord.Embed(title="Credit",
                          description="봇 크레딧",
                          timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                          color=0x00ff00)
    embed.add_field(name="프로그래밍 언어 / 모듈", value="Python / Discord.py", inline=True)
    embed.add_field(name="봇 총 제작자", value="<@929382103555141712>", inline=True)
    embed.add_field(name="일부 코드", value="https://www.youtube.com/@b_code", inline=True)
    embed.add_field(name="소스코드", value="https://github.com/alvinbank1/roomescapebot/blob/main/new.py", inline=True)
    await interaction.response.send_message(embed=embed, ephemeral=True)

@tree.command(name="문의답변", description="문의에 답변합니다", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, user:discord.Member, content:str):
    if interaction.channel.id == 961195825306951700:
        msg = content
        try:
            embed = discord.Embed(title="문의 답변",
                                  description="문의의 답변이 도착하였습니다!",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x00ff00)
            embed.add_field(name="답변", value=content, inline=True)
            embed.add_field(name="답변자", value=interaction.user.mention, inline=True)
            await DMChannel.send(user, embed=embed)
        except:
            await interaction.response.send_message("메세지 전송에 실패하였습니다.", ephemeral=True)
        else:
            embed = discord.Embed(title="문의 답변",
                                  description="문의 답변 로그입니다",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x00ff00)
            embed.add_field(name="답변", value=content, inline=True)
            embed.add_field(name="답변자", value=interaction.user.mention, inline=True)
            await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("올바르지 않은 채널입니다.")

@tree.command(name="문의종료", description="문의를 종료합니다", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, user:discord.Member, reason:str):
    if interaction.channel.id == 961195825306951700:
        embed = discord.Embed(title="문의 종료",
                              description="문의가 종료되었습니다",
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                              color=0xff0000)
        embed.add_field(name="사유", value=reason, inline=True)
        embed.add_field(name="종료자", value=interaction.user.mention, inline=True)
        try:
            await DMChannel.send(user, embed=embed)
        except:
            await interaction.response.send_message("메세지 전송에 실패하였습니다.", ephemeral=True)
        else:
            embed = discord.Embed(title="문의 종료",
                                  description="문의가 종료되었습니다",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0xff0000)
            embed.add_field(name="사유", value=reason, inline=True)
            embed.add_field(name="종료자", value=interaction.user.mention, inline=True)
            await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("올바르지 않은 채널입니다.")

@tree.command(name="chat-gpt", description="챗 GPT 명령어입니다!", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, message: str):
    await interaction.response.send_message("서버에서 데이터를 가져오는 중 입니다.\n잠시만 기다려 주세요!",ephemeral=False)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user","content":message}
        ]
    )
    print(response["choices"][0].message["content"])
    embed = discord.Embed(title="Chat GPT 대답", description="Q. " + message,
                          timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x93C54B)
    embed.add_field(name="답변", value=response["choices"][0].message["content"], inline=True)
    await interaction.edit_original_response(embed=embed, content="")
    #await id.send(embed=embed)

@tree.command(name="지원결과", description="지원서 결과를 보냅니다.", guild=discord.Object(id=848128376643911700))
async def self(interaction: discord.Interaction, user:discord.Member,name: str,result: bool, feedback: str):
    await interaction.response.send_message("결과 전송중...", ephemeral=True)
    embed = discord.Embed(title=name + " 지원 결과 안내", description="지원하신 " + name + "의 결과를 안내드립니다.",
                          timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x93C54B)
    if result == True:
        embed.add_field(name="결과", value="지원 결과는 합격입니다.")
        embed.add_field(name="피드백", value=feedback)
        embed.set_footer(text="지원해 주셔서 감사합니다. 곧 DM이 올 것이니, DM을 켜두시기 바랍니다.",
                         icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
    else:
        embed.add_field(name="결과", value="지원 결과는 불합격입니다.")
        embed.add_field(name="피드백", value=feedback)
        embed.set_footer(text="지원해 주셔서 감사합니다. 다음에 다시 지원해주시기 바랍니다.",
                         icon_url="https://cdn.discordapp.com/avatars/855015531584290877/04ba95df55ff875d171c0fbc82e62aaa.png?size=256")
    await user.send(embed=embed)
    await interaction.edit_original_response(content="결과 전송이 완료되었습니다!")

@client.event
async def on_message(message):
    global count
    print(message.author.bot)
    if message.author.bot == False:
        if message.channel.id == 872396858729832518:
            if message.content == str(count):
                await message.channel.purge(limit=1)
                await message.channel.send(message.author.mention + ": " + str(count))
                await client.get_channel(872396858729832518).edit(topic="다음 숫자: " + str(count+1))
                count += 1
            else:
                await message.channel.purge(limit=1)
    if message.author != client.user:
        print(message.author.name+": "+message.content)
        log = client.get_channel(1078528911656357968)
        embed = discord.Embed(title="메세지 전송 로그",
                              description=message.author.mention,
                              timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                              color=0x00f00)
        embed.add_field(name="메세지", value=message.content, inline=True)
        embed.add_field(name="메세지 링크", value="[메세지로 이동]("+message.jump_url+")", inline=True)
        await log.send(embed=embed)
    empty_array = []
    modmail_channel = client.get_channel(961195825306951700)
    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            embed = discord.Embed(title="문의",
                                  description="문의가 도착했습니다!",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x0055ff)
            if message.content != "":
                embed.add_field(name="문의 내용", value=message.content, inline=True)
            embed1 = discord.Embed(title="문의",
                                  description="문의하신 내용입니다",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x0055ff)
            if message.content != "":
                embed1.add_field(name="문의 내용", value=message.content, inline=True)
            for file in files:
                embed.add_field(name="파일 링크", value=file.url, inline=True)
                embed1.add_field(name="파일 링크", value=file.url, inline=True)
            await modmail_channel.send("@here", embed=embed)
            await message.channel.send(embed=embed1)
        else:
            embed = discord.Embed(title="문의",
                                  description="문의가 도착했습니다!",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x0055ff)
            embed.add_field(name="문의 내용", value=message.content, inline=True)
            embed.add_field(name="문의 맴버", value=message.author.mention, inline=True)
            try:
                await modmail_channel.send("@here", embed=embed)
            except:
                embed = discord.Embed(title="오류 발생",
                                      description="스크립트 오류가 발생하였습니다.",
                                      timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                      color=0xff0000)
                embed.add_field(name="오류코드", value="0458 Failed to send", inline=True)
                await modmail_channel.send(embed=embed)
            embed = discord.Embed(title="문의",
                                  description="문의하신 내용입니다",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x0055ff)
            embed.add_field(name="문의 내용", value=message.content, inline=True)
            try:
                await message.channel.send(embed=embed)
            except:
                embed = discord.Embed(title="오류 발생",
                                      description="스크립트 오류가 발생하였습니다.",
                                      timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                      color=0xff0000)
                embed.add_field(name="오류코드", value="0473 Failed to send", inline=True)
                await message.channel.send(embed=embed)

    elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            embed = discord.Embed(title="문의",
                                  description="문의가 도착했습니다!",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x0055ff)
            embed.add_field(name="문의 내용", value=message.content, inline=True)
            for file in files:
                embed.add_field(name="파일 링크", value=file.url, inline=True)
            await member_object.send("@here", embed=embed)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            embed = discord.Embed(title="문의",
                                  description="문의하신 내용입니다",
                                  timestamp=datetime.datetime.now(pytz.timezone('UTC')),
                                  color=0x0055ff)
            embed.add_field(name="문의 내용", value=mod_message, inline=True)
            await member_object.send(embed=embed)


client.run('YOUR_TOKEN_HERE')
