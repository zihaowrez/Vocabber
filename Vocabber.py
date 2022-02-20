from tkinter import *
from tkinter import ttk
from random import *
from datetime import *
from PIL import Image, ImageTk
import os

def statistics():

    def back_home():
        frame.destroy()
        home_frame = home()
        home_frame.pack(fill = 'both', expand = True)
        return home_frame

    frame = Frame(window)

    title = Label(frame, text = 'Statistics', font = (THEME_FONT, 24))
    title.place(x = 320, y = 70, anchor = 'center')

    langs, word_counts = read_initial()[-2:]

    now = datetime.now()
    days = (now - datetime.strptime(install_date, '%Y-%m-%d')).days
    days_lbl = Label(frame, text = 'It has been ' + str(days)
                     + ' days since you installed Vocabber.', font = (THEME_FONT, 14))
    days_lbl.place(x = 40, y = 120)

    if word_counts:

        sum_lbl = Label(frame, text = 'You have learned ' + str(sum(word_counts))
                        + ' words with Vocabber, including', font = (THEME_FONT, 14))
        sum_lbl.place(x = 40, y = 160)

        count_lbls = []
        for i in range(len(langs)):
            count_lbls.append(Label(frame, text = str(word_counts[i])
                                    + ' from ' + langs[i], font = (THEME_FONT, 13)))
            x = 40 + 200 * (i // 5)
            count_lbls[-1].place(x = x, y = 210 + 35 * (i % 5))

        comment_lbl = Label(frame, text = 'Keep it up!', font = (THEME_FONT, 14))
        comment_lbl.place(x = 40, y = 400)

    else:
        comment_lbl = Label(frame, text = 'Seems that you have not started yet. ◑.◑',
                            justify = 'left', font = (THEME_FONT, 14))
        comment_lbl.place(x = 40, y = 160)

    back = Button(frame, text = 'Back', font = (THEME_FONT, 14), bd = 2,
                  command = lambda: back_home().tkraise())
    back.place(x = 540, y = 30)

    frame.pack(fill = 'both', expand = True)

    return frame

def settings():

    def save():

        RE_etr.config(bg = 'white')
        FL_etr.config(bg = 'white')
        CD_etr.config(bg = 'white')
        WD_etr.config(bg = 'white')

        try:
            RE = int(RE_etr.get())
        except:
            RE_etr.config(bg = 'pink')
            return 
        else:
            if RE <= 0:
                RE_etr.config(bg = 'pink')
                return 
        
        try:
            FL = int(FL_etr.get())
        except:
            FL_etr.config(bg = 'pink')
            return 
        else:
            if FL <= 0:
                FL_etr.config(bg = 'pink')
                return

        try:
            CD = float(CD_etr.get())
        except:
            CD_etr.config(bg = 'pink')
            return 
        else:
            if CD <= 0:
                CD_etr.config(bg = 'pink')
                return 

        try:
            WD = float(WD_etr.get())
        except:
            WD_etr.config(bg = 'pink')
            return 
        else:
            if WD <= 0:
                WD_etr.config(bg = 'pink')
                return

        NUM_CHOICES = int(NC_cmb.get())
        RECENT = RE
        FAMILIAR_LINE = FL
        CORRECT_DELAY = round(CD * 1000)
        WRONG_DELAY = round(WD * 1000)

        write_initial(langs, word_counts, (NUM_CHOICES, RECENT, FAMILIAR_LINE, CORRECT_DELAY, WRONG_DELAY))

        FL_etr.config(bg = 'white')
        CD_etr.config(bg = 'white')
        WD_etr.config(bg = 'white')

        msg = Label(s_window, text = 'Saved.', fg = 'green')
        msg.place(x = 400, y = 330)
        msg.after(2000, msg.destroy)

        frame = home()

    s_window = Toplevel()
    s_window.title('Settings')
    s_window.geometry('560x380+20+20')

    NC, RE, FL, CD, WD, install_date, langs, word_counts = read_initial()

    NC_lbl = Label(s_window, text = 'Number of choices in quiz: ',
                       font = (THEME_FONT, 13))
    NC_lbl.grid(column = 0, row = 0)
    NC_lbl.config(height = 2, width = 25, anchor = 'se')

    NC_values = [4, 6, 8]
    NC_cmb = ttk.Combobox(s_window, values = NC_values)
    NC_cmb.current(NC_values.index(NC))
    NC_cmb.grid(column = 1, row = 0, sticky = 'sw')
    NC_cmb.config(width = 4)

    RE_lbl = Label(s_window, text = 'A word is categorized under "Recent Words"\nin         days after input',
                   justify = 'left', font = (THEME_FONT, 13))
    RE_lbl.place(x = 32, y = 70)
    RE_etr = Entry(s_window, bd = 2)
    RE_etr.insert(0, str(RE))
    RE_etr.place(x = 55, y = 100)
    RE_etr.config(width = 4)

    FL_lbl = Label(s_window, text = 'A word is categorized under "Unfamiliar Words"\nif the familiarity is below',
                   justify = 'left', font = (THEME_FONT, 13))
    FL_lbl.place(x = 32, y = 140)
    FL_etr = Entry(s_window, bd = 2)
    FL_etr.insert(0, str(FL))
    FL_etr.place(x = 240, y = 170)
    FL_etr.config(width = 4)

    CD_lbl = Label(s_window, text = 'In quiz, go to the next word in        s if answered correctly.',
                       font = (THEME_FONT, 13))
    CD_lbl.place(x = 32, y = 210)
    CD_etr = Entry(s_window, bd = 2)
    CD_etr.insert(0, str(round(CD / 1000, 1)))
    CD_etr.place(x = 285, y = 215)
    CD_etr.config(width = 4)

    WD_lbl = Label(s_window, text = 'In quiz, go to the next word in        s if answered wrongly.',
                       font = (THEME_FONT, 13))
    WD_lbl.place(x = 32, y = 260)
    WD_etr = Entry(s_window, bd = 2)
    WD_etr.insert(0, str(round(WD / 1000, 1)))
    WD_etr.place(x = 285, y = 265)
    WD_etr.config(width = 4)

    save_btn = Button(s_window, text = 'Save', command = save, font = (THEME_FONT, 13))
    save_btn.place(x = 470, y = 320)

    s_window.focus()

    s_window.mainloop()

def remove_space(s):
    while s and s[0] == ' ':
        s = s[1:]
    while s and s[-1] == ' ' :
        s = s[:-1]
    return s

def message_window(message, *actions):
    m_window = Toplevel()
    m_window.title('Message')
    m_window.geometry('480x240+20+20')
    text = Label(m_window, text = message, font = (THEME_FONT, 14))
    text.place(x = 240, y = 100, anchor = 'center')
    btns = []
    x_indent = 0
    for i in range(len(actions)):
        
        def cmd(actions):
            def combined():
                m_window.destroy()
                for action in actions[1:]:
                    action()
            return combined
        
        btns.append(Button(m_window, text = actions[i][0], font = (THEME_FONT, 14),
                   command = cmd(actions[i])))
        btns[i].place(x = 450 - x_indent, y = 200, anchor = 'e')
        x_indent += 40 + 8 * len(actions[i][0])

    m_window.focus()        
    m_window.mainloop()

def create_lang(new_lang, lang_seln):
    lang = new_lang.get()
    lang = remove_space(lang)
    if lang:
        if lang in langs:
            message_window('Language already exists.\n', ('Ok', ))
        else:
            langs.insert(0, lang)
            f = open(PATH + lang + '.txt', 'w')
            f.close()
            
            lang_list, word_counts = read_initial()[-2:]
            lang_list.insert(0, lang)
            word_counts.insert(0, 0)
            
            write_initial(lang_list, word_counts)
            
            lang_seln.insert(0, lang)
            new_lang.delete(0, 'end')

def rename_lang(lang_seln):

    def rename():

        lang = lang_seln.get(ACTIVE)
        langs.remove(lang)
        
        lang_list, word_counts = read_initial()[-2:]
        pos = lang_list.index(lang)
        lang_list.insert(pos, name_etr.get())
        lang_list.remove(lang)
        
        write_initial(lang_list, word_counts)

        lang_seln.delete(pos)
        lang_seln.insert(pos, lang_list[pos])
        
        r_window.destroy()
    
    if lang_seln.curselection():
        
        lang = lang_seln.get(ACTIVE)

        r_window = Toplevel()
        r_window.title('Rename')
        r_window.geometry('480x240+20+20')

        title = Label(r_window, text = lang, font = (THEME_FONT, 18))
        title.place(x = 240, y = 70, anchor = 'center')

        name_etr = Entry(r_window, text = lang)
        name_etr.place(x = 240, y = 120, anchor = 'center')
        name_etr.config(width = 24)

        confirm_btn = Button(r_window, text = 'Confirm', font = (THEME_FONT, 14),
                             command = rename)
        confirm_btn.place(x = 240, y = 180, anchor = 'center')

        def to_rename(key):
            rename()

        r_window.bind('<Return>', to_rename)

        r_window.focus()        
        r_window.mainloop()

def delete_lang(lang_seln):
    
    def lang_deletion():
        lang = lang_seln.get(ACTIVE)
        langs.remove(lang)
        os.remove(PATH + lang + '.txt')
        
        lang_list, word_counts = read_initial()[-2:]
        word_counts.pop(lang_list.index(lang))
        lang_list.remove(lang)
        
        write_initial(lang_list, word_counts)
        
        lang_seln.delete(ACTIVE)
    
    if lang_seln.curselection():
        lang = lang_seln.get(ACTIVE)
        message_window('You are deleting the vocab file "' + lang + '".\n' +
                       'Are you sure?\n', ('No', ), ('Yes', lang_deletion)) 

def read_initial():
    f = open(PATH + 'initialize.txt', 'r', encoding = 'utf-16')
    data = f.read().split('\n')

    NC, RE, FL, CD, WD = [int(x) for x in data[:5]]
    install_date = data[5]
    
    while data[-1] == '':
        del data[-1]

    langs = data[6::2]
    word_counts = data[7::2]
    word_counts = [int(count) for count in word_counts]
    
    return NC, RE, FL, CD, WD, install_date, langs, word_counts


def write_initial(langs, word_counts, *pars):
    f = open(PATH + 'initialize.txt', 'w', encoding = 'utf-16')
    if pars:
        for par in pars[0]:
            f.write(str(par) + '\n')
    else:
        f.write(str(NUM_CHOICES) + '\n' + str(RECENT) + '\n' + str(FAMILIAR_LINE) + '\n' +
                str(CORRECT_DELAY) + '\n' + str(WRONG_DELAY) + '\n')
    f.write(install_date + '\n')
    for i in range(len(langs)):
        f.write(langs[i] + '\n' + str(word_counts[i]) + '\n')
    f.close()
    
def read_vocab_file(lang):
    f = open(PATH + lang + '.txt', 'r', encoding = 'utf-16')
    vocabs = f.read().split(sep = '\n')[:-1]
    f.close()
    words = []
    familiarities = []
    lasts = []
    times = []
    marks = []
    categories = []
    meanings = []
    for i in range(len(vocabs)):
        v = vocabs[i].split(sep = '\t')[:-1]
        words.append(v[0])
        familiarities.append(int(v[1]))
        lasts.append(int(v[2]))
        times.append(datetime.strptime(v[3], '%Y-%m-%d'))
        marks.append(int(v[4]))
        categories.append([])
        meanings.append([])
        for j in range(5, len(v), 2):
            categories[-1].append(v[j])
            meanings[-1].append(v[j+1])
        
    return words, familiarities, lasts, times, marks, categories, meanings

def renew_langs(lang):
    index = langs.index(lang)
    langs.insert(0, langs.pop(index))
    word_counts = read_initial()[-1]
    word_counts.insert(0, word_counts.pop(index))
    write_initial(langs, word_counts)

def input_vocab(lang):

    def back_home():
        frame.destroy()
        home_frame = home()
        home_frame.pack(fill = 'both', expand = True)
        return home_frame
    
    frame = Frame(window)

    if lang:
        
        renew_langs(lang)

        words, familiarities, lasts, times, marks, categories, meanings = read_vocab_file(lang)

        title = Label(frame, text = 'Enter New Words', font = (THEME_FONT, 20))
        title.place(x = 320, y = 70, anchor = 'center')
        language = Label(frame, text = 'To vocab file: ' + lang,
                         font = (THEME_FONT, 14), fg = 'red')
        language.place(x = 320, y = 110, anchor = 'center')

        category_lbl, meaning_lbl = [], []
        
        word_lbl = Label(frame, text = '* Word', font = (THEME_FONT, 14))
        word_lbl.place(x = 40, y = 160, anchor = 'w')

        compul_lbl = Label(frame, text = '* Compulsory', font = (THEME_FONT, 13))
        compul_lbl.place(x = 440, y = 155, anchor = 'w')

        def onWord(key):
            if key.keycode == 40:
                category_etr[0].focus()
            elif key.keycode == 13:
                if input_vocab():
                    word_etr.focus()
   
        def onCategory(key, i):
            if key.keycode == 40:
                meaning_etr[i].focus()
            elif key.keycode == 38 and i == 0:
                word_etr.focus_set()
            elif key.keycode == 38:
                meaning_etr[i-1].focus()
            elif key.keycode == 13:
                if input_vocab():
                    word_etr.focus()

        def onMeaning(key, i):
            if key.keycode == 40 and i < 3:
                category_etr[i+1].focus()
            elif key.keycode == 38:
                category_etr[i].focus()
            elif key.keycode == 13:
                if input_vocab():
                    word_etr.focus()

        category_etr, meaning_etr = [], []
        
        word_etr = Entry(frame, bd = 2)
        word_etr.place(x = 160, y = 160, anchor = 'w')
        word_etr.config(width = 20)

        word_etr.bind('<Key>', lambda key: onWord(key))

        for i in range(4):

            meaning_text = '* Meaning ' if i == 0 else 'Meaning '

            category_lbl.append(Label(frame, text = 'Category ' + str(i+1),
                                 font = (THEME_FONT, 14)))
            category_lbl[-1].place(x = 40 + 280 * (i // 2), y = 205 + 100 * (i % 2), anchor = 'w')
            meaning_lbl.append(Label(frame, text = meaning_text + str(i+1),
                                     font = (THEME_FONT, 14)))
            meaning_lbl[-1].place(x = 40 + 280 * (i // 2), y = 250 + 100 * (i % 2), anchor = 'w')
            
            category_etr.append(Entry(frame, bd = 2))
            category_etr[-1].place(x = 160 + 280 * (i // 2), y = 205 + 100 * (i % 2), anchor = 'w')
            category_etr[-1].config(width = 20)

            category_etr[-1].bind('<Key>', lambda key, i = i: onCategory(key, i))
        
            meaning_etr.append(Entry(frame, bd = 2))
            meaning_etr[-1].place(x = 160 + 280 * (i // 2), y = 250 + 100 * (i % 2), anchor = 'w')
            meaning_etr[-1].config(width = 20)

            meaning_etr[-1].bind('<Key>', lambda key, i = i: onMeaning(key, i))

        def input_vocab():
            
            word_etr.config(background = 'white')
            for i in range(4):
                category_etr[i].config(bg = 'white')
                meaning_etr[i].config(bg = 'white')

            wd = remove_space(word_etr.get())
            if not wd:
                word_etr.config(bg = 'pink')
                return True

            cat, mng = [], []
            
            for i in range(4):
                cat.append(remove_space(category_etr[i].get()))
                mng.append(remove_space(meaning_etr[i].get()))
                if mng[-1] and cat[-1] in cat[:-1]:
                    category_etr[i].config(bg = 'pink')
                    category_etr[i].focus()
                    return 
                if not mng[-1]:
                    if i != 0 and not cat[-1]:
                        cat = cat[:-1]
                        mng = mng[:-1]
                    else:
                        cat, mng = [], []
                        meaning_etr[i].config(bg = 'pink')
                        meaning_etr[i].focus()
                        return 
            
            if wd in words:

                i = words.index(wd)

                def no():
                    m_window.destroy()
                
                def replace():

                    for j in range(len(categories[i])):
                        if categories[i][j] not in cat:
                            cat.append(categories[i][j])
                            mng.append(meanings[i][j])

                    categories[i], meanings[i] = cat, mng
                    times[i] = datetime.now()
                    familiarities[i] = round(familiarities[i] / 2)
                        
                    f = open(PATH + lang + '.txt', 'w', encoding = 'utf-16')
                    for j in range(len(words)):
                        
                        f.write(words[j] + '\t' + str(familiarities[j]) + '\t'
                                + str(lasts[j]) + '\t'
                                + datetime.strftime(times[j], '%Y-%m-%d') + '\t'
                                + str(marks[j]) + '\t')
                        for k in range(len(categories[j])):
                            f.write(categories[j][k] + '\t' + meanings[j][k] + '\t')
                        f.write('\n')
                    f.close()
                    word_etr.delete(0, 'end')
                    for j in range(4):
                        category_etr[j].delete(0, 'end')
                        meaning_etr[j].delete(0, 'end')

                    m_window.destroy()
                    msg = Label(frame, text = 'Replaced Successfully!', fg = 'green')
                    msg.place(x = 420, y = 405)
                    msg.after(2000, msg.destroy)

                original = ''
                for j in range(len(categories[i])):
                    if categories[i][j]:
                        original += categories[i][j]
                    original += meanings[i][j] + '\n'

                new = ''
                for j in range(len(cat)):
                    if cat[j]:
                        new += cat[j] + ' '
                    new += mng[j] + '\n'
                for j in range(len(categories[i])):
                    if categories[i][j] not in cat and len(cat) < 4:
                        if categories[i][j]:
                            new += categories[i][j] + ' '
                        new += meanings[i][j] + '\n'

                m_window = Toplevel()
                m_window.title('Message')
                m_window.geometry('480x360+20+20')

                msg_lbl = Label(m_window, text = 'Word already exists.\nDo you want to replace it?\n\n',
                                font = (THEME_FONT, 14))
                msg_lbl.place(x = 240, y = 80, anchor = 'center')
                wd_lbl = Label(m_window, text = wd, fg = 'red',
                               font = (THEME_FONT, 14, 'italic'))
                wd_lbl.place(x = 240, y = 110, anchor = 'center')
                grp_lbl1 = Label(m_window, text = 'Original', fg = 'grey',
                                 font = (THEME_FONT, 14))
                grp_lbl1.place(x = 120, y = 140, anchor = 'center')
                grp_lbl2 = Label(m_window, text = 'New', fg = 'blue',
                                 font = (THEME_FONT, 14))
                grp_lbl2.place(x = 360, y = 140, anchor = 'center')
                
                original_lbl = Label(m_window, text = original, justify = 'left')
                original_lbl.place(x = 60, y = 160)
                new_lbl = Label(m_window, text = new, justify = 'left')
                new_lbl.place(x = 300, y = 160)

                yes_btn = Button(m_window, text = 'Yes', font = (THEME_FONT, 13),
                                 command = replace)
                yes_btn.place(x = 394, y = 310, anchor = 'e')
                no_btn = Button(m_window, text = 'No', font = (THEME_FONT, 13), command = no)
                no_btn.place(x = 450, y = 310, anchor = 'e')

                def onKey(key):
                    replace()
                
                m_window.bind('<Return>', onKey)
                m_window.focus()
                
                '''message_window('Word already exists.\nDo you want to replace it?\n\n'
                               + words[i] + '\nOriginal:'
                               + '           New:',
                                ('No', ), ('Yes', replace))'''
                
            else:
                words.append(wd)
                familiarities.append(1)
                lasts.append(0)
                times.append(datetime.now())
                marks.append(0)
                categories.append(cat)
                meanings.append(mng)
                    
                f = open(PATH + lang + '.txt', 'a', encoding = 'utf-16')
                f.write(wd + '\t1\t0\t' + datetime.now().strftime('%Y-%m-%d') + '\t0\t')
                for i in range(len(cat)):
                    f.write(cat[i] + '\t' + mng[i] + '\t')
                f.write('\n')
                f.close()
                    
                word_etr.delete(0, 'end')
                for i in range(4):
                    category_etr[i].delete(0, 'end')
                    meaning_etr[i].delete(0, 'end')
                msg = Label(frame, text = 'Input Successfully!', fg = 'green')
                msg.place(x = 420, y = 405)
                msg.after(2000, msg.destroy)

            return True

        input_btn = Button(frame, text = 'Input', font = (THEME_FONT, 14),
                       command = lambda: input_vocab())
        input_btn.place(x = 320, y = 420, anchor = 'center')
        input_btn.config(width = 12)
        
        back = Button(frame, text = 'Back', font = (THEME_FONT, 14),
                       command = lambda: back_home().tkraise())
        back.place(x = 540, y = 30)

        frame.pack(fill = 'both', expand = True)

        return frame

    else:
        return back_home()
        
def choose_scope(lang):

    def back_home():
        frame.destroy()
        home_frame = home()
        home_frame.pack(fill = 'both', expand = True)
        return home_frame

    def to_quiz(lang, scope, data):

        global SAME_CAT
        SAME_CAT = u.get()
        
        if v.get():
            m = select_etr.get()
            try:
                scope = sample(scope, min(len(scope), int(select_etr.get())))
            except:
                select_etr.config(bg = 'pink')
                return 

        frame.destroy()
        quiz_frame = quiz(lang, scope, data)
        quiz_frame.pack(fill = 'both', expand = True)
        return quiz_frame

    frame = Frame(window)
    
    if lang:

        renew_langs(lang)

        data = read_vocab_file(lang)
        words, familiarities, lasts, times, marks, categories, meanings = data
        n = len(words)

        title = Label(frame, text = 'Choose your scope', font = ('Comic Sans MS', 20))
        title.place(x = 320, y = 70, anchor = 'center')

        language_lbl = Label(frame, text = 'Current language: ' + lang,
                             font = ('Comic Sans MS', 14), fg = 'red')
        language_lbl.place(x = 320, y = 110, anchor = 'center')
        
        v = IntVar()
        select_chb = Checkbutton(frame, text = 'Choose       words\nfrom the scope',
                                 variable = v, justify = 'left', font = (THEME_FONT, 13))
        select_chb.place(x = 50, y = 180, anchor = 'w')
        select_etr = Entry(frame, bd = 2)
        select_etr.place(x = 137, y = 168, anchor = 'w')
        select_etr.config(width = 3)

        u = IntVar()
        same_cat_chb = Checkbutton(frame, text = 'Generate options\nfrom the same category',
                                   variable = u, justify = 'left', font = (THEME_FONT, 13))
        same_cat_chb.place(x = 50, y = 240, anchor = 'w')

        def check(event):
            select_chb.select()
        
        select_etr.bind('<ButtonRelease-1>', check)

        def s(len_scope):
            if len_scope == 1:
                return ' word'
            else:
                return ' words'

        all_btn = Button(frame, text = 'All words', font = ('Comic Sans MS', 14),
                         command = lambda: to_quiz(lang, range(n), data))
        all_btn.place(x = 320, y = 200, anchor = 'center')
        all_lbl = Label(frame, text = str(n) + s(n), font = (THEME_FONT, 13),
                        fg = 'blue')
        all_lbl.place(x = 320, y = 240, anchor = 'center')            
        
        now = datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
        recent_scope = [i for i in range(n) if (now - times[i]).days <= RECENT]
        recent_btn = Button(frame, text = 'Recent inputs', font = ('Comic Sans MS', 14),
                            command = lambda: to_quiz(lang, recent_scope, data))
        recent_btn.place(x = 500, y = 200, anchor = 'center')
        l = len(recent_scope)
        recent_lbl = Label(frame, text = str(l) + s(l), font = (THEME_FONT, 13),
                           fg = 'blue')
        recent_lbl.place(x = 500, y = 240, anchor = 'center')

        unfamil_scope = [i for i in range(n) if familiarities[i] < FAMILIAR_LINE]
        unfamil_btn = Button(frame, text = 'Unfamiliar words', font = ('Comic Sans MS', 14),
                             command = lambda: to_quiz(lang, unfamil_scope, data))
        l = len(unfamil_scope)
        unfamil_btn.place(x = 500, y = 320, anchor = 'center')
        unfamil_lbl = Label(frame, text = str(l) + s(l), font = (THEME_FONT, 13),
                            fg = 'blue')
        unfamil_lbl.place(x = 500, y = 360, anchor = 'center')

        last_scope = [i for i in range(n) if lasts[i]]
        last_btn = Button(frame, text = 'Mistakes collection', font = ('Comic Sans MS', 14),
                          command = lambda: to_quiz(lang, last_scope, data))
        l = len(last_scope)
        last_btn.place(x = 140, y = 320, anchor = 'center')
        last_lbl = Label(frame, text = str(l) + s(l), font = (THEME_FONT, 13),
                         fg = 'blue')
        last_lbl.place(x = 140, y = 360, anchor = 'center')

        marked_scope = [i for i in range(n) if marks[i]]
        marked_btn = Button(frame, text = 'Marked words', font = ('Comic Sans MS', 14),
                             command = lambda: to_quiz(lang, marked_scope, data))
        l = len(marked_scope)
        marked_btn.place(x = 320, y = 320, anchor = 'center')
        marked_lbl = Label(frame, text = str(l) + s(l), font = (THEME_FONT, 13),
                           fg = 'blue')
        marked_lbl.place(x = 320, y = 360, anchor = 'center')

        back = Button(frame, text = 'Back', font = (THEME_FONT, 14), bd = 2,
                      command = lambda: back_home().tkraise())
        back.place(x = 540, y = 30)
        
        frame.pack(fill = 'both', expand = True)
        
        return frame
        
    else:
        return back_home()

def quiz(lang, scope, data, counts = None, *shown):

    frame = Frame(window)
    
    if scope:

        def update(par):
            f = open(PATH + lang + '.txt', 'w', encoding = 'utf-16')
            for j in range(len(words)):
                f.write(words[j] + '\t' + str(familiarities[j]) + '\t' + str(lasts[j]) + '\t'
                        + times[j].strftime('%Y-%m-%d') + '\t' + str(marks[j]) + '\t')
                for k in range(len(categories[j])):
                    f.write(categories[j][k] + '\t' + meanings[j][k] + '\t')
                f.write('\n')
            f.close()

            langs, word_counts = read_initial()[-2:]
            word_counts[langs.index(lang)] += par
            write_initial(langs, word_counts)

        def back_home():
            update(0)
            frame.destroy()
            home_frame = home()
            home_frame.pack(fill = 'both', expand = True)
            return home_frame

        def show_next(lang, scope, data, counts, shown):
            next_frame = quiz(lang, scope, data, counts, shown)
            next_frame.pack(fill = 'both', expand = True)
            return next_frame

        def finished():
            frame.destroy()
            finish_frame = Frame(window)
            
            comments = ['Review the words and you will do better next time!',
                        'Don\'t give up! Practice makes perfect',
                        'Not bad! You\'re making progress!',
                        'Good job! Keep it up!',
                        'Amazing!',
                        'Congratulations!']
            if sum(counts):
                rate = round(counts[0] / sum(counts) * 100)
                if rate < 60:
                    text = Label(finish_frame, text = 'You\'ve got ' + str(rate) + '% correct.\n'
                                 + comments[randint(0, 1)], font = ('Comic Sans MS', 18))
                elif rate < 90:
                    text = Label(finish_frame, text = 'You\'ve got ' + str(rate) + '% correct!\n'
                                 + comments[randint(2, 3)], font = ('Comic Sans MS', 18))
                else:
                    text = Label(finish_frame, text = 'You\'ve got ' + str(rate) + '% correct!\n'
                                 + comments[randint(4, 5)], font = ('Comic Sans MS', 18))
                text.place(x = 320, y = 160, anchor = 'center')

            else:
                return back_home()
            
            '''next_word = Button(finish_frame, text = 'Next', font = ('Comic Sans MS', 14),
                               command = lambda: show_next().tkraise())
            next_word.place(x = 240, y = 330)'''

            def cmd():
                def combined():
                    finish_frame.destroy()
                    back_home().tkraise()
                return combined

            back = Button(finish_frame, text = 'Home', font = ('Comic Sans MS', 14), bd = 2,
                           command = cmd())
            back.place(x = 540, y = 30)

            finish_frame.pack(fill = 'both', expand = True)
            
            return finish_frame
        
        words, familiarities, lasts, times, marks, categories, meanings = data
        n = len(words)

        if shown:
            shown = shown[0]
        else:
            shown = dict()
            for i in scope:
                shown[i] = False
        not_shown = [i for i in shown.keys() if not shown[i]]
        correct = choice(not_shown)
        shown[correct] = 1
        indeces = [correct]
        
        m = min(n, NUM_CHOICES)
        if SAME_CAT:
            cat = choice(categories[correct])
        a, b = 0, 0
        while True:
            other = choice(range(n))
            if b > 3*n or len(indeces) == m:
                break
            if SAME_CAT and a < n:
                if cat not in categories[other]:
                    a += 1
                    continue
            if set(meanings[other]) == set(meanings[correct]):
                b += 1
                continue
            if other not in indeces:
                indeces.append(other)

        shuffle(indeces)
            
        title = Label(frame, text = words[correct], font = ('微软雅黑', 24))
        title.place(x = 320, y = 100, anchor = 'center')

        if not counts:
            counts = [0, 0]

        s1 = str(sum(counts))
        s0 = str(len(scope))
        s2 = str(counts[0])
        s3 = str(counts[1])

        count1 = Label(frame, text = s1 + ' / ' + s0 + ' shown - ')
        count2 = Label(frame, text = s2 + ' correct, ', fg = 'green')
        count3 = Label(frame, text = s3 + ' incorrect', fg = 'red')
        count1.place(x = 20, y = 20)
        count2.place(x = 95 + 5 * (len(s0) + len(s1)), y = 20)
        count3.place(x = 150 + 5 * (len(s0) + len(s1) + len(s2)), y = 20)
        
        options = []
        selected = [0]
        
        def sel_correct():

            if not selected[0]:
                selected[0] = 1
                familiarities[correct] += 1
                lasts[correct] = 0
                counts[0] += 1

                if familiarities[correct] == FAMILIAR_LINE:
                    update(1)
                else:
                    update(0)
                
                scr = familiarities[correct]
                text = 'Familiarity: ' + str(scr)
                if scr >= FAMILIAR_LINE:
                    score = Label(frame, text = text, fg = 'green')
                else:
                    score = Label(frame, text = text)
                score.place(x = 320, y = 140, anchor = 'center')
                options[cr].config(bg = 'palegreen')
                if len(not_shown) > 1:
                    def to_next():
                        frame.destroy()
                        show_next(lang, scope, data, counts, shown).tkraise()
                    frame.after(CORRECT_DELAY, to_next)
                else:
                    frame.after(CORRECT_DELAY, finished)
                
        def sel_wrong(i):

            if not selected[0]:
                
                if FAMILIAR_LINE <= familiarities[correct] < FAMILIAR_LINE * 2:
                    update(-1)
                else:
                    update(0)
                
                selected[0] = 1
                familiarities[correct] //= 2
                lasts[correct] = 1
                counts[1] += 1
                
                scr = familiarities[correct]
                text = 'Familiarity: ' + str(scr)
                if scr >= FAMILIAR_LINE:
                    score = Label(frame, text = text, fg = 'green')
                else:
                    score = Label(frame, text = text)
                score.place(x = 320, y = 140, anchor = 'center')
                options[i].config(bg = 'pink')
                options[cr].config(bg = 'palegreen')
                if len(not_shown) > 1:
                    def to_next():
                        frame.destroy()
                        show_next(lang, scope, data, counts, shown).tkraise()
                    frame.after(WRONG_DELAY, to_next)
                else:
                    frame.after(WRONG_DELAY, finished)

        items = []
        dy = [[], []]
        m = len(indeces)
        for i in range(m):
            items.append('')
            for j in range(len(categories[indeces[i]])):
                if categories[indeces[i]][j]:
                    items[-1] += categories[indeces[i]][j] + ' '
                l = 16
                items[-1] += meanings[indeces[i]][j] + '\n'
            items[-1] = items[-1][:-1]

            if indeces[i] == correct:
                cr = i
                options.append(Button(frame, text = items[i], justify = 'left', wraplength = 240,
                                      font = ('Comic Sans MS', 13), command = sel_correct))
            else:
                options.append(Button(frame, text = items[i], justify = 'left', wraplength = 240,
                                      font = ('Comic Sans MS', 13),
                                      command = lambda i = i: sel_wrong(i)))
            factor = (m+1) // 2
            options[i].place(x = 60 + 280 * (i // factor), y = 440 - 70 * (i % factor) - sum(dy[i // factor]),
                             anchor = 'sw')
            options[i].config(width = 24)
            dy[i // factor].append(items[-1].count('\n') * 25)
        
        '''next_word = Button(frame, text = 'Next', font = ('Comic Sans MS', 14),
                           command = lambda: show_next(lang, shown).tkraise())
        next_word.place(x = 520, y = 270)

        def show_next_key(event = None):
            show_next(lang, shown).tkraise()
        next_word.bind('<Return>', show_next_key)
        next_word.focus()'''
        
        marked = ImageTk.PhotoImage(Image.open(PATH + 'marked.png'))
        unmarked = ImageTk.PhotoImage(Image.open(PATH + 'unmarked.png'))

        def mark(click):
            marks[correct] = 1
            msg = Label(frame, text = 'Marked!', fg = 'orange', font = (THEME_FONT, 13))
            msg.place(x = 565, y = 150, anchor = 'center')
            msg.after(1000, msg.destroy)
            mark_lbl = Label(frame, image = marked)
            mark_lbl.place(x = 565, y = 110, anchor = 'center')
            mark_lbl.image = marked
            mark_lbl.bind('<ButtonRelease-1>', unmark)

        def unmark(click):
            marks[correct] = 0
            msg = Label(frame, text = 'Unmarked!', fg = 'blue', font = (THEME_FONT, 13))
            msg.place(x = 565, y = 150, anchor = 'center')
            msg.after(1000, msg.destroy)
            mark_lbl = Label(frame, image = unmarked)
            mark_lbl.place(x = 565, y = 110, anchor = 'center')
            mark_lbl.image = unmarked
            mark_lbl.bind('<ButtonRelease-1>', mark)

        if marks[correct]:
            mark_lbl = Label(frame, image = marked)
            mark_lbl.image = marked
            mark_lbl.bind('<ButtonRelease-1>', unmark)
        else:
            mark_lbl = Label(frame, image = unmarked)
            mark_lbl.image = unmarked
            mark_lbl.bind('<ButtonRelease-1>', mark)

        mark_lbl.place(x = 565, y = 110, anchor = 'center')
        
        exit_btn = Button(frame, text = 'Exit', font = ('Comic Sans MS', 14), bd = 2,
                       command = lambda: back_home().tkraise())
        exit_btn.place(x = 540, y = 20)

        frame.pack(fill = 'both', expand = True)
        
        return frame
    
    else:
        frame.destroy()
        return choose_scope(lang)

def show_word_list(lang_seln):

    lang = lang_seln.get(ACTIVE)

    if lang:

        wl_window = Toplevel()
        wl_window.title(lang + ' Word List')
        wl_window.geometry('580x480+20+80')

        frame = Frame(wl_window)

        f = open(PATH + lang + '.txt', 'r', encoding = 'utf-16')
        lines = []
        lines_display = []
        while True:
            line = f.readline()[:-1].split('\t')[:-1]
            if line:
                lines.append(line)
                i = 5
                while i < len(line) - 1:
                    l = [line[0], line[i], line[i+1], int(line[1]),
                         'Yes' if int(line[4]) else 'No']
                    lines_display.append(l)
                    i += 2
            else:
                break
        f.close()

        lines_display.sort()

        cols = ('word', 'category', 'explanation', 'familiarity', 'marked')
        table = ttk.Treeview(frame, columns = cols,
                             show = 'headings')
        
        ysb = ttk.Scrollbar(frame, orient = 'vertical', command = table.yview)
        table['yscroll'] = ysb.set

        table.grid(in_ = frame, row = 0, column = 0, sticky=NSEW)
        ysb.grid(in_ = frame, row = 0, column = 1, sticky=NS)

        table.rowconfigure(0, weight = 1)
        table.columnconfigure(0, weight = 1)

        for c in cols:
            table.heading(c, text = c.title())
        
        for i in range(len(lines_display)):
            table.insert('', 'end', values = lines_display[i])

        table.column('word', width = 100)
        table.column('category', width = 80)
        table.column('explanation', width = 220)
        table.column('familiarity', width = 90)
        table.column('marked', width = 60)

        style = ttk.Style(frame)
        style.configure('Treeview')
        table.configure(style = 'Treeview', height = 16)

        def sort(event):            
            region = table.identify("region", event.x, event.y)
            if region == 'heading':
                col = table.identify_column(event.x)
                col = int(col[1]) - 1
                rev = True
                for i in range(len(lines_display) - 1):
                    if lines_display[i][col] > lines_display[i+1][col]:
                        rev = False
                lines_display.sort(key = lambda x: x[col], reverse = rev)
                table.delete(*table.get_children())
                for j in range(len(lines_display)):
                    table.insert('', 'end', values = lines_display[j])
        
        table.bind('<ButtonRelease-1>', sort)
        
        def edit():

            search_etr.delete(0, 'end')
            selected = table.selection()

            if selected:
                
                for i in range(len(lines)):
                    if lines[i][0] == table.item(selected[0])['values'][0]:
                        line = lines[i]
                        break

                edit_window = Toplevel()
                edit_window.title('Edit')
                edit_window.geometry('420x420+20+80')

                title = Label(edit_window, text = 'Edit Word/Mark', font = ('Comic Sans MS', 18))
                title.place(x = 210, y = 70, anchor = 'center')

                label1 = Label(edit_window, text = 'Word: ', font = ('Comic Sans MS', 14))
                label1.place(x = 60, y = 120)

                def to_edit_vocab(key):
                    edit_vocab(word_etr.get(), v.get())
                
                word_etr = Entry(edit_window, bd = 2)
                word_etr.place(x = 180, y = 125)
                word_etr.config(width = 24)
                word_etr.insert(END, line[0])
                edit_window.bind('<Return>', to_edit_vocab)

                v = IntVar()
                mark_chb = Checkbutton(edit_window, text = 'Mark', variable = v, font = (THEME_FONT, 13), height = 3)
                mark_chb.place(x = 200, y = 160)
                if line[4] == 1:
                    mark_chb.select()

                def edit_vocab(wd, mk):

                    wd = remove_space(wd)
                    if not wd:
                        word_etr.config(bg = 'pink')
                        return

                    for ld in lines_display:
                        if ld[0] == line[0]:
                            if ld[0] != wd:
                                ld[0] = wd
                                ld[3] = str(int(ld[3] + 1) // 2)
                            ld[4] = 'Yes' if mk else 'No'

                    table.delete(*table.get_children())
                    
                    for j in range(len(lines_display)):
                        table.insert('', 'end', values = lines_display[j])

                    if line[0] != wd:
                        line[0] = wd
                        line[3] = datetime.strftime(datetime.now(), '%Y-%m-%d')
                        line[1] = (int(line[1]) + 1) // 2
                    line[4] = int(mk)
                    lines[i] = line

                    f = open(PATH + lang + '.txt', 'w', encoding = 'utf-16')
                    for l in lines:
                        for item in l:
                            f.write(str(item) + '\t')
                        f.write('\n')
                    f.close()

                    edit_window.destroy()
                
                input_btn = Button(edit_window, text = 'Confirm', font = ('Comic Sans MS', 14), bd = 3,
                                   command = lambda: edit_vocab(word_etr.get(), v.get()))
                input_btn.place(x = 210, y = 340, anchor = 'center')
                input_btn.config(width = 10)

                edit_window.focus()
                edit_window.mainloop()

        def mark():
            pass

        def delete():

            search_etr.delete(0, 'end')
            selected = table.selection()

            if selected:

                line = table.item(selected[0])['values']
            
                for l in lines_display:
                    if l == line:
                        break
                lines_display.remove(l)

                table.delete(*table.get_children())
                    
                for j in range(len(lines_display)):
                    table.insert('', 'end', values = lines_display[j])

                for l in lines:
                    i = 5
                    while i < len(l):
                        if (l[0], l[i]) == (line[0], line[1]):
                            del l[i]
                            del l[i]
                            if len(l) == 5:
                                lines.remove(l)
                            break
                        i += 2
                    else:
                        continue
                    break

                f = open(PATH + lang + '.txt', 'w', encoding = 'utf-16')
                for l in lines:
                    for item in l:
                        f.write(str(item) + '\t')
                    f.write('\n')
                f.close()
        
        def search(key, current, target, count):
            key_word = search_etr.get()
            if key_word:
                if key.keycode == 38 and target:
                    current = max(0, current - 1)
                    table.selection_set(target[current])
                    search_etr.bind('<Key>', lambda key: search(key, current, target, count))
                    search_count.config(text = 'result ' + str(current + 1) + ' / ' + str(count))
                elif key.keycode in (13, 40) and target:
                    if current == count - 1:
                        if key.keycode == 13:
                            current = 0
                    else:
                        current += 1
                    table.selection_set(target[current])
                    search_etr.bind('<Key>', lambda key: search(key, current, target, count))
                    search_count.config(text = 'result ' + str(current + 1) + ' / ' + str(count))
                elif key.keycode == 13:
                    count = 0
                    target = []
                    for l in table.get_children():
                        if key_word in table.item(l)['values'][0].lower() or key_word in table.item(l)['values'][2].lower():
                            target.append(l)
                            count += 1
                    search_etr.bind('<Key>', lambda key: search(key, 0, target, count))
                    if not count:
                        search_count.config(text = 'result 0 / 0')
                        table.selection_set()
                        return 
                    table.selection_set(target[0])
                    search_count.config(text = 'result ' + str(current + 1) + ' / ' + str(count))
                else:
                    target = []
                    current = 0
                    count = 0
                    search_etr.bind('<Key>', lambda key: search(key, current, target, count))
            else:
                search_count.config(text = 'result 0 / 0')
                table.selection_set()
            

        edit_btn = Button(wl_window, text = 'Edit Word', font = (THEME_FONT, 13),
                          command = edit)
        edit_btn.place(x = 20, y = 420)
        mark_btn = Button(wl_window, text = 'Mark', font = (THEME_FONT, 13),
                          command = mark)
        mark_btn.place(x = 140, y = 420)
        delete_btn = Button(wl_window, text = 'Delete Line', font = (THEME_FONT, 13),
                            command = delete)
        delete_btn.place(x = 200, y = 420)
        search_lbl = Label(wl_window, text = 'Search: ', font = (THEME_FONT, 13))
        search_lbl.place(x = 220, y = 20)
        search_etr = Entry(wl_window, bd = 2)
        search_etr.place(x = 300, y = 25)
        search_etr.config(width = 20)
        search_etr.bind('<Key>', lambda key: search(key, 0, [], 0))
        search_count = Label(wl_window, text = '')
        search_count.place(x = 550, y = 35, anchor = 'e')
            
        frame.pack(pady = 60)

        wl_window.focus()
        wl_window.mainloop()



PATH = os.getcwd() + '\\vocabber_storage\\'

window = Tk()
window.title('Vocabber')
window.geometry('640x480+20+20')

THEME_FONT = 'Comic Sans MS'

def home():

    global langs    
    global NUM_CHOICES
    global RECENT
    global FAMILIAR_LINE
    global CORRECT_DELAY
    global WRONG_DELAY
    global install_date
    
    if not os.path.exists(PATH):
        os.mkdir(PATH)
    
    try:
        NUM_CHOICES, RECENT, FAMILIAR_LINE, CORRECT_DELAY, WRONG_DELAY, install_date, langs, word_counts = read_initial()        
        now = datetime.now()
        day_count = (now - datetime.strptime(install_date, '%Y-%m-%d')).days
    except FileNotFoundError:
        install_date = datetime.now().strftime('%Y-%m-%d')
        f = open(PATH + 'initialize.txt', 'w', encoding = 'utf-16')
        f.write('6\n5\n4\n2000\n3000\n' + install_date + '\n')
        f.close()
        langs = []
        word_counts = []
        NUM_CHOICES = 6
        RECENT = 5
        FAMILIAR_LINE = 4
        CORRECT_DELAY = 2000
        WRONG_DELAY = 3000

    frame = Frame(window)

    title = Label(frame, text = 'Vocabber', font = (THEME_FONT, 26))
    title.place(x = 320, y = 70, anchor = 'center')

    text1 = Label(frame, text = 'Select a Language: ', font = (THEME_FONT, 14))
    text1.place(x = 35, y = 140)

    lang_seln = Listbox(frame, height = 8, width = 20,
                        selectmode = 'Single', selectbackground = 'blue')
    for lang in langs:
        lang_seln.insert(END, lang)
    lang_seln.place(x = 210, y = 145)
    lang_seln.focus()
    lang_seln.select_set(0)

    def move(key):
        lang_seln.select_clear(0, END)
        if key.keycode == 40:
            lang_seln.select_set(min(lang_seln.index(ACTIVE) + 1, len(langs) - 1))
        elif key.keycode == 38:
            lang_seln.select_set(max(lang_seln.index(ACTIVE) - 1, 0))
        else:
            lang_seln.select_set(ACTIVE)

    lang_seln.bind('<Key>', move)

    def to_input_vocab(lang):
        frame.destroy()
        return input_vocab(lang)

    def to_choose_scope(lang):
        frame.destroy()
        return choose_scope(lang)
    
    input_btn = Button(frame, text = 'Enter New Words', font = (THEME_FONT, 13), bd = 3,
                       command = lambda: to_input_vocab(lang_seln.get(ACTIVE)).tkraise())
    input_btn.place(x = 380, y = 140)

    quiz_btn = Button(frame, text = 'Vocab Quiz', font = (THEME_FONT, 13), bd = 3,
                      command = lambda: to_choose_scope(lang_seln.get(ACTIVE)).tkraise())
    quiz_btn.place(x = 380, y = 190)
    
    word_list_btn = Button(frame, text = 'Word List', font = (THEME_FONT, 13), bd = 3,
                           command = lambda: show_word_list(lang_seln))
    word_list_btn.place(x = 380, y = 240)

    rename_btn = Button(frame, text = 'Rename', font = (THEME_FONT, 13), bd = 3,
                        command = lambda: rename_lang(lang_seln))
    rename_btn.place(x = 380, y = 290)

    delete_btn = Button(frame, text = 'Delete', font = (THEME_FONT, 13), bd = 3,
                        command = lambda: delete_lang(lang_seln))
    delete_btn.place(x = 470, y = 290)

    text2 = Label(frame, text = 'Learning a new language?', font = (THEME_FONT, 14))
    text2.place(x = 60, y = 350)

    new_lang_etr = Entry(frame, bd = 2)
    new_lang_etr.place(x = 80, y = 410, anchor = 'w')
    new_lang_etr.config(width = 24)

    create_btn = Button(frame, text = 'Create', font = (THEME_FONT, 14), bd = 3,
                        command = lambda: create_lang(new_lang_etr, lang_seln))
    create_btn.place(x = 300, y = 410, anchor = 'w')

    def to_create_lang(key):
        create_lang(new_lang_etr, lang_seln)

    new_lang_etr.bind('<Return>', to_create_lang)

    def to_statistics():
        frame.destroy()
        return statistics()

    statistics_btn = Button(frame, text = 'Statistics', font = (THEME_FONT, 13), bd = 3,
                            command = lambda: to_statistics().tkraise())
    statistics_btn.place(x = 500, y = 75)

    settings_btn = Button(frame, text = 'Settings', font = (THEME_FONT, 13), bd = 3,
                            command = settings)
    settings_btn.place(x = 500, y = 25)

    return frame


home_frame = home()
home_frame.pack(fill = 'both', expand = True)

window.mainloop()
