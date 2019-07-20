############################################  NOTE  ########################################################
#
#           Creates NER training data in Spacy format from JSON downloaded from Dataturks.
#
#           Outputs the Spacy training data which can be used for Spacy training.
#
############################################################################################################

import spacy
from convertPDFToText import convertPDFToText
from convertDocxToText import convertDocxToText

def parse():

    nlp = spacy.load("/model")

    #f = open("sample.txt", "r")
    doc_to_test = nlp("Ryan Sandagon Successfully managed ~20 React Js programmer.")
    print([(ent.text, ent.label_) for ent in doc_to_test.ents])


parse()
