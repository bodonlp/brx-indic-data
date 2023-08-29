# conda activate py310
# python brx_indic_database_export.py
# Desktop Machine at Cabin

import mysql.connector
import hashlib
import tqdm
from dotenv import load_dotenv
load_dotenv()
import os
password = os.getenv("PASSWORD")

mydb = mysql.connector.connect(
  host="localhost",
  user="sn",
  password=password,
  database="bpcc"
)
mycursor = mydb.cursor()
domains=['daily','ilci','wiki']
lang_pair = "eng_Latn-brx_Deva"
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
    bodo_path = indic_path + domain + "\\" + lang_pair + "\\train.brx_Deva"
    english_path = indic_path + domain + "\\" + lang_pair + "\\train.eng_Latn"
    with open(bodo_path, 'r', encoding="utf8") as f, open(english_path, 'r', encoding="utf8") as e:
        bodo = f.readlines()
        english = e.readlines()
        # use tqdm to get progress bar
        for i in tqdm.tqdm(range(len(bodo))):
            brx = bodo[i].strip()
            eng = english[i].strip()
            insert_indic(eng, eng, brx)
        

