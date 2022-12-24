# Simple Spell Checker
#### Video Demo:  https://youtu.be/-jbdyLVBeGw
#### Description
For my CS50 final project, I made a website that uses python and flask to implement a spell checking tool that corrects words and gives statistics such as total number of words, a character counter for the original text, and a misspelled-word count.

Using Flask, I created a one-page web application, with home.html as the web page it operates on. The page has two text boxes. The first takes input from the user and the second displays the corrected text. My code parses through the text and separates words using spaces and punctuations. It then uses functions from the pyspellchecker library to check whether the word is spelt correctly or not, and appends the incorrectly spelt words to an array.

As the characters are copied from the old text to the new text, the misspelled words get replaced with the suggested correction provided by the spell checker function from the pyspellchecker library. The new text, number of total words, character count and number of misspelled words are used when rendering the HTML template, with the new text being displayed in the bottom text box, and the other information is displayed on the right side of the page.

I uploaded a json file named words_dictionary.json from https://github.com/dwyl/english-words containing 466k plus words for the spell checker functions to make use of, allowing it to recognise more words as spelt correctly. If there is no suggested correction for a incorrectly-spelled word, it will just be shown as it is in the corrected text.

The css file styles.css is a stylesheet for the web page. I used css to give the page a two-column layout to display the text boxes and stats side-by-side for a better visual look, and made everything look more centered. The background image does not belong to me and was taken from https://www.freepik.com/free-photo/vintage-crumpled-paper-textured-background_15599884.htm#query=parchment%20texture&position=14&from_view=keyword as credited in the footer of the page. All texts on page (excluding inside the text boxes) are in the Verdana font.

#### Languages and Libraries
* HTML
* Python
* Flask
* [pyspellchecker library](https://pypi.org/project/pyspellchecker/)
* string library

#### Problems
The tool is not completely accurate. Some words may be counted as 'incorrect' and will be 'corrected' to something else. This most notably happens with words ending in 's and (s) as apostrophes and brackets are used to separate words, so the letter 's' counts as one word and will be corrected. A possible feature that could be added is to directly tell the user which words were corrected and give a list of other possible corrections for the misspelled words.