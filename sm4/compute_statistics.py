"""
compute_statistics.py

Basic statistics are calculated from the data of the given file.
"""

class ComputeStatistics:
    """
    Class to carry out state operations in a list of items.
    """


    def __init__(self):
        self.decimals = 4
        self.file_name_save = "results.txt"


    def get_file_data(self, file_name):
        """
            Extracts the data from the given file and returns it in an array
        """
        data = []
        with open(file_name, 'r', encoding="utf-8") as file:
            data = [float(line.strip()) for line in file]
        return data


    def get_statics(self, data):
        """
            Calculate all statistical data
        """
        median = 0
        mod = 0
        sd = 0
        variance = 0
        count = len(data)
        mean = sum(data) / count

        # Calculate the median
        sorted_data = sorted(data)
        if count % 2 == 0:
            mid1 = sorted_data[count // 2 - 1]
            mid2 = sorted_data[count // 2]
            median = (mid1 + mid2) / 2
        else:
            median = sorted_data[count // 2]

        # Calculate the mode
        frequencies = {number: data.count(number) for number in set(data)}
        mod = max(frequencies, key=frequencies.get)

        # Calculate the variance
        variance = sum((x - mean) ** 2 for x in data) / (count -  1)

        # Calculate the deviate standard
        sd = variance ** 0.5

        statics = {
            "count":  count,
            "mean": mean,
            "median": median,
            "mod": mod,
            "sd": round(sd, self.decimals),
            "variance": round(variance, self.decimals)
        }
        return statics


    def set_print_statics(self, data):
        """
            Print result data to a file
        """
        print("\nRESULTS")
        for clave, valor in data.items():
            print(f"{clave.upper()}: {valor}")
        print("\n")


    def set_save_statics(self, data):
        """
            Save result data to a file
        """
        with open(self.file_name_save, 'w', encoding="utf-8") as file:
            for clave, valor in data.items():
                file.write(f"{clave.upper()}: {valor}" + "\n")


    def operation(self):
        """
        :param file_name: File name to read.
        """
        try:
            file_name = input("File name: ")
            file_data = self.get_file_data(file_name)
            statics = self.get_statics(file_data)
            self.set_print_statics(statics)
            self.set_save_statics(statics)
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    compute_statistics = ComputeStatistics()
    compute_statistics.operation()
