from sentiment import SentimentAnalysis
import re

compiled_pattern = re.compile(r'(.*),(neg|pos),(neg|pos)')

class Dataset:
    def __init__(self, file_name):
        self.lines = []
        self.attributes = []
        self.dataset_relation = ''

        self.added_features = 0

        self.file_name = file_name
        self.load_file(file_name)

    def add_feature(self,attribute_name, attribute_type, delegate):
        self.attributes.append((attribute_name, attribute_type))
        self.added_features += 1        

        for i, line in enumerate(self.lines):
            line.append(delegate(line, i))

    def export_file(self):
        dataset_relation_append = self.dataset_relation + '_' + str(self.added_features)

        arff_write = open(self.file_name + '_' + str(self.added_features) + '.arff', 'w')
        
        arff_write.write("@relation " + dataset_relation_append + '\n\n')

        for attr in self.attributes:
            arff_write.write("@attribute " + attr[0] + " " + attr[1] + '\n')

        arff_write.write("\n@data\n")

        for line in self.lines:
            arff_write.write(','.join(str(i) for i in line) + '\n')

    
    def load_file(self, file_name):
        header = True
        arff_file = open(file_name+".arff", "r")
        
        for line in arff_file:
            if header:
                if line.find('@attribute') != -1:
                    attr_name = line.split(' ')[1]
                    attr_type = line.split(' ')[2]
                    self.attributes.append((attr_name,attr_type))

                elif line.find('@relation') != -1:
                    dataset_relation = line.split(' ')[1]
                    self.dataset_relation = dataset_relation.strip()

                elif line.find('@data') != -1:
                    header = False

            else:
                regex_result = compiled_pattern.match(line)

                if regex_result:
                    new_line = [item for item in regex_result.groups()]
                    self.lines.append(new_line)

        arff_file.close()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        file_name = sys.argv[1]

        Dataset(file_name)