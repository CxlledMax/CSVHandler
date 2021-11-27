class CSVHandler:
    def load(path):
        if ".csv" in path:
            file = open(path)
            beautified = [element for element in [row.strip() for row in file.readlines()]]
            final = [row.split(", ") for row in beautified]
            return final

    def parse(path, data):
        if ".csv" in path:
            with open(path, "r+") as file:
                file.truncate(0)
            with open(path, "a") as file:
                for row in data:
                    file.write(", ".join(row) + "\n")
