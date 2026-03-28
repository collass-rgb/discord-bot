import os, json, urllib.request, urllib.parse
import discord
from anthropic import Anthropic

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
ANTHROPIC_KEY = os.environ['ANTHROPIC_API_KEY']
GAS_URL = os.environ['GAS_WEBAPP_URL']
CHANNEL_ID = int(os.environ.get('BOT_CHANNEL_ID', '0'))

claude = Anthropic(api_key=ANTHROPIC_KEY)
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def call_gas(action, query):
    params = urllib.parse.urlencode({'action': action, 'query': query})
    try:
        with urllib.request.urlopen(f'{GAS_URL}?{params}', timeout=15) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {'error': str(e)}

def ask_claude(question, data):
    msg = claude.messages.create(
        model='claude-sonnet-4-6', max_tokens=600,
        system='你是貨況查詢助理，用繁體中文簡潔回答，可用 Discord Markdown 格式。',
        messages=[{'role':'user','content': f'資料：{json.dumps(data,ensure_ascii=False)}\n問題：{question}'}]
    )
    return msg.content[0].text

@client.event
async def on_ready():
    print(f'Bot 上線：{client.user}')

@client.event
async def on_message(message):
    if message.author.bot: return
    if CHANNEL_ID and message.channel.id != CHANNEL_ID: return
    if client.user not in message.mentions: return
    question = message.content.replace(f'<@{client.user.id}>', '').strip()
    if not question:
        await message.reply('請問我問題，例如：查 A802-B 成本')
        return
    import re
    sku_match = re.search(r'\b([A-Za-z]\d{3,4}(?:-[\w]+)?)\b', question)
    sku = sku_match.group(1).upper() if sku_match else question
    action = 'recent_purchases' if any(k in question for k in ['進貨','採購','買了']) else 'search_product'
    async with message.channel.typing():
        data = call_gas(action, sku)
        answer = ask_claude(question, data)
    await message.reply(answer)

client.run(DISCORD_TOKEN)
