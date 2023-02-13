import nextcord
from nextcord.ext import commands

class ShareManger(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
    
    # 계획중: 업로드 채널 설정, 수동 업로드
    # 봇/앱 ===> 서버 ===> 앱

    

def setup(client: commands.Bot) -> None:
    client.add_cog(ShareManger(client))