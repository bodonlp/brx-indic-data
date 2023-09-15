import tqdm
import os
wordnet_pairs=[
    "brx_asm",
    "brx_ben",
    "brx_guj",
    "brx_hin",
    "brx_kan",
    "brx_kas",
    "brx_kok",
    "brx_mal",
    "brx_mar",
    "brx_mni",
    "brx_nep",
    "brx_ori",
    "brx_pan",
    "brx_san",
    "brx_tam",
    "brx_tel",
    "brx_urd"
]
bpcc_lang_pairs = {
    "brx":"brx_Deva",
    "asm":"asm_Beng",
    "ben":"ben_Beng",
    "doi:":"doi_Deva",
    "gom":"gom_Deva",
    "guj":"guj_Gujr",
    "hin":"hin_Deva",
    "kan":"kan_Knda",
    "kas":"kas_Arab",
    "mai":"mai_Deva",
    "mal":"mal_Mlym",
    "mar":"mar_Deva",
    "mni_b":"mni_Beng",
    "mni":"mni_Mtei",
    "nep":"npi_Deva",
    "ori":"ory_Orya",
    "pan":"pan_Guru",
    "san":"san_Deva",
    "sat":"sat_Olck",
    "tam":"tam_Taml",
    "tel":"tel_Telu",
    "urd":"urd_Arab"
}

wordnet_path = "E:\\bpcc\\wordnet\\"
wordnet_data_path = "E:\\bpcc\\brx_indic\\wordnet\\"

for lp in wordnet_pairs:
    print(lp)
    lang_one = lp.split("_")[0]
    lang_two = lp.split("_")[1]
    files = ['dev','tst','val']
    for f in files:
        with open(wordnet_path+lp+'\\'+f+"."+lang_one, 'r', encoding="utf8") as ef, open(wordnet_path+lp+'\\'+f+"."+lang_two, 'r', encoding="utf8") as indfile:
            bodo = ef.readlines()
            indic = indfile.readlines()
            for bl, il in zip(bodo,  indic):
                bodo = bl.strip()
                indic_lang = il.strip()
                # write in wordnet data path if path not exists create path
                # if bpcc_lang_pairs[lang_two] exists in bpcc_lang_pairs then create path
                if lang_two in bpcc_lang_pairs:                        
                    pair = bpcc_lang_pairs[lang_one]+"-"+bpcc_lang_pairs[lang_two]
                    wordnet_data_path = "E:\\bpcc\\brx_indic\\wordnet\\"+pair+"\\"
                    if not os.path.exists(wordnet_data_path):
                        os.makedirs(wordnet_data_path)
                    with open(wordnet_data_path+"train."+bpcc_lang_pairs[lang_one], 'a', encoding="utf8") as bf, open(wordnet_data_path+"train."+bpcc_lang_pairs[lang_two], 'a', encoding="utf8") as ifile: 
                        bf.write(bodo+"\n")
                        ifile.write(indic_lang+"\n")
                else:
                    continue