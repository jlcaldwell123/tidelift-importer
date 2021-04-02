import csv
import os
import sys
class TideliftCaller(object):
    def __init__(self):
        self.catalog = 'test'
    def request_package(self, platform, name, version):
        result = os.system("tidelift request " + platform + " " + name + " " + version)
def main(dependency_file):
    tideliftCaller = TideliftCaller()
    with open(dependency_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='	', quotechar='|')
        for row in spamreader:
            print(row)
            tideliftCaller.request_package(row[0], row[1], row[2])
if __name__ == "__main__":
    main(sys.argv[1])