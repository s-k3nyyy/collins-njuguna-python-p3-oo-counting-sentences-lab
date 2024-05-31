class MyString:
    '''MyString in count_sentences.py'''

    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
            self.value = ""
        else:
            self.value = value

    def count_sentences(self):
        '''returns the number of sentences in the value.'''
        if not self.value:
            return 0
        else:
            sentences = self.value.replace('?', '.').replace('!', '.').split('.')
            return sum(1 for sentence in sentences if sentence.strip())

    def is_sentence(self):
        '''returns True if value ends with a period and False otherwise.'''
        return self.value.endswith('.')

    def is_question(self):
        '''returns True if value ends with a question mark and False otherwise.'''
        return self.value.endswith('?')

    def is_exclamation(self):
        '''returns True if value ends with an exclamation mark and False otherwise.'''
        return self.value.endswith('!')
