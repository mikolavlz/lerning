


class ParserDoc:
    @staticmethod
    def parce(filename):
        return NotImplementedError

class ParcerJSON(ParserDoc):
    @staticmethod
    def parce(filename):
        print('Здесь парсим ждейсон')

class ParcerXML(ParserDoc):
    @staticmethod
    def parce(filename):
        print('Здесь парсим XML')

class Parcer:
    @classmethod
    def open(cls,filename):
        ext = filename.split('.')[-1]
        if ext == "xml":
            parcer = ParcerXML
        elif ext == "json":
            parcer = ParcerJSON
        else:
            raise RuntimeError('Невозможно определит ьформат файла')

        obj = parcer.parce(filename)

Parcer.open('pars.json')