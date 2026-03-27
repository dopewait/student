from vkbottle.bot import Bot, Message
TOKEN="vk1.a.mQ_UJQHYAGdLTHErr0A72_-1WzHRdM_ZN8niCZ9TvisSvIVkJ55o7PnXQ6gp4dxyo9vSV1YTQ8IDyc82DsD73nZ5PnDa2rpCKeOEkeFZDt76Z6lDSJxrjJPaI8hzfXR03LXQPfuM0f3B06IgCjDttMMSAoyozNnq6tb0NgghYrzgz51xanxQIYWH7Nw9hfDQJFi83QcE9l4Yd8h3cwUcig"

bot=Bot(TOKEN)
#команда /start
@bot.on.message(text="/start")
async def start_handler(message:Message):
    await message.answer("Привет я твой первый бот в вконтакте!")
#Ответ на любое сообщение "Привет"
@bot.on.messsage(text="Привет")
async def hi_handler(message:Message):
    user_id=message.from_id
    await message.answer(f"И тебе привет id пользователя {user_id}") 
#обработка остального текста
@bot.on.message()
async def my_message(message:Message):
    text=message.text
    if text:
        await message.answer(f"Ты написал {text}, молодец {user_id} и Гор!")
if name=="main":
    print("Бот запущен!")
    bot.run_forever()