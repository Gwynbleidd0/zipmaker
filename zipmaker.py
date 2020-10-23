import argparse
import zipfile
import os
import sys
import shutil



#Функция архивации самой папки и всех вложенных в нее папок и файлов
def zipper(name):
    new_zip = zipfile.ZipFile(f'zipped/{name}.zip', 'w')
    for folder, dirs, files in os.walk(name):
        if files != []:
            for file in files:
                if dirs != '':
                    new_zip.write(
                        os.path.join(folder, file),
                        os.path.relpath(os.path.join(folder,file)),
                        compress_type = zipfile.ZIP_DEFLATED)
        else:
            for i in dirs:
                new_zip.write(
                    os.path.relpath(os.path.join(folder,i)),
                    compress_type = zipfile.ZIP_DEFLATED)
    new_zip.close()

#Получаем путь из аргумента, иначе используем текущую директорию
try:
    path = os.path.join(os.getcwd(),sys.argv[1])
except:
    path = '.'


#Переходим в нужную директорию
try:
    os.chdir(path)
    #Проверяем, есть ли папка zipped. Иначе создаем. 
    if not os.path.exists('zipped'):
        os.mkdir('zipped')
    #Обходим все папки и архивируем их
    for i in os.listdir(path):
        if os.path.isdir(i) and i != 'zipped':
            zipper(i)
            shutil.rmtree(i)
except FileNotFoundError:
    print('Пожалуйста, введите подходящий путь')
except PermissionError:
    print('Отказано в доступе')
except Exception:
    print(Exception)

    



    
    