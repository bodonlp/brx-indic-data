# conda activate py310
# python brx_indic_database_export.py
# Desktop Machine at Cabin

import hashlib
import tqdm
import os
domains=['daily','ilci','wiki']
lan_pairs = [
    "eng_Latn-brx_Deva",
    "eng_Latn-asm_Beng",
    "eng_Latn-ben_Beng",
    "eng_Latn-doi_Deva",
    "eng_Latn-gom_Deva",
    "eng_Latn-guj_Gujr",
    "eng_Latn-hin_Deva",
    "eng_Latn-kan_Knda",
    "eng_Latn-kas_Arab",
    "eng_Latn-mai_Deva",
    "eng_Latn-mal_Mlym",
    "eng_Latn-mar_Deva",
    "eng_Latn-mni_Beng",
    "eng_Latn-mni_Mtei",
    "eng_Latn-npi_Deva",
    "eng_Latn-ory_Orya",
    "eng_Latn-pan_Guru",
    "eng_Latn-san_Deva",
    "eng_Latn-sat_Olck",
    "eng_Latn-tam_Taml",
    "eng_Latn-tel_Telu",
    "eng_Latn-urd_Arab"
]

indic_path = "E:\\bpcc\\"
brx_indic_path = "E:\\bpcc\\brx_indic\\"
brx_eng_dict = {}
for domain in domains:
    # print tqdm progress bar for domains
    print(domain)

    for pair in lan_pairs:
        lang_one = pair.split("-")[0]
        lang_two = pair.split("-")[1]
        # check directory exists
        if not os.path.exists(indic_path + domain + "\\" + pair):
            continue
        english_path = indic_path + domain + "\\" + pair + "\\train."  + lang_one
        indic_lang_path = indic_path + domain + "\\" + pair + "\\train."+ lang_two
        with open(indic_lang_path, 'r', encoding="utf8") as f, open(english_path, 'r', encoding="utf8") as e:
            
            english = e.readlines()
            indic = f.readlines()
            # if brx_Deva and eng_Latn store in a dictionary
            if pair == 'eng_Latn-brx_Deva':
                for i in tqdm.tqdm(range(len(english))):
                    brx = indic[i].strip()
                    eng = english[i].strip()
                    brx_eng_dict[eng] = brx

            else:
                for i in tqdm.tqdm(range(len(english))):
                    ind = indic[i].strip()
                    eng = english[i].strip()
                    # if eng is brx_eng_dict then get the brx_Deva value

                    if eng in brx_eng_dict:
                        brx = brx_eng_dict[eng]
                        # write to file
                        # if brx_indic path exists then write to file
                        if os.path.exists(brx_indic_path + domain + "\\" + 'brx_Deva-'+lang_two):
                            with open(brx_indic_path + domain + "\\" + 'brx_Deva-'+lang_two + "\\train.brx_Deva", 'a', encoding="utf8") as bfile:
                                bfile.write(brx + "\n")
                            with open(brx_indic_path + domain + "\\" + 'brx_Deva-'+lang_two + "\\train."+ lang_two, 'a', encoding="utf8") as ifile:
                                ifile.write(ind + "\n")
                        else:
                            #create ditrectory and write to file
                            os.makedirs(brx_indic_path + domain + "\\" + 'brx_Deva-'+lang_two)
                            with open(brx_indic_path + domain + "\\" + 'brx_Deva-'+lang_two + "\\train.brx_Deva", 'a', encoding="utf8") as bfile:
                                bfile.write(brx + "\n")
                            with open(brx_indic_path + domain + "\\" + 'brx_Deva-'+lang_two + "\\train."+ lang_two, 'a', encoding="utf8") as ifile:
                                ifile.write(ind + "\n")
                    else:
                        continue
