from complainer_bot import InternetSpeedTwitterBot


CHROME_DRIVER_PATH = "C:\Programming\Web Driver\chromedriver.exe"
PROMISED_DOWN = 600
PROMISED_UP = 20

complainer_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
complainer_bot.get_internet_speed()
if complainer_bot.down < PROMISED_DOWN or complainer_bot.up < PROMISED_UP:
    complainer_bot.tweet_at_provider(PROMISED_DOWN, PROMISED_UP)

