import json
import os
from os.path import getsize, join


def update_stats():
    path = 'C:\\Users\\user\\PycharmProjects\\flask-1\\static\\upload'
    total_imgs_size = 0
    total_files_size = 0
    total_files = 0
    total_imgs = 0
    for root, dirs, files in os.walk(path):
        if root == join(path, 'files'):
            total_files = len(files)
            total_files_size += sum([getsize(join(root, name)) for name in files])
            total_files_size = round(total_files_size / (1024 * 1024), 2)
        if root == join(path, 'imgs'):
            total_imgs = len(files)
            total_imgs_size += sum([getsize(join(root, name)) for name in files])
            total_imgs_size = round(total_imgs_size / (1024 * 1024), 2)

    total_files = str(total_files) + '个'
    total_files_size = str(total_files_size) + 'MB'
    total_imgs = str(total_imgs) + '个'
    total_imgs_size = str(total_imgs_size) + 'MB'
    f = open('static/stats.txt', 'w', encoding='UTF-8')
    s = {"total_imgs_size": total_imgs_size, "total_files_size": total_files_size, "total_imgs": total_imgs,
         "total_files": total_files}
    s = json.dumps(s, ensure_ascii=False)
    f.write(s)
    f.close()


if __name__ == '__main__':
    update_stats()
