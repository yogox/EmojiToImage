import os
import re
import discord

# BOTのアクセストークン
TOKEN = ''
# 画像ファイルを格納しているディレクトリのパス
FILE_DIR = "image/"
# 画像ファイルの拡張子
FILE_SUFFIX = ".png"
# オリジナルユーザー名の前につける文字
USER_PREFIX = ""
# オリジナルユーザー名の後につける文字
USER_SUFFIX = "さん から"


# クライアントを生成
client = discord.Client()

async def send_response(message, file_name, user_description):
    # 絵文字名と同名の画像ファイル名を作成
    image_path = FILE_DIR + file_name + FILE_SUFFIX

    # 画像ファイルが存在しない場合、戻る
    if not os.path.isfile(image_path):
        await message.channel.send(content=image_path + " is not found")
        return

    # 画像ファイルを取得
    image_file = discord.File(image_path)
    # メッセージ＋画像を送信
    await message.channel.send(content=user_description, file=image_file)

# 起動時のイベント
@client.event
async def on_ready():
    # 起動表示兼リビジョン確認
    print('rev1.11 start')

# メッセージ送信時のイベント
@client.event
async def on_message(message):
    # print(message.content)

    # 送信者がBOTの時は何もせずに終了
    if message.author.bot:
        return

    # 絵文字を投稿した場合、コンテンツは"<:絵文字名:任意数列>"となる。
    # 正規表現で先頭が<:__任意文字列:>で始まる文字列をマッチして絵文字名を判別

    # 絵文字英エイリアスが___で始まる場合、返信モード。
    emoji_id = re.match(r'<:___(.+):.+>', message.content)
    if emoji_id:
        file_name = emoji_id.group(1)

        # 返信モードの時はメッセージは設定しない
        user_description = None

        # BOTによるメッセージ送信
        await send_response(message, file_name, user_description)

        return

    # 絵文字英エイリアスが__で始まる場合、変換モード。
    emoji_id = re.match(r'<:__(.+):.+>', message.content)
    if emoji_id:
        file_name = emoji_id.group(1)

        # オリジナルユーザー名からメッセージ文字列を作成
        user_description = USER_PREFIX + message.author.name + USER_SUFFIX

        # BOTによるメッセージ送信
        await send_response(message, file_name, user_description)
        # オリジナルメッセージを削除
        await message.delete()

        return


# BOTの起動とDiscordサーバーへの接続
client.run(TOKEN)
