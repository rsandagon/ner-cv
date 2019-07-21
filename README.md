# NLP - NER using Spacy

NLP Studies with CV Parsing

### Training
* Run `python train.py` . This will create the `model` folder
* Run `python -m spacy package model models` to create package versions of the model
* To build tar gz of the mode, go inside the specific folder (e.g. en_model-0.0.0), and rung `python setup.py sdist`

### Loading Model
* Run `pip install /path/to/en_model-0.0.0.tar.gz` to install the model.
* You may now load the model by importing it or calling it with `spacy.load("en")`.

### Parsing Documents
* Run `python parse.py` to parse resume files inside the resumes folder.


##References:
* [Machine Learning](https://medium.com/tag/machine-learning?source=post)
* [NLP](https://medium.com/tag/nlp?source=post)
* [Named Entity
Recognition](https://medium.com/tag/named-entity-recognition?source=post)
