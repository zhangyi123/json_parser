#!/usr/bin/env python

"""Clean comment text for easier parsing."""

from __future__ import print_function

import re
import string
import argparse

import subprocess

__author__ = ""
__email__ = ""

# Some useful data.
_CONTRACTIONS = {
    "tis": "'tis",
    "aint": "ain't",
    "amnt": "amn't",
    "arent": "aren't",
    "cant": "can't",
    "couldve": "could've",
    "couldnt": "couldn't",
    "didnt": "didn't",
    "doesnt": "doesn't",
    "dont": "don't",
    "hadnt": "hadn't",
    "hasnt": "hasn't",
    "havent": "haven't",
    "hed": "he'd",
    "hell": "he'll",
    "hes": "he's",
    "howd": "how'd",
    "howll": "how'll",
    "hows": "how's",
    "id": "i'd",
    "ill": "i'll",
    "im": "i'm",
    "ive": "i've",
    "isnt": "isn't",
    "itd": "it'd",
    "itll": "it'll",
    "its": "it's",
    "mightnt": "mightn't",
    "mightve": "might've",
    "mustnt": "mustn't",
    "mustve": "must've",
    "neednt": "needn't",
    "oclock": "o'clock",
    "ol": "'ol",
    "oughtnt": "oughtn't",
    "shant": "shan't",
    "shed": "she'd",
    "shell": "she'll",
    "shes": "she's",
    "shouldve": "should've",
    "shouldnt": "shouldn't",
    "somebodys": "somebody's",
    "someones": "someone's",
    "somethings": "something's",
    "thatll": "that'll",
    "thats": "that's",
    "thatd": "that'd",
    "thered": "there'd",
    "therere": "there're",
    "theres": "there's",
    "theyd": "they'd",
    "theyll": "they'll",
    "theyre": "they're",
    "theyve": "they've",
    "wasnt": "wasn't",
    "wed": "we'd",
    "wedve": "wed've",
    "well": "we'll",
    "were": "we're",
    "weve": "we've",
    "werent": "weren't",
    "whatd": "what'd",
    "whatll": "what'll",
    "whatre": "what're",
    "whats": "what's",
    "whatve": "what've",
    "whens": "when's",
    "whered": "where'd",
    "wheres": "where's",
    "whereve": "where've",
    "whod": "who'd",
    "whodve": "whod've",
    "wholl": "who'll",
    "whore": "who're",
    "whos": "who's",
    "whove": "who've",
    "whyd": "why'd",
    "whyre": "why're",
    "whys": "why's",
    "wont": "won't",
    "wouldve": "would've",
    "wouldnt": "wouldn't",
    "yall": "y'all",
    "youd": "you'd",
    "youll": "you'll",
    "youre": "you're",
    "youve": "you've"
}

# You may need to write regular expressions.

def sanitize(text):
    """Do parse the text in variable "text" according to the spec, and return
    a LIST containing FOUR strings 
    1. The parsed text.
    2. The unigrams
    3. The bigrams
    4. The trigrams
    """

    # YOUR CODE GOES BELOW:

    
    #decode
    L=[]
    parse=""
    uni=""
    bi=""
    tri=""
    text=text.decode("utf-8")
    text=text.encode('ascii', 'ignore')
    text=text.decode("utf-8")
    text=text.replace("\\n", " ")
    text=text.replace("\\t", " ")
    text = re.sub('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '', text)#good
    text=' '.join(text.split()) #3

        #4
    text=re.sub(',',' ,',text)
    text=re.sub('\.',' .',text)
    text=re.sub(';',' ;',text)
    text=re.sub('\?',' ?',text)
    text=re.sub('\!',' !',text)
        #i=re.sub('\...',' ...',i)

        #5
    text=re.sub("[^\w\d'\s\.,-;?!:]+",'',text)
    text=text.lower()
    parse+=text
    if len(parse)!=0 and parse[-1]==' ':
        parse=parse[:-1]

        #for uni
    text=re.sub("[^\w\d\s]+",'',text)
    text=' '.join(text.split()) #3
    for each_key in _CONTRACTIONS:
        #text=text.replace(" "+each_key+" "," "+_CONTRACTIONS[each_key]+" ")
          
        text= re.sub(r"\b" + re.escape(each_key) +r"\b"  , _CONTRACTIONS[each_key], text)


    uni+=text

        #for bi
    split=parse.split()
    length=len(split)

    str_bi=""

    last=length-1
    last_second=last-1
    temp=0

    while temp<=last_second:
        if split[temp]=='.' or split[temp]==',' or split[temp]=='-' or split[temp]==';' or split[temp]=='?' or split[temp]=='!' or split[temp]==':':
            temp+=1
            continue            
        else:
            if split[temp+1]=='.' or split[temp+1]==',' or split[temp+1]=='-' or split[temp+1]==';' or split[temp+1]=='?' or split[temp+1]=='!' or split[temp+1]==':':
                temp+=1
                continue
            else:
                str_bi+= (split[temp]+"_"+split[temp+1]+" ") 
        temp+=1
    

        #for tri
    last_thrid=last-2
    temp=0
    str_tri=""
    while temp<=last_thrid:
        if split[temp]=='.' or split[temp]==',' or split[temp]=='-' or split[temp]==';' or split[temp]=='?' or split[temp]=='!' or split[temp]==':' or split[temp+1]=='.' or split[temp+1]==',' or split[temp+1]=='-' or split[temp+1]==';' or split[temp+1]=='?' or split[temp+1]=='!' or split[temp+1]==':'        or split[temp+2]=='.' or split[temp+2]==',' or split[temp+2]=='-' or split[temp+2]==';' or split[temp+2]=='?' or split[temp+2]=='!' or split[temp+2]==':':
            temp+=1
            continue
        else:
            str_tri+= (split[temp]+"_"+split[temp+1]+"_"+split[temp+2]+" ")
            temp+=1

    if len(str_bi)!=0 and str_bi[-1]==' ':
        str_bi=str_bi[:-1]
    if len(str_tri)!=0 and str_tri[-1]==' ':
        str_tri=str_tri[:-1]
    parsed_text=parse
    unigrams=uni
    bigrams=str_bi
    trigrams=str_tri
    return [parsed_text, unigrams, bigrams, trigrams]


if __name__ == "__main__":
    # This is the Python main function.
    # You should be able to run
    # python cleantext.py <filename>
    # and this "main" function will open the file,
    # read it line by line, extract the proper value from the JSON,
    # pass to "sanitize" and print the result as a list.

    # YOUR CODE GOES BELOW.
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()
    #a= subprocess.check_output(['jq','.body',args.file.name]).splitlines()
    a = subprocess.Popen(['jq','.body',args.file.name], stdout=subprocess.PIPE)
    for line in a.stdout:

        print (sanitize(line))


    # for i in a:
    #     print (sanitize(i))

#sanitize(text);
