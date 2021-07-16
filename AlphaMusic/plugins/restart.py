import logging
import pickle
from os import execl, path, remove
from sys import executable

from telethon.events import NewMessage

from .. import bot, OWNER_ID

logger = logging.getLogger(__name__)

if path.exists('restart.pickle'):
    with open('restart.pickle', 'rb') as status:
        chat, msg_id = pickle.load(status)
    bot.loop.run_until_complete(bot.edit_message(
        chat, msg_id, "Reiniciado con éxito!"))
    remove('restart.pickle')


@bot.on(NewMessage(pattern='/restart', from_users=OWNER_ID))
async def restart(event):
    restart_message = await event.reply("Reiniciando, espere!")
    with open('restart.pickle', 'wb') as status:
        pickle.dump([event.chat_id, restart_message.id], status)
    logger.info('Reiniciando AlphaMusic')
    execl(executable, executable, "-m", "AlphaMusic")
