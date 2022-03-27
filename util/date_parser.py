

def parse(date: str):

    date_ojb = date.split('-')
    try:
        year = date_ojb[0]
        month = date_ojb[1]
        day = date_ojb[2]
    except Exception:
        return ' ' * 8
    return  f'{day}{month}{year}'
