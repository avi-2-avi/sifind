from tkinter.constants import FIRST
import string
import re, json
import enchant
# import difflib

# Diccionario que evalua las palabras en Español - Perú
# Se necesita de Node.js para compilarlo y descargar diccionario es_PE
# https://github.com/wooorm/dictionaries/tree/main/dictionaries/es-PE
# https://github.com/LibreOffice/dictionaries
dic = enchant.Dict("es_PE")

class Sentence:
    firstWord = None
    lastWord = None
    sentence = None

    def __init__(self, sentence):
        self.sentence = sentence

    def check_idioms(self, word):
        idioms = 'src/abrev.json'
        with open(idioms, 'r') as idf:
            idioms_content = idf.read()
        idioms_content = json.loads(idioms_content)

        if dic.check(word) == False:
            for key, value in idioms_content.items():
                if(word == key):
                    word = value
        return word

    def get_words(self):
        # Regla 1: Patrones de puntuacion
        pattern = r'[' + string.punctuation + ']'
        self.sentence = re.sub(pattern, ' ', self.sentence)

        lis = list(self.sentence.split(" "))  
        # Regla 2: Palabras en minuscula
        firstWord = lis[0].lower()
        lastWord = lis[len(lis)-1].lower()

        # Regla 3: Jergas
        lastWord = self.check_idioms(lastWord)
        lastWord = lastWord.replace('\n', '')
        firstWord = self.check_idioms(firstWord)

        return (lastWord, firstWord) 


class List:
    _words_list = []

    def get_freq(self, _list):
        _dict = {}
        for word in _list:
            if word in _dict:
                _dict[word] += 1
            else:
                _dict[word] = 1

        # Regla 4: Homofonos - Parte 2
        # Utilizar sugestion mas cercana si no hay similitudes en los resultados ya obtenidos 
        # No se utilizo ya que no es muy preciso
#        _tmp_dic = {}
#        for key, value in _dict.items():
#            if dic.check(key) == False:
#                print(key)
#                dict,max = {}, 0
#                suggestions = set(dic.suggest(key))
#
#                for pos in suggestions:
#                    tmp = difflib.SequenceMatcher(None, word, pos).ratio()
#                    dict[tmp] = pos
#                    if tmp > max:
#                        max = tmp
#                key = dict[max]
#            _tmp_dic[key] = value
            
        return _dict

    def check_list(self, _list):

        # Regla 4: Homofonos - Parte 1
        # Checkear con palabras que ya estan en el diccionario 
        new_list = []
        for word in _list:
            if dic.check(word) == False:
                suggestions = set(dic.suggest(word))

                # Sugestiones
                for pos in suggestions:
                    # Palabras en la lista
                    for _word in self._words_list:
                        if pos == _word:
                            word = _word

            new_list.append(word)
        return new_list 

    def get_lists(self, filename):
        # Test
        # filename = 'src/input_testing.txt'

        with open(filename) as f:
            lines = f.readlines()

        lastl, firstl = [], []

        for line in lines:
            ev = Sentence(line)
            lastWord, firstWord = ev.get_words() 
            lastl.append(lastWord)
            firstl.append(firstWord)
            lastl.sort()
            firstl.sort()

        self._words_list = lastl + firstl 
        firstl = self.check_list(firstl)
        lastl = self.check_list(lastl)

        lastDic = self.get_freq(lastl)
        firstDic = self.get_freq(firstl)

        return (firstDic, lastDic)
