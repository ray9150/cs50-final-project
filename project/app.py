from flask import Flask, render_template, request
from spellchecker import SpellChecker
import string

app = Flask(__name__)

spell = SpellChecker()

#file taken from https://github.com/dwyl/english-words
spell.word_frequency.load_dictionary("words_dictionary.json")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        misspelled_words = []
        old_text = request.form.get("old_text")
        start_word = 0
        end_word = 0
        word_made = False
        end_sentence = list(string.punctuation)
        end_sentence.append(" ")
        character_counter = 0
        word_counter = 0
        for i in (old_text):
            if word_made:
                if i not in end_sentence:
                    start_word = character_counter
                    word_made = False
            else:
                if i in end_sentence:
                    end_word = character_counter
                    temp = old_text[start_word:end_word].lower()
                    if spell[temp] == False and temp.isnumeric() == False:
                        misspelled_words.append([temp, start_word, end_word])
                    word_made = True
                    word_counter += 1
            character_counter += 1
        if word_made == False:
            end_word = character_counter + 1
            temp = old_text[start_word:end_word].lower()
            if spell[temp] == False and temp.isnumeric() == False:
                        misspelled_words.append([temp, start_word, end_word])
            word_counter += 1

        new_text = ""
        if len(misspelled_words) != 0:
            character_counter2 = 0
            word_corrected = False
            word_counter2 = 0
            for j in old_text:
                for k in range(len(misspelled_words)):
                    if character_counter2 == misspelled_words[k][1]:
                        temp = spell.correction(misspelled_words[word_counter2][0])
                        if temp != None:
                            new_text += temp
                        else:
                            new_text += misspelled_words[word_counter2][0]
                        word_corrected = True
                        word_counter2 += 1
                    elif character_counter2 == misspelled_words[k][2]:
                        word_corrected = False
                if word_corrected == False:
                    new_text += j
                character_counter2 += 1
        else:
            new_text = "There were no missplelled words found in the above text."
        return render_template("home.html", old_text=old_text, new_text=new_text, w_count=word_counter, char_count=character_counter, miss_word=len(misspelled_words))
    else:
        return render_template("home.html")