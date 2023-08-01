pip install python-lei
from python_lei.lei_search import SearchLEI
search_possible_lei = SearchLEI()
raw_data, table = search_possible_lei.search_lei("Apple INC.", show_table=True)
print(table)
print(raw_data)
[{'LegalName': 'APPLE INC.', 'LEI': 'HWUPKR0MPOU8FGXBT394'}]
