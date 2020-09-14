import os

def filePath(fileDir = 'data', fileName = 'login.yaml'):
    path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(path, fileDir, fileName)
