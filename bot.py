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
        messages=[{'role': 'user', 'content': f'資料：{json.dumps(data, ensure_ascii=False)}\n問題：{question}'}]
    )
    return msg.content[0].text

def format_product(r):
    weight = r.get('重量', '')
    weight_str = f"{weight} kg" if weight != '' and weight != 0 else '未填'
    last_date = r.get('最近進貨日期', '') or '無記錄'
    last_qty = r.get('最近進貨數量', '')
    try:
        last_qty_str = f"{int(last_qty)} 件" if last_qty != '' and last_qty != '無記錄' else '無記錄'
    except:
        last_qty_str = '無記錄'
    return (
        f"📦 **{r.get('貨號', '')}**｜{r.get('商品名稱', '')}\n"
        f"💰 最新台幣成本：{r.get('最新台幣', '')}\n"
        f"📊 毛利率：{r.get('毛利率', '')}\n"
        f"🏷️ 定價：{r.get('定價', '')}\n"
        f"⚖️ 重量：{weight_str}\n"
        f"📅 最後進貨：{last_date}　數量：{last_qty_str}"
    )

def format_purchase(r):
    source = f"（{r.get('來源', '')}）" if r.get('來源') else ''
    return (
        f"📅 {r.get('日期', '')} {source}\n"
        f"💴 含稅：{r.get('含稅', '')}　💰 台幣：{r.get('台幣', '')}　📦 數量：{r.get('數量', '')}"
    )

@client.event
async def on_ready():
    print(f'Bot 上線：{client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if CHANNEL_ID and message.channel.id != CHANNEL_ID:
        return
    if client.user not in message.mentions:
        return

    question = message.content.replace(f'<@{client.user.id}>', '').strip()

    if not question:
        await message.reply(
            '**使用方式：**\n'
            '`查 貨號` — 查商品資訊\n'
            '`進貨 貨號` — 查進貨記錄\n'
            '`AI 問題` — 用 AI 回答複雜問題'
        )
        return

    import re

    # AI 模式
    if question.lower().startswith('ai '):
        q = question[3:].strip()
        sku_match = re.search(r'\b([A-Za-z]\d{3,4}(?:-[\w]+)?)\b', q)
        sku = sku_match.group(1).upper() if sku_match else q
        action = 'recent_purchases' if any(k in q for k in ['進貨', '採購', '買了']) else 'search_product'
        async with message.channel.typing():
            data = call_gas(action, sku)
            answer = ask_claude(q, data)
        await message.reply(answer)
        return

    # 制式模式：查進貨記錄
    if question.startswith('進貨 ') or question.startswith('進貨　'):
        sku = question[3:].strip().upper()
        async with message.channel.typing():
            data = call_gas('recent_purchases', sku)
        results = data.get('results', [])
        if not results:
            await message.reply(f'找不到「{sku}」的進貨記錄。')
            return
        lines = [f"**{sku} 最近進貨記錄**"]
        for r in results:
            lines.append(format_purchase(r))
        await message.reply('\n\n'.join(lines))
        return

    # 制式模式：查商品資訊
    sku = re.sub(r'^查\s*', '', question).strip().upper()
    async with message.channel.typing():
        data = call_gas('search_product', sku)
    results = data.get('results', [])
    if not results:
        await message.reply(f'找不到「{sku}」的商品資料。')
        return
    lines = []
    for r in results:
        lines.append(format_product(r))
    await message.reply('\n\n'.join(lines))

client.run(DISCORD_TOKEN)
