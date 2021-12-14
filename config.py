import os.path



###############################################################################
###############################################################################
###############################################################################
# IP-Adresses:
# The IP-Adresses to other known modules.
EXTRACTION_MODULE_API = {
    "BASEURI" : "http://127.0.0.1:8002",
    "send_to": "/extraction/transform_pdf_to_data",
    "has_results": "/extraction/has_extraction/?document_id=",
    "get_results": "/extraction/get_task_extraction/?document_id="
                         }
ANNOTATION_MODULE_API = {
    "BASEURI" : "http://127.0.0.1:8003",
    "send_to": "/annotation/extract_annotations",
    "has_results": "/annotation/has_results/?document_id=",
    "get_results": "/annotation/get_task_results/?document_id="
                         }
ANALYSIS_MODULE_API = {
    "BASEURI" : "http://127.0.0.1:8007",
    "send_to": "/api/contextualize_data",
    "has_results": "/analysis/has_results/?document_id=",
    "get_results": "/annotation/get_full_logs/?document_id="
                         }

###############################################################################
###############################################################################
###############################################################################
# Database:
# These are the folders where the files will be saved.
# 
DATABASE_FOLDERS = {
            'upload': 'uploaded',
            'extract': 'extracted',
            'annotate': 'annotated',
            'analyse': 'analysed',
            'question_template': 'question_templates',
            'triple_template': 'triple_templates'
        }

###############################################################################
###############################################################################
###############################################################################
# Indexs:
# The Indexs are part of the database. These helps to identify fast different 
# documents

DATABASE_INDEX_PATHS = {
            'upload': 'indexes/uploaded.json',
            'extract': 'indexes/extracted.json',
            'annotate': 'indexes/annotated.json',
            'analyse': 'indexes/analysed.json',
            'question_template': 'indexes/question_templates.json',
            'triple_template': 'indexes/triple_templates.json'
        }

##################
# Paths

PATH_TO_APP = os.path.abspath(__file__).replace("config.py", "")
# DATABASE_INDEX_PATHS = {type: os.path.join(PATH_TO_APP, rel_path) for type, rel_path in database_folders.items()}
DATABASE_MAIN_PATH = os.path.join(PATH_TO_APP, "database/files")
PATH_TO_TMP = os.path.join(PATH_TO_APP, "static/tmp")
PATH_TO_QUESTIONTEMPLATE = os.path.join(PATH_TO_APP, "files/question_templates.json")
PATH_TO_TRIPLEFILE = os.path.join(PATH_TO_APP, "files/test_triple.txt")