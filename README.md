# Interface Screenshots

<img width="474" alt="vocabber_1" src="https://user-images.githubusercontent.com/67496158/157855860-ef7b59b9-c714-4f52-be56-f98a60ebd643.png">
<img width="473" alt="vocabber_2" src="https://user-images.githubusercontent.com/67496158/157855879-3508e9e6-09a1-47c7-a654-0a1df921c35b.png">


# User Guide

You can run the program by downloading `Vocabber.zip`, unzipping it, and running `Vocabber.py` with Python.

Welcome to Vocabber! This small program aims to help language learners memorize new words. Vocabber supports most languages in the world (utf-16 character set). In addition, Vocabber does not support the Internet, so there is no need to use the Internet, and users need to input new words by themselves.

## Functionalities

### 1. Create a word list ("Create")

We recommend creating a word list for each language.

### 2. Delete a word list ("Delete")

You can delete word lists that you do not want to keep (such as sample data).

### 3. Enter new words ("Enter new words")

Here you can enter new words, and you can enter up to 4 definitions for a word. Optionally, each definition can be classified using the "Category" column. We recommend classifying according to parts of speech (nouns, verbs, adjectives…).

If you want to add a new definition to an existing word, just enter the new definition once, and the program will integrate it into the original definition (but the total number does not exceed 4).

### 4. Vocabulary quiz ("Vocab quiz")

After entering, select a scope ("scope") for the word quiz. On the left you can enter the number of words for the quiz. If the "Generate options from the same category" option is checked, all options in the quiz will select the same category as the correct answer (when the word has multiple categories, one is selected randomly). The time to stay in the current page after selection can be modified in Settings.

The scope of "Recent inputs" is the most recently entered vocabulary (default is 5 days, which can be modified in Settings).

When you enter a new word, its familiarity is 1. Each time you answer correctly in the quiz, the word's familarity will increase by 1. Each wrong answer will half the word's familarity. All words with a familiarity below a certain value (default is 4, can be modified in Settings) belong to "Unfamiliar words".

After starting the quiz, you can click the star to the right of a word to mark the word. They will be classified as "Marked words".
Words that you answer incorrectly will be stored in the "Mistakes collection".

### 5. "Word list"

Each definition of each word in the word list occupies one line, so a word may appear on up to 4 lines.
If there is a spelling error, you can edit the word in the word list, delete the definition, and then you can re-enter it on the input new word interface.

### 6. "Statistics"

Vocabber keeps track of your learning journey. When the word list is deleted, Statistics also deletes the corresponding records.
