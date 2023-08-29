# conda activate py310
# python brx_indic_database_export.py
# Desktop Machine at Cabin

import mysql.connector
import hashlib
import tqdm
import os
from dotenv import load_dotenv

load_dotenv('.env')
password = os.getenv('PASSWORD')

mydb = mysql.connector.connect(
  host="localhost",
  user="sn",
  password=password,
  database="bpcc"
)
mycursor = mydb.cursor()
domains=['daily','ilci','wiki']
lang_pair = "eng_Latn-brx_Deva"
lang_one = lang_pair.split("-")[0]
lang_two = lang_pair.split("-")[1]
indic_path = "E:\\bpcc\\"
def insert_indic(hash_val, eng, indic_lang):
    sql = "INSERT INTO brx_indic (hash, eng, brx) VALUES (%s, %s, %s)"
    
    hash = hashlib.sha256(hash_val.encode('utf-8')).hexdigest()
    eng = eng
    indic_lang = indic_lang
    val = (hash, eng, indic_lang)
    mycursor.execute(sql, val)
    
    mydb.commit()
def update_indic(hash_val, eng, indic_lang):
    sql = "UPDATE brx_indic SET asm = %s WHERE hash = %s AND eng = %s"
    
    hash = hashlib.sha256(hash_val.encode('utf-8')).hexdigest()
    eng = eng
    indic_lang = indic_lang
    val = (indic_lang, hash, eng)
    mycursor.execute(sql, val)
    
    mydb.commit()
for domain in domains:
    english_path = indic_path + domain + "\\" + lang_pair + "\\"  + lang_one
    indic_lang_path = indic_path + domain + "\\" + lang_pair + "\\"+ lang_two
    with open(indic_lang_path, 'r', encoding="utf8") as f, open(english_path, 'r', encoding="utf8") as e:
        bodo = f.readlines()
        english = e.readlines()
        # use tqdm to get progress bar
        for i in tqdm.tqdm(range(len(bodo))):
            brx = bodo[i].strip()
            eng = english[i].strip()
            # for newly created database
            #insert_indic(eng, eng, brx)
            # for updating database
            update_indic(eng, eng, brx)
        

