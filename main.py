from telethon import TelegramClient, events, Button
from telethon.tl.functions.channels import GetParticipantsRequest, EditBannedRequest
from telethon.tl.types import ChatBannedRights, ChannelParticipantsSearch
import asyncio

api_id = 29267104
api_hash = 'a5fdbcda645214f1dc597736ab477a50'
bot_token = '7048898243:AAHv65uYHcls_OguCdDyoPg7BoYSm33eROU'

banned_rights = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True
)

client = TelegramClient('banbot', api_id, api_hash)


@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    name = event.sender.first_name
    msg = f"""<b>⌜──────────────⌝
  ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ
⌞──────────────⌟</b>

✦ » ʜᴇʏ <b>{name}</b>

<b>─────────────────────</b>

✦ » ɪ'ᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇ ʙᴀɴᴀʟʟ ʙᴏᴛ .

✦ » ʙᴀɴ ᴏʀ ᴅᴇsᴛʀᴏʏ ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs 
ғʀᴏᴍ ᴀ ɢʀᴏᴜᴘ ᴡɪᴛʜɪɴ ᴀ ꜰᴇᴡ sᴇᴄᴏɴᴅs .

✦ » ᴄʜᴇᴄᴋ ᴍʏ ᴀʙɪʟɪᴛʏ, ɢɪᴠᴇ ᴍᴇ ᴏɴʟʏ ʙᴀɴ 
ᴘᴏᴡᴇʀ ᴀɴᴅ ᴛʏᴘᴇ <code>/banall</code> ᴛᴏ sᴇᴇ ᴍᴀɢɪᴄ ɪɴ 
ɢʀᴏᴜᴘ .

<b>─────────────────────</b>

◈ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➯ <a href="https://t.me/SimpleBotsTech">sɪᴍᴘʟᴇ ʙᴏᴛs ᴛᴇᴄʜ</a>"""

    buttons = [
        [Button.url("✚ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚", "https://t.me/Ban_all_fastbot?startgroup=true")],
        [
            Button.url("『 sᴜᴘᴘᴏʀᴛ 』", "https://t.me/SimpleBotsTechSupport"),
            Button.url("『 ᴜᴘᴅᴀᴛᴇs 』", "https://t.me/SimpleBotsTech")
        ],
        [
            Button.url("『 ᴏᴡɴᴇʀ 』", "https://t.me/unbrokenkid"),
            Button.url("『 ᴍᴜsɪᴄ ʙᴏᴛ 』", "http://t.me/SIMPLE_MUSIC_PROBOT")
        ]
    ]

    await event.respond(msg, buttons=buttons, parse_mode='html')


@client.on(events.NewMessage(pattern='/banall'))
async def ban_all_handler(event):
    if not (event.is_group or event.is_channel):
        return

    try:
        group = await event.get_input_chat()
        participants = await client(GetParticipantsRequest(
            channel=group,
            filter=ChannelParticipantsSearch(''),
            offset=0,
            limit=10000,
            hash=0
        ))

        admins = await client.get_participants(group, filter=ChannelParticipantsSearch(''))
        admin_ids = [a.id for a in admins if hasattr(a, 'participant') and getattr(a.participant, 'admin_rights', None)]

        for user in participants.users:
            if user.bot or user.id in admin_ids or user.id == event.sender_id:
                continue
            try:
                await client(EditBannedRequest(group, user.id, banned_rights))
            except:
                continue
    except Exception as e:
        print("Error banning members:", e)


async def main():
    await client.start(bot_token=bot_token)
    print("Bot is up.")
    await client.run_until_disconnected()

# This is the main entry point for Leapcell to run
if __name__ == "__main__":
    asyncio.run(main())
    
