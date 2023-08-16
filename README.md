# luggageinfototelegram
A script getting the information on lost&amp;found luggage (tested with Air Serbia)

===
Have you ever faced the problem that the airplane took you to your destination but your luggage didn't make it?
The carrier's phone is not answering, the airport has not yet received the information, and the dedicated website is very slow?

I was once in such a situation, so this small script does all the checking rounting for me.

The script crawls to the search interface, gets the info on the credentials of your luggage. All of this done in telegram bot.


requirements:
dotenv (for getting secrets)
aiogram (this is what i usuallty use, but in this particular case it's a superfluous function)
selenium


The bot requires:
1) installing chrome webdriver for selenium
2) getting a telgram bot api token (https://help.zoho.com/portal/en/kb/desk/support-channels/instant-messaging/telegram/articles/telegram-integration-with-zoho-desk#How_to_create_a_Telegram_Bot)
