############################################  NOTE  ########################################################
#
#           Reads the resumes folder and outputs a csv containing parsed file
#
############################################################################################################

import spacy
import glob
from converter import convert_pdf_to_text
from converter import convert_docx_to_text

class Parse():

    def __init__(self):
        nlp = spacy.load("./model")


        # Glob module matches certain patterns
        docx_files = glob.glob("resumes/*.docx")
        pdf_files = glob.glob("resumes/*.pdf")
        text_files = glob.glob("resumes/*.txt")

        files = set(docx_files + pdf_files + text_files)
        files = list(files)

        for f in files:
            # info is a dictionary that stores all the data obtained from parsing
            info = {}

            self.inputString, info['extension'] = self.readFile(f)
            info['fileName'] = f

            doc_to_test = nlp(self.inputString)
            print([(ent.text, ent.label_) for ent in doc_to_test.ents])
            print('--------')

    def readFile(self, fileName):
        '''
        Read a file given its name as a string.
        Modules required: os
        UNIX packages required: antiword, ps2ascii
        '''
        extension = fileName.split(".")[-1]
        if extension == "txt":
            f = open(fileName, 'r')
            string = f.read()
            f.close()
            return string, extension
        elif extension == "docx":
            try:
                return convert_docx_to_text(fileName), extension
            except:
                return ''
                pass
        elif extension == "pdf":
            try:
                return convert_pdf_to_text(fileName), extension
            except:
                return ''
                pass
        else:
            print
            'Unsupported format'
            return '', ''


if __name__ == "__main__":
    Parse()