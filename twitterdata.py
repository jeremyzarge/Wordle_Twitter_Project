import pandas as pd
from ntscraper import Nitter


def char_to_num(color):
    if color == '⬜' or color == '⬛':
        return 0
    if color == '🟨':
        return 1
    if color == '🟩':
        return 2
    return 0


def tweet_to_tuple(text):
    first_grey = text.find('⬜')
    if first_grey == -1:
        first_grey = 5000
    first_yellow = text.find('🟨')
    if first_yellow == -1:
        first_yellow = 5000
    first_green = text.find('🟩')
    if first_green == -1:
        first_green = 5000
    first_black = text.find('⬛')
    if first_black == -1:
        first_black = 5000
    if min(first_green, first_yellow, first_grey, first_black) == 5000:
        return []
    else:
        first = min(first_green, first_yellow, first_grey, first_black)
        connec_check = (len(text[first:]) >= 5) and (
            text[first+4] == '🟩' or text[first+4] == '🟨' or text[first+4] == '⬜' or text[first+4] == '⬛')
        if not connec_check:
            return tweet_to_tuple(text[first+4:])
        else:
            bandle_check = (len(text[first:]) >= 6) and not (
                text[first+5] == '🟩' or text[first+5] == '🟨' or text[first+5] == '⬜' or text[first+5] == '⬛')
            if not bandle_check:
                return tweet_to_tuple(text[first+5:])
            one = char_to_num(text[first])
            two = char_to_num(text[first+1])
            three = char_to_num(text[first+2])
            four = char_to_num(text[first+3])
            five = char_to_num(text[first+4])
            return ([(one, two, three, four, five)] + tweet_to_tuple(text[first+5:]))


scraper = Nitter(log_level=1, skip_instance_check=False)

wordle_tweets = scraper.get_tweets(
    "wordle930", mode='hashtag', number=50, instance=None)
# Replace with today's wordle number

combo = []
for tweet in wordle_tweets['tweets']:
    combo += tweet_to_tuple(tweet['text'])

print(combo)
