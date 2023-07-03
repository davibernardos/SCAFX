## CONSTANTS: PATH SETTINGS
## ------------------------------
ROOT_INPUT = "db-input"
ROOT_OUTPUT = "db-output"
ROOT_TREE = "images/"
OUTPUT_FILE = "csv-output-extrator.csv"

## CONSTANTS: CLUSTERING SETTINGS
## ------------------------------
METRIC = "euclidean"
METHOD = "average"

## CONSTANTS: INPUT SETTINGS
## ------------------------------
LS_TYPES = ['void', 'int', 'long', 'float', 'double', 'char']

## CONSTANTS: LEARNING TOPICS
## ------------------------------
T1 = "Lista01"
T2 = "Lista02"
T3 = "Lista03"
T4 = "Lista04"
T5 = "Lista05"

## CONSTANTS: CLASSROOM
## ------------------------------
C1 = "T1"
C2 = "T2"
C3 = "T3"

## CONSTANTS: CLASSROOM
## ------------------------------
LS_GROUPS = ['GA', 'GB', 'GC', 'GD']

## CONSTANTS: COLUMN NAMES
## ------------------------------
COLUMN_NAMES = {
    T1: ['NF', 'NP', 'NC', 'NR'],
    T2: ['NPt_s', 'NAdd_s', 'NPt_ds', 'NAdd_ds'],
    T3: ['NStr', 'NStrM', 'NStrT', 'NStrI', 'NStrC'],
    T4: ['NFRec', 'NCRec', 'NIFPar', 'NRRec', 'NRNRec'],
    T5: ['NSizeof', 'NMalloc', 'NFree']
}