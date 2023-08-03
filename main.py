import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

arr = [
        ["","","","",""],
        ["","","","",""]
        ]#목록 리스트입니다.

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.group(invoke_without_command=True)
async def 목록(ctx):#저정되어있는 목록을 불러옵니다.
    try:#arrResult 변수를 선언한 후 2차원 목록 리스트에서 원소를 하나씩 배정합니다.
        arrResult = "주간 목록 \n"
        i = 1
        while i <= 5:
            arrResult = arrResult + arr[0][i-1] + "\n"
            i = i + 1

        arrResult =  arrResult + "일간 목록 \n"
        i = i - 5
        while i <= 5:
            arrResult = arrResult + arr[1][i-1] + "\n"
            i = i + 1

        await ctx.send(arrResult)
    except:
        await ctx.send("제대로 입력해주세요")

@목록.command()
async def 주간추가(ctx, arg1, arg2, arg3):#ex) 목록 주간추가 5 3 밥먹기 5월 3주차 밥먹기
    try:
        i = 1
        while i <= 5:
            if arr[0][i-1] == "":
                arr[0][i-1] = f"{arg1}월 {arg2}주차 {arg3}"
                i = i + 10
            else:
                i = i + 1
    except:
        await ctx.send("제대로 입력해주세요")

@목록.command()
async def 일간추가(ctx, arg1, arg2, arg3):#ex) 목록 일간추가 5 3 밥먹기 5월 3일 밥먹기
    try:
        i = 1
        while i <= 5:
            if arr[1][i-1] == "":
                arr[1][i-1] = f"{arg1}월 {arg2}일 {arg3}"
                i = i + 10
            else:
                i = i + 1
    except:
        await ctx.send("제대로 입력해주세요")

bot.run('MTEwODI2MjEzMTc0MjI4NTg4Nw.GNWoXj.yc0PJgr744NA-dLcmqLH_zZ8yaS2XULB7FsPXs')

#메모 명령어 만들기
#수정 삭제 명령어 만들기
#명령어 권한 지정
#띄어쓰기 인식 개선