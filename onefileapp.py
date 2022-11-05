from tkinter import *
from tkinter import ttk
import numpy as np
from numpy.linalg import norm
import pyttsx3
import speech_recognition as sr
import tkinter as tk
import tkinter.font as tkf
import threading

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def settt(stringgg):
    print("inside settt for "+stringgg)
    global lab1
    lab1.config(text="IT Assistant : "+stringgg)
    lab1.update()
    speak(stringgg)

def takeCommand():
    global lab1
    print("inside take command")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("inside with microphone")
        r.adjust_for_ambient_noise(source, duration=1)
        settt("*Listening*")
        print("after label")
        audio = r.listen(source)
        query=""
    try:
        lab1.config(text="IT Assistant : *Recognizing*")
        lab1.update()
        print("after label recog")
        query = r.recognize_google(audio, language='en-in')
        query=query.lower()

    except Exception as e:
        print(e)
        return "none"
    else:
        lab1.config(text="User : "+query)
        lab1.update()
        print("after setting query")
        return query

def core():
    global pb
    global main,mainl
    global sentence_embeddings,model,preprocess,dftemp
    import warnings
    import numpy as np
    warnings.filterwarnings("ignore")
    import pandas as pd
    main_df = pd.read_excel(r'.\df_withoutdup_final_origi1.xlsx')
    dftemp=main_df.copy()
    main_df_new = pd.DataFrame()
    main_df_new["combined data"] = "-"
    main_df_new["combined data"] = main_df["Subject"] + " " + main_df["Message"]
    main_df_new.head()
    pb['value']+=20
    mainl.config(text="Performing Preprocessing")
    main.update()
    import string
    import nltk
    import re
    from nltk.stem import WordNetLemmatizer
    from string import punctuation
    from nltk.corpus import stopwords

    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')

    def sent_tokens_func(text):
        return nltk.sent_tokenize(text)

    def word_tokens_func(text):
        return nltk.word_tokenize(text)  

    def to_lower(text):
        if not isinstance(text,str):
            text = str(text)
        return text.lower()

    def number_omit_func(text):
        output = ''.join(c for c in text if not c.isdigit())
        return output

    def remove_punctuation(text):
        return ''.join(c for c in text if c not in punctuation) 

    def stopword_remove_func(sentence):
        stop_words = stopwords.words('english')
        return ' '.join([w for w in nltk.word_tokenize(sentence) if not w in stop_words])

    def lemmatize(text):
            wordnet_lemmatizer = WordNetLemmatizer()
            lemmatized_word = [wordnet_lemmatizer.lemmatize(word)for word in nltk.word_tokenize(text)]
            return " ".join(lemmatized_word)

    def preprocess(text):
            lower_text = to_lower(text)
            sentence_tokens = sent_tokens_func(lower_text)
            word_list = []
            for each_sent in sentence_tokens:
                lemmatizzed_sent = lemmatize(each_sent)
                clean_text = number_omit_func(lemmatizzed_sent)
                clean_text = remove_punctuation(clean_text)
                clean_text = stopword_remove_func(clean_text)
                word_tokens = word_tokens_func(clean_text)
                for i in word_tokens:
                    word_list.append(i)
            return " ".join(word_list)
    pb['value']+=10
    mainl.config(text="Loading Transformer")
    main.update()
    sample_data = main_df_new['combined data']
    sample_data = sample_data.apply(preprocess)
    sample_data_new=main_df['Solution']
    sample_data_new = sample_data_new.apply(preprocess)
    main_df_new['preprocessed combined data'] = sample_data
    main_df['Solution']=sample_data
    main_df_new.to_csv("Preprocessed_data.csv",index=False)
    df_all_rows = pd.concat([main_df['Solution'],main_df_new],axis=1)
    df_all_rows.to_csv("Preprocessed__data.csv",index=False)

    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    pb['value']+=35
    mainl.config(text="Performing Encoding ... This May Take a While !")
    main.update()
    sentences=main_df_new['preprocessed combined data'].values.tolist()
    sentence_embeddings = np.array(model.encode(sentences))
    pb['value']+=35
    main.update()

def task():
    core()
    main.destroy()

main = Tk()
main.title("Loading ... Please Wait !")
mainl = Label(main, text="Loading Dataset")
mainl.grid(row=2,column=1,sticky="news",padx=10,pady=10)
pb = ttk.Progressbar(
    main,
    orient='horizontal',
    mode='determinate',
    length=280
)
pb.grid(row=1,column=1,sticky="news",padx=10,pady=10)
main.after(200, task)
main.mainloop()

def getsol(ssent,*args):
    global sentence_embeddings,model,preprocess,dftemp
    intext=ssent
    intext=preprocess(intext)
    intext_embedding=np.transpose(np.array(model.encode([intext])))
    cosine=np.dot(sentence_embeddings,intext_embedding)/(norm(sentence_embeddings,axis=1)*norm(intext_embedding))
    index = np.where(cosine == np.amax(cosine))
    index=list(index[0])
    settt(dftemp['Solution'][index[0]])  

def meow(*args):
    print("inside while loop")
    query=takeCommand()
    if query=="none":
        print("inside if")
        settt("Sorry, you were not audible.")
    else:
        print("inside else")
        getsol(query)
 
root = tk.Tk()
# root.attributes('-alpha',0.6)
root.attributes('-topmost', True)
root.overrideredirect(1)
root.geometry('600x500-500+200')
filename = tk.PhotoImage(file = "helpdesk.png")
fs=tkf.Font(family='Impact',size=11)
lab1 = tk.Label(root, text="",pady=50,wraplength=200,image=filename,compound=CENTER,font=fs,foreground='black')
lab1.pack()
root.bind('<space>',meow) 
root.bind('<Map>',settt("Hello, This is your personal IT help assistant! How may I help you? Press spacebar and tell your issues."))
root.mainloop() 