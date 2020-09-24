import telebot
import config
from telebot import types 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	markup.row('О нас', 'Выбор города')
	markup.row('Связаться с нами')

	markup2 = types.InlineKeyboardMarkup(row_width=2)
	item = types.InlineKeyboardButton('Омск', callback_data = 'Омск')
	item2 = types.InlineKeyboardButton('Москва', callback_data = 'Москва')
	item3 = types.InlineKeyboardButton('Казань', callback_data = 'Казань')
	item4 = types.InlineKeyboardButton('Иркутск', callback_data = 'Иркутск')
	markup2.add(item, item2, item3, item4)

	bot.send_message(message.chat.id, "Здравствуйте, {0.first_name} {1.last_name}!\nЯ - бот <b>{2.first_name}</b>\nМы - компания Be Educated.  Официальный представитель государственных и частных Российских и Европейских ВУЗ-ов в средней Азиию".format(message.from_user, message.from_user, bot.get_me()), 
		parse_mode='html')
	bot.send_message(message.chat.id, 'Для удобства есть меню, вы можете его открыть нажав на соответстувующю кнопку')
	bot.send_message(message.chat.id, "Выберите город для поступления на учебу", reply_markup=markup2)


@bot.message_handler(content_types=['text'])
def lalala(message):
	markup2 = types.InlineKeyboardMarkup(row_width=2)
	item = types.InlineKeyboardButton('Омск', callback_data = 'Омск')
	item2 = types.InlineKeyboardButton('Москва', callback_data = 'Москва')
	item3 = types.InlineKeyboardButton('Казань', callback_data = 'Казань')
	item4 = types.InlineKeyboardButton('Иркутск', callback_data = 'Иркутск')
	markup2.add(item, item2, item3, item4)

	if message.text == 'Выбор города':
		bot.send_message(message.chat.id, "Выберите город для поступления на учебу", reply_markup=markup2)
	elif message.text == 'О нас':
		bot.send_message(message.chat.id, "Мы - компания Be Educated.  Официальный представитель государственных и частных Российских и Европейских ВУЗ-ов в средней Азиию6".format(message.from_user, message.from_user, bot.get_me()), 
		parse_mode='html')
	elif message.text == 'Связаться с нами':
		bot.send_message(message.chat.id, 'Напишите нашему оператору @janbo_a')
	else:
		bot.send_message(message.chat.id, 'Я вас не понимаю')
	#bot.send_message(message.chat.id, '')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

	markup2 = types.InlineKeyboardMarkup(row_width=2)
	markup3 = types.InlineKeyboardMarkup(row_width=2)
	item = types.InlineKeyboardButton('Омск', callback_data = 'Омск')
	item2 = types.InlineKeyboardButton('Москва', callback_data = 'Москва')
	item3 = types.InlineKeyboardButton('Казань', callback_data = 'Казань')
	item4 = types.InlineKeyboardButton('Иркутск', callback_data = 'Иркутск')

	it1 = types.InlineKeyboardButton('МосАП', callback_data = 'МосАП')
	it2 = types.InlineKeyboardButton('Реавиз', callback_data = 'Реавиз')
	it3 = types.InlineKeyboardButton('ММА', callback_data = 'ММА')


	markup2.add(item, item2, item3, item4)
	markup3.add(it1, it2, it3)
	
	try:
		if call.message:
			if call.data == 'Омск':
				bot.send_message(call.message.chat.id, 'Омская гуманитарная академия\nВысококвалифицированный научно-преподавательский состав академии ведет качественную подготовку бакалавров и специалистов, в этом им помогает инфраструктура вуза, которая была значительно расширена за прошедшие годы')
				bot.send_document(call.message.chat.id, open('files/omga.jpg', 'rb'))
				bot.send_message(call.message.chat.id, 'Подождите минуту, мы отправляем вам файл со специальностями')
				omga = open('files/omgaO.pdf', 'rb')
				bot.send_document(call.message.chat.id, omga)
				omga.close()
			elif call.data == 'Москва':
				bot.send_message(call.message.chat.id, 'В Москве расположены три университета, пожалуйста, выберите одну:\n1.МосАП\n2.Реавиз\n3.ММА', reply_markup=markup3)
			elif call.data == 'МосАП':
				bot.send_message(call.message.chat.id, 'Московская академия предпринимательства\nФундаментальное академическое образование, максимум практики и погружение в профессию с самого начала обучения')
				bot.send_document(call.message.chat.id, open('files/mosap.png', 'rb'))
				bot.send_message(call.message.chat.id, 'Подождите минуту, мы отправляем вам файл со специальностями')
				omga = open('files/MosapO.pdf', 'rb')
				bot.send_document(call.message.chat.id, omga)
				omga.close()
				#bot.send_message(call.message.chat.id, 'Оставьте свой номер и мы с вами свяжемся')
			elif call.data == 'Реавиз':
				bot.send_message(call.message.chat.id, 'Московский медицинский институт\nУлучшение здоровья людей через обучение студентов и врачей последним достижениям медицинской науки и практики.')
				bot.send_document(call.message.chat.id, open('files/reavz.png', 'rb'))
				bot.send_message(call.message.chat.id, 'Подождите минуту, мы отправляем вам файл со специальностями')
				omga = open('files/reavizO.pdf', 'rb')
				bot.send_document(call.message.chat.id, omga)
				omga.close()
				#bot.send_message(message.chat.id, 'Оставьте свой номер и мы с вами свяжемся')
			elif call.data == 'ММА':
				bot.send_message(call.message.chat.id, 'Московская международная академия – молодой, но многообещающий вуз, который был образован как лингвистический, но уже больше десятилетия работает как универсальное высшее учебное заведение.')
				bot.send_document(call.message.chat.id, open('files/mma.png', 'rb'))
				bot.send_message(call.message.chat.id, 'Подождите минуту, мы отправляем вам файл со специальностями')
				omga = open('files/mmaO.pdf', 'rb')
				bot.send_document(call.message.chat.id, omga)
				omga.close()
				#bot.send_message(call.message.chat.id, 'Оставьте свой номер и мы с вами свяжемся')
			elif call.data == 'Казань':
				bot.send_message(call.message.chat.id, 'Казанский национальный исследовательский университет\nИнженерный химико-технологический институт')
				bot.send_document(call.message.chat.id, open('files/kaznitu.png', 'rb'))
				bot.send_message(call.message.chat.id, 'Подождите минуту, мы отправляем вам файл со специальностями')
				omga = open('files/kaznituO.pdf', 'rb')
				bot.send_document(call.message.chat.id, omga)
				#bot.send_message(call.message.chat.id, 'Оставьте свой номер и мы с вами свяжемся')
				omga.close()
			elif call.data == 'Иркутск':
				bot.send_message(call.message.chat.id, 'Иркутский национальный исследовательский университет')
				bot.send_document(call.message.chat.id, open('files/irnitu.png', 'rb'))
				bot.send_message(call.message.chat.id, 'Подождите минуту, мы отправляем вам файл со специальностями')
				omga = open('files/irnituO.pdf', 'rb')
				bot.send_document(call.message.chat.id, omga)
				omga.close()
				#bot.send_message(call.message.chat.id, 'Оставьте свой номер и мы с вами свяжемся')
			else:
				bot.send_message(call.message.chat.id, 'Пожалуйста, выберите из списка')
	except Exception as e:
		print(repr(e))

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

bot.polling(none_stop=True)