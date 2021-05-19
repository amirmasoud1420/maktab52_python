import os


class BackupOpen:
    def __init__(self, *arg, **kwarg):
        self.file_path = arg[0]
        self.arg = arg
        self.kwarg = kwarg
        self.backup_file_contents = ''
        self.is_exist = False

    def __enter__(self):
        if os.path.exists(self.file_path):
            self.is_exist = True
            with open(self.file_path, 'r') as f:
                self.backup_file_contents = f.read()
        self.file = open(*self.arg, **self.kwarg)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.file.close()
            print("error received!!!")
            if self.is_exist:
                with open(self.file_path, 'w') as f:
                    f.write(self.backup_file_contents)
                    return True
            else:
                self.file.close()
                os.remove(self.file_path)
        else:
            self.file.close()

        return True


with BackupOpen('pejman1.txt', 'w') as f:
    f.file.write('\nsalam')
    f.read()
