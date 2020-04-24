import os
import shutil
import sys
import urllib3

factorio_stable = "https://factorio.com/get-download/stable/headless/linux64" # url to download latst-stable for future implementation
factorio_path = input('Specify Factorio path ex. \n "/home/user/factorio/" --> ')  # get factorio path
try:
    os.chdir(factorio_path)
except Exception as e:
    print("Path not found: " + factorio_path)
    print(e)
factorio_version = input('Factorio version \n ex. "0.18.xx" --> ')  # get factorio version
path_file = factorio_path+factorio_version
print("Factorio path : " + factorio_path)
print("Factorio version : " + factorio_version)
print("Temp folder : " + path_file)

factorio_latestexperimental = "https://factorio.com/get-download/" + factorio_version + "/headless/linux64"
http = urllib3.PoolManager()
resp = http.request('GET', factorio_latestexperimental, preload_content=False)
with open(factorio_path + "/linux64", 'wb') as out:
    while True:
        data = resp.read(2048)
        if not data:
            break
        out.write(data)
resp.release_conn()
#temp dir to move all extracted data /home/user/factorio/0.xx.xx/
try:
    os.mkdir(path_file)
    shutil.unpack_archive(factorio_path + "linux64", path_file, "tar")
except OSError:
    print("Creation of the directory %s failed" % path_file)
else:
    print("Successfully created the directory %s " % path_file)
path = ["/factorio/bin/","/factorio/data/","/factorio/config-path.cfg"]
for x in path:
    abs_path = path_file + x
    dest = shutil.move(abs_path, factorio_path)
    print("Destination path:", dest)
try:
    os.remove(factorio_path+"/linux64")
    shutil.rmtree(path_file)
except OSError as e:
    print("Error: %s : %s" % (path_file, e.strerror))


