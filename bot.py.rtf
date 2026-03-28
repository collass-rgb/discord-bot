{\rtf1\ansi\ansicpg950\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 CourierNewPSMT;\f1\froman\fcharset0 Times-Roman;\f2\fnil\fcharset136 PingFangTC-Regular;
}
{\colortbl;\red255\green255\blue255;\red202\green202\blue202;\red23\green22\blue34;\red22\green65\blue142;
\red0\green0\blue0;\red117\green117\blue117;}
{\*\expandedcolortbl;;\cssrgb\c83137\c83137\c83137;\cssrgb\c11765\c11765\c18039;\cssrgb\c10196\c33725\c62745;
\cssrgb\c0\c0\c0;\cssrgb\c53333\c53333\c53333;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrt\brdrnil \trbrdrl\brdrnil \trbrdrt\brdrnil \trbrdrr\brdrnil 
\clvertalt \clcbpat3 \clwWidth11403\clftsWidth3 \clbrdrt\brdrs\brdrw10\brdrcf6 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw10\brdrcf6 \clbrdrr\brdrnil \clpadt186 \clpadl320 \clpadb186 \clpadr266 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import os, json, urllib.request, urllib.parse
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 import discord
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 from anthropic import Anthropic
\f1 \cf0 \strokec5 \
\

\f0 \cf2 \strokec2 DISCORD_TOKEN\'a0 = os.environ['DISCORD_TOKEN']
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 ANTHROPIC_KEY\'a0 = os.environ['ANTHROPIC_API_KEY']
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 GAS_URL\'a0 \'a0 \'a0 \'a0 = os.environ['GAS_WEBAPP_URL']
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 CHANNEL_ID \'a0 \'a0 = int(os.environ.get('BOT_CHANNEL_ID', '0'))
\f1 \cf0 \strokec5 \
\

\f0 \cf2 \strokec2 claude\'a0 = Anthropic(api_key=ANTHROPIC_KEY)
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 intents = discord.Intents.default()
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 intents.message_content = True
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 client\'a0 = discord.Client(intents=intents)
\f1 \cf0 \strokec5 \
\

\f0 \cf2 \strokec2 def call_gas(action, query):
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0params = urllib.parse.urlencode(\{'action': action, 'query': query\})
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0try:
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0with urllib.request.urlopen(f'\{GAS_URL\}?\{params\}', timeout=15) as r:
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return json.loads(r.read().decode())
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0except Exception as e:
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return \{'error': str(e)\}
\f1 \cf0 \strokec5 \
\

\f0 \cf2 \strokec2 def ask_claude(question, data):
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0msg = claude.messages.create(
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0model='claude-sonnet-4-6', max_tokens=600,
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0system='
\f2 \'a7\'41\'ac\'4f\'b3\'66\'aa\'70\'ac\'64\'b8\'df\'a7\'55\'b2\'7a\'a1\'41\'a5\'ce\'c1\'63\'c5\'e9\'a4\'a4\'a4\'e5\'c2\'b2\'bc\'e4\'a6\'5e\'b5\'aa\'a1\'41\'a5\'69\'a5\'ce
\f0  Discord Markdown 
\f2 \'ae\'e6\'a6\'a1\'a1\'43
\f0 ',
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0messages=[\{'role':'user','content': f'
\f2 \'b8\'ea\'ae\'c6\'a1\'47
\f0 \{json.dumps(data,ensure_ascii=False)\}\\n
\f2 \'b0\'dd\'c3\'44\'a1\'47
\f0 \{question\}'\}]
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0)
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0return msg.content[0].text
\f1 \cf0 \strokec5 \
\

\f0 \cf2 \strokec2 @client.event
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 async def on_ready():
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0print(f'Bot 
\f2 \'a4\'57\'bd\'75\'a1\'47
\f0 \{client.user\}')
\f1 \cf0 \strokec5 \
\

\f0 \cf2 \strokec2 @client.event
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 async def on_message(message):
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0if message.author.bot: return
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0if CHANNEL_ID and message.channel.id != CHANNEL_ID: return
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0if client.user not in message.mentions: return
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0question = message.content.replace(f'<@\{client.user.id\}>', '').strip()
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0if not question:
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0await message.reply('
\f2 \'bd\'d0\'b0\'dd\'a7\'da\'b0\'dd\'c3\'44\'a1\'41\'a8\'d2\'a6\'70\'a1\'47\'ac\'64
\f0  A802-B 
\f2 \'a6\'a8\'a5\'bb
\f0 ')
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0import re
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0sku = (re.search(r'\\b([A-Za-z]\\d\{3,4\}(?:-[\\w]+)?)\\b', question) or [None, question])[1].upper()
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0action = 'recent_purchases' if any(k in question for k in ['
\f2 \'b6\'69\'b3\'66
\f0 ','
\f2 \'b1\'c4\'c1\'ca
\f0 ','
\f2 \'b6\'52\'a4\'46
\f0 ']) else 'search_product'
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0async with message.channel.typing():
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0data = call_gas(action, sku)
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0answer = ask_claude(question, data)
\f1 \cf0 \strokec5 \

\f0 \cf2 \strokec2 \'a0\'a0\'a0\'a0await message.reply(answer)
\f1 \cf0 \strokec5 \
\

\f0 \cf2 \strokec2 client.run(DISCORD_TOKEN)
\f1 \cf0 \strokec5 \cell \lastrow\row
}