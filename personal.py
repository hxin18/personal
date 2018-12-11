import sys
import nltk
import regex as re

def nltk_pos_tag(text):
    '''
    @input text: a sentence to determine its personality
    @return its personality
    '''

    #create a dictionary
    mapping ={}
    mapping["i"] = "first, single"
    mapping["my"] = "first, single"
    mapping["we"] = "first, plural"
    mapping["our"] = "first, plural"
    mapping["you"] = "first"
    mapping["your"] = "first"
    mapping["they"] = "third, plural"
    mapping["their"] = "third, plural"

    #remove all quote
    pattern = r'"(.*?)"'
    text = re.sub(pattern,"",text)
    text = text.split()

    #find all pronouns
    prp = [x[0] for x in nltk.pos_tag(text) if x[1] in ["PRP","PRP$"]]
    if len(prp)>0:
        prp_first = prp[0]
    else:
        prp_first = ""
    if prp_first.lower() in mapping:
        return mapping[prp_first.lower()]
    return "third"

def main():
    if len(sys.argv)<2:
        print("usage:python personal.py -s sentance\npython personal.py -f filename")
        return
    op = sys.argv[1]
    if op == "-s":
        sentance = " ".join(sys.argv[2:])
        if len(sentance)  == 0:
            print("Invalid input\nusage:python personal.py -s sentance\npython personal.py -f filename")
        else:
            print("This sentence is written in the personality of '"+nltk_pos_tag(sentance)+"'.")
    elif op =="-f":
        if sys.argv[2]:
            flg = False
            with open(sys.argv[2],"r") as f:
                for line in f:
                    if len(line)>0:
                        flg = True
                        print("This sentence is written in the personality of '"+nltk_pos_tag(line)+"'.")
            if not flg:
                print("Invalid input\nusage:python personal.py -s sentance\npython personal.py -f filename")
        else:
            print("Invalid input\nusage:python personal.py -s sentance\npython personal.py -f filename")
    else:
        print("Invalid input\nusage:python personal.py -s sentance\npython personal.py -f filename")
        

if __name__ == "__main__":
    main()