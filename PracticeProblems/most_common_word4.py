def main():
    sentence = 'Knowing that millions of people around the world would be ' \
               'watching in person and on television and expecting great ' \
               'things from him — at least one more gold medal for America, ' \
               'if not another world record — during this, his fourth and ' \
               'surely his last appearance in the World Olympics, ' \
               'and realizing that his legs could no longer carry him down ' \
               'the runway with the same blazing speed and confidence in ' \
               'making a huge, eye-popping leap that they were capable of a ' \
               'few years ago when he set world records in the 100-meter ' \
               'dash and in the 400-meter relay and won a silver medal in ' \
               'the long jump, the renowned sprinter and track-and-field ' \
               'personality Carl Lewis, who had known pressure from fans and ' \
               'media before but never, even as a professional runner, ' \
               'this kind of pressure, made only a few appearances in races  ' \
               'during the few months before the Summer Olympics in Atlanta, ' \
               'Georgia, partly because he was afraid of raising ' \
               'expectations even higher and he did not want to be ' \
               'distracted by interviews and adoring fans who would follow ' \
               'him into stores and restaurants demanding autographs and ' \
               'photo-opportunities, but mostly because he wanted to ' \
               'conserve his energies and concentrate, like a martial arts ' \
               'expert, on the job at hand: winning his favorite competition, ' \
               'the long jump, and bringing home another Gold Medal for the ' \
               'United States, the most fitting conclusion to his brilliant ' \
               'career in track and field.'
    sentences = [sentence, 'Many people have lots of different things. Have '
                           'have have have. Most people want more but have '
                           'less']

    for test in sentences:
        word, occurences = get_word(test)
        print(word, 'occured', occurences, 'times.')


def get_word(sentence):
    sentence = sentence.replace('.', '').replace(',', '').lower().split()
    # strip would have to used after splitting the strings apart
    # sentence = sentence.strip(".,?!").lower().split()
    print(sentence)
    freq_table = dict()
    for word in sentence:
        if len(word) == 4:
            freq_table[word] = freq_table.get(word, 0) + 1
    max_value = 0
    max_key = ''
    for key, value in freq_table.items():
        # this will return first max number. If there is a tie then first
        # word is still used
        if value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value

if __name__ == '__main__':
    main()
