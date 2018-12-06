import os,sys

print("Epub To Kindle Mobi")
print("Created by Hakono")
print()
if len(sys.argv) <2:
    print("请传入要转换的书籍目录！")
    input()
    os._exit(0)

print("待转换的文件：")
epubs = sys.argv[1:]

for epub_path in epubs:
    print(epub_path)
print()
print("**************开始转换**************")
for idx,epub_path in enumerate(epubs):
    print("%d. 开始转换: %s" % (idx+1,epub_path))
    if not os.path.exists(epub_path):
        print("此文件不存在")
        continue
    status =  os.system('kindlegen.exe "%s"' % epub_path)

    epub_file_name = os.path.basename(epub_path)
    epub_dir_path = os.path.dirname(epub_path)
    mobi_file_name = os.path.splitext(epub_path)[0] + ".mobi"
    mobi_file_path = os.path.join(epub_dir_path,mobi_file_name)

    print("epub转换完成，新mobi文件：%s" % mobi_file_path)
    print("开始为epub瘦身...")
    before_size = os.path.getsize(mobi_file_path)/1024/1024
    status = os.system('kindlestrip.exe "%s" "%s"' % (mobi_file_path,mobi_file_path))
    after_size = os.path.getsize(mobi_file_path)/1024/1024
    print("瘦身完成：%.1fMB -> %.1fMB" %(before_size,after_size))
    print("转换完成")
    print()


