import yaml
from common.public import filePath

class operateYaml():
    def readYaml(self):
        with open(filePath(), 'r', encoding= 'utf-8') as f:
            return list(f)
    def dictYaml(self):
        with open(filePath(fileDir= 'config', fileName= 'config.yaml'), 'r', encoding= 'utf-8') as f:
            return f
