from datetime import datetime


class Logger:

    def __init__(self, file_name=None):
        self.do = 1 # manual switch

        if file_name is None:
            date = str(datetime.now())
            date = date.replace(" ", "_")
            date = date.replace(":", "_")
            date = date.replace("-", "_")
            date = date.replace(".", "_")
            print(date)
            underscored_date = date
            print(underscored_date)
            self.file_path = "./resources/log_data/" + underscored_date + ".txt"
            # self.file_path = "./resources/xd.txt"
        else:
            self.file_path = file_name

        with open(self.file_path, "w") as f:
            f.write("Logger:")
            f.write(self.line_break())

    def log_into_file(self, new_entry):
        print(new_entry)
        if self.do is 1:
            with open(self.file_path, "a") as f:
                f.write("\n" + new_entry)

    def line_break(self):
        return "\n---------------------------------------------------------"
