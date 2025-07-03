# Article parser from Metanit.com

## Description

Application for automatic parsing of article texts from the metanit.com website for their subsequent processing using neural networks.

## Functionality

Works in 2 modes:
1) Parsing a topic
2) Parsing a single page

## Technologies

Language: Python
Framework: tkinter

## Installation and launch

1. Deploy the environment and install dependencies
```
python -m venv venv # create an environment
.\venv\Scripts\activate # activate (Windows)
pip install -r requirements.txt
```

2. Launch the application
```
python script.py
```

## User Guide

#### Fields
- `Link to table of contents`: link to the table of contents page of the topic that needs to be downloaded.
- `Single link`: (single mode) link to the article
- `Single file name`: (single mode) what name to use for the files
- `Save path`: directory for saving articles
- `Additional file path`: directory for saving template files, where the article text will be inserted after AI processing.
- `Header`: Text to insert at the beginning of the article file.
- `Footer`: Text to insert at the end of the article file.
- `Additional file header`: Text to insert at the beginning of the template file.
- `Additional file footer`: Text to insert at the end of the template file.

**Service fields:**
- `Chapter block selector`: CSS selector of the div block of the table of contents page containing the link to the article.
- `Chapter title selector`: CSS selector of the block with the link text, for parsing the article title. (added to the chapter block selector)
- `Link selector`: CSS selector to get a link to the article (added to the chapter block selector)
- `Filtering (reg. expressions)`: Regular expressions to remove uninformative text.
- `Replacement list`: Text pairs (find -> replace), mainly needed for escaping characters.
- `Content filtering selectors`: Filtered blocks when parsing an article.

---
1. Depending on the mode, fill in the required fields:
- Topic mode: Link to the table of contents
- Single page mode: Single link and Name of a single file
2. Also fill in the Save path (where the files will be saved), Path for an additional file (blanks for inserting articles after they are processed by the neural network).
3. If necessary, you can specify your own headers and footers for both files.
4. The finished configuration can be saved to load from the file next time.
5. When everything is ready, click Run. The progress of the process will be displayed in the lower logging window.

![](./_/Pasted%20image%2020250527163929.png)
