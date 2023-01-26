import pickle
import os

from DataStorage.ADataStoreBase import DataStoreBase
from DataStorage.AUtils import get_exception_printable_string
from DataStorage.Result import Result


class ADataStore(DataStoreBase):
    BACKUP_EXTENSION = '.BAK'
    _storage = None
    _storageFilePath = None

    def __init__(self, storageFilePath: str):
        super().__init__()
        self._lastError = None
        self._storageFilePath = storageFilePath
        self._storage = dict()
        self._fileName = os.path.basename(storageFilePath)
        dirName = os.path.dirname(self._storageFilePath)
        if not os.path.isdir(dirName): os.makedirs(dirName)

    def Save(self) -> Result:
        try:
            if os.path.exists(self._storageFilePath):
                if os.path.exists(self._storageFilePath + self.BACKUP_EXTENSION):
                    os.remove(self._storageFilePath + self.BACKUP_EXTENSION)
                os.rename(self._storageFilePath, self._storageFilePath + self.BACKUP_EXTENSION)
            with open(self._storageFilePath, "wb") as fileHandler:
                pickle.dump(self._storage, fileHandler)
            return Result(success=True)
        except Exception as ex:
            return Result(success=False, message=get_exception_printable_string(ex))

    def Load(self) -> Result:
        sErrors = ''
        try:
            if not os.path.exists(self._storageFilePath):
                raise FileNotFoundError(self._storageFilePath)
            with open(self._storageFilePath, "rb") as fileHandler:
                self._storage = pickle.load(fileHandler)
            return Result(success=True)
        except Exception as ex1:
            sErrors += get_exception_printable_string(ex1)
        try:
            if not os.path.exists(self._storageFilePath + self.BACKUP_EXTENSION):
                raise FileNotFoundError(self._storageFilePath + self.BACKUP_EXTENSION)
            with open(self._storageFilePath + self.BACKUP_EXTENSION, "rb") as fileHandler:
                self._storage = pickle.load(fileHandler)
                self.Save()
            return Result(success=True, message=sErrors)
        except Exception as ex2:
            sErrors += get_exception_printable_string(ex2)
        return Result(success=False, message=sErrors)

    def AddUpdate(self, key: str, value: object) -> Result:
        isKeyExist = key in self._storage
        pickledValue = pickle.dumps(value)
        self._storage[key] = pickledValue
        if isKeyExist: Result(success=True, message='Updated')
        return Result(success=True, message='Added')

    def Remove(self, key: str) -> Result:
        isExisted = self._storage.pop(key, None)
        if isExisted: return Result(success=True)
        return Result(success=False, message='Key [{}] not exist'.format(key))

    def __getitem__(self, key):
        pickledValue = self._storage[key]
        unPickledValue = pickle.loads(pickledValue)
        return unPickledValue

    def __str__(self):
        strReturn = ''
        for key in self._storage.keys():
            pickledValue = self._storage[key]
            unPickledValue = pickle.loads(pickledValue)
            strReturn += '({} {})'.format(key, unPickledValue)
        return strReturn

    def __iter__(self) -> (str, object):
        for key in self._storage:
            pickledValue = self._storage[key]
            unPickledValue = pickle.loads(pickledValue)
            yield key, unPickledValue

    def __contains__(self, key):
        return key in self._storage


if __name__ == "__main__":
    ds = ADataStore('d:\\temp\\storage.dat')
    # ds.AddUpdate('k1', 1)
    # print(ds.AddUpdate('k2', 2))
    # print(ds.AddUpdate('k2', 3))
    # ds.Save()

    r = ds.Load()
    print(r.Message)
    ds.Save()
