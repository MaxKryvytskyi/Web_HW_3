import re
import os
import multiprocessing

translate_dict = {ord('а'):'a', ord('б'):'b', ord('в'):'v', ord('г'):'g', ord('д'):'d', ord('е'):'e', 
    ord('ё'):'yo', ord('ж'):'zh', ord('з'):'z', ord('и'):'i', ord('й'):'i', ord('к'):'k', ord('л'):'l', 
    ord('м'):'m', ord('н'):'n', ord('о'):'o', ord('п'):'p', ord('р'):'r', ord('с'):'s', ord('т'):'t', 
    ord('у'):'u', ord('ф'):'f', ord('х'):'h', ord('ц'):'c', ord('ч'):'ch', ord('ш'):'sh', ord('щ'):'sch', 
    ord('ъ'):'', ord('ы'):'y', ord('ь'):'', ord('э'):'e', ord('ю'):'u', ord('я'):'ya', ord('А'):'A', 
    ord('Б'):'B', ord('В'):'V', ord('Г'):'G', ord('Д'):'D', ord('Е'):'E', ord('Ё'):'YO', ord('Ж'):'ZH', 
    ord('З'):'Z', ord('И'):'I', ord('Й'):'I', ord('К'):'K', ord('Л'):'L', ord('М'):'M', ord('Н'):'N',
    ord('О'):'O', ord('П'):'P', ord('Р'):'R', ord('С'):'S', ord('Т'):'T', ord('У'):'U', ord('Ф'):'F', 
    ord('Х'):'H', ord('Ц'):'C', ord('Ч'):'CH', ord('Ш'):'SH', ord('Щ'):'SCH', ord('Ъ'):'', ord('Ы'):'y', 
    ord('Ь'):'', ord('Э'):'E', ord('Ю'):'U', ord('Я'):'YA', ord('ґ'):'', ord('ї'):'', ord('є'):'', 
    ord('Ґ'):'g', ord('Ї'):'i', ord('Є'):'e', ord(' '):'_'}

# Список Папок та розшинень може оновлятись
category_dict = {
    "Images":['jpeg', 'png', 'jpg', 'svg'],
    "Documents":['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx','rtf'],
    "Audio":['mp3', 'ogg', 'wav', 'amr'],
    "Video":['avi', 'mp4', 'mov', 'mkv'],
    "Archives":['zip', 'gz', 'tar'],
    "Exe":['exe'],
    "Python":['py'],
    "Html_css":['html', 'css'],
    "Others":[]
}

# Замінює кириліцю на латиницю
def normalize(text: str):
    file = text.rsplit('.', maxsplit=1)
    normal_text = file[0].translate(translate_dict)
    normal_text = re.sub(r"[^a-zA-Z0-9]", "_", normal_text)
    file[0] = normal_text
    text = '.'.join(file)
    return text

def get_cpu_count():
    try:
        # Вернуть количество доступных ядер CPU
        return os.cpu_count()
    except NotImplementedError:
        # Если os.cpu_count() не поддерживается, используйте multiprocessing.cpu_count()
        return multiprocessing.cpu_count()