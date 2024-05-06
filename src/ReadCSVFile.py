import csv, os
class ReadCSVFile:

    def fix_working_directory(self):
        current_working_directory = os.getcwd()
        while "test" in current_working_directory or "src" in current_working_directory:
            os.chdir("../")
            current_working_directory = os.getcwd()

    def get_file_data(self,file_name):
        self.fix_working_directory()
        file_data = []
        with open("resource/" + file_name, 'rt')as data_file:
            file_reader = csv.reader(data_file)
            for row in file_reader:
                file_data.append(row)
        return file_data

    def get_last_lines(self, file_name, numer_of_lines):
        return get_file_data(file_name)[-1 * numer_of_lines]