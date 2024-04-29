'''Task 2 - get_cats_info()'''

from pathlib import Path

def get_cat_dict(cat_info_txt: str) -> dict:
    '''Convert cat_info_txt to cat_dict'''

    cat = cat_info_txt.split(",")
    cat_dict = {"id": cat[0], "name": cat[1], "age": cat[2]}

    return cat_dict

def get_cats_info(path: str) -> list:
    '''total_salary'''
    if Path(path).exists():
        with open(path, "r", encoding="utf-8") as fh:
            cat_list = [get_cat_dict(el.strip()) for el in fh.readlines()]
    else:
        raise FileNotFoundError("Invalid file path specified")

    return cat_list
