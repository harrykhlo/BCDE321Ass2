import subprocess
import os


class MyCreator:
    def __init__(self, image_name, file_name):
        self.image_name = image_name
        self.file_name = file_name
        print('Creating diagram...')

    def create_diagram(self):
        if self.validate_file_name():
            if self.validate_image_name():
                subprocess.call('pyreverse -o ' + self.image_name + ' -A -S -mn -f ALL ' + self.file_name)  # creates a image file
                print('Diagram "' + self.image_name + '" created!')

    def validate_file_name(self):
        try:
            with open(self.file_name) as f:
                f.close()
                return True
        except FileNotFoundError:
            print("File Doesn't Exist!")
            return False

    def validate_image_name(self):  # always returns with a classes. prefix, figure out later
        return True

    def delete_diagram(self):
        os.remove('classes.' + self.image_name)
        print(self.image_name + ' deleted!')


# MyCreator('FullClassDiagram.png', 'TestClass.py').run()
