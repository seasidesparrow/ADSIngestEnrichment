import json
from adsenrich.references import ReferenceWriter

with open('./jats_iop_apj_923_1_47.json', 'r') as fin:
    record = json.load(fin)


lol = ReferenceWriter(data=record, 
                      reference_directory="./ref_test/",
                      reference_source="iop")
lol.write_references_to_file()

