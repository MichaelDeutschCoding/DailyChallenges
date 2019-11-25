from operator import itemgetter
import string

class Text:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.text = f.read()
        words = self.text.lower().split()
        # self.word_list = [word.strip(';")(,.?') for word in words if word.isalpha()]
        # self.word_list = [word for word in words if word.isalpha()]
        self.word_list = [word.strip(',/.?")(;') for word in words if not word.isdigit()]

    def word_count(self):
        self.count_dict = {}
        for word in self.word_list:
            try:
                self.count_dict[word] +=1
            except KeyError:
                self.count_dict[word] = 1 

    def print_words(self, num):
        """ Prints alphabetized {num} of words and their frequency"""
        print(' WORD                 COUNT')
        print('=' * 28)
        for word, count in sorted(self.count_dict.items())[:num]:
            print(f'{word:<20}', count)

    def print_top(self, num):
        print('   WORD             COUNT')
        print('=' * 18,    " ======")  
        for key, value in sorted(self.count_dict.items(), key = itemgetter(1), reverse = True) [:num]:
            print(f'{key:<20}', value)

    def unique_words(self):
        self.unique = [word for word, freq in self.count_dict.items() if freq == 1]

    def remove_punctuation(self):
        return ''.join((char for char in self.text if char not in string.punctuation))

    def remove_stop_words(self):
        stop_words = [key for key, value in sorted(self.count_dict.items(), key= itemgetter(1), reverse=True)[:50]]
        return ' '.join((word for word in self.word_list if word not in stop_words))


stranger = Text('the_stranger.txt')
stranger.word_count()
stranger.unique_words()
print(len(stranger.word_list))
print(len(stranger.unique))
# print(stranger.word_list[:100])
# print(stranger.remove_stop_words())
