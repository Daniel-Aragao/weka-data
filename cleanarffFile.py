"""
Before using:
    - put anottations: "relation", "attributes" and "data" in uppercase
    - put types in uppercase
    - change tabs with commas, make sure you substitute all commas for spaces before
    - change all single quotes to double quotes
"""

file_name = "./SentiWordNet_3.0.0_20130122"
arff_file = open(file_name+".arff", "r")

arff_read_lines = arff_file.readlines()
arff_write = open(file_name + '_clean.arff', 'w')

state = ''

strings_positions = []

attr_count = 0

for line in arff_read_lines:
    if line.startswith("@RELATION"):
        state = "@RELATION"
        arff_write.write(line)

    elif line.startswith("@DATA"):
        state = "@DATA"
        arff_write.write(line)

    elif line.startswith("@ATTRIBUTE"):
        attr_type = line.split(' ')[2]

        if attr_type.find("STRING") >= 0:
            strings_positions.append(attr_count)

        attr_count += 1

        arff_write.write(line)

    elif state == "@DATA":
        columns = line.split(',')

        for i, column in enumerate(columns):
            column = column.strip()

            if not column:
                columns[i] = '?'
                
            elif i in strings_positions:
                if column:
                    columns[i] = "'" + column + "'"

                
        new_line = ','.join(i for i in columns) + '\n'

        arff_write.write(new_line)   

    else:
        arff_write.write(line)

arff_write.flush()
arff_write.close()
arff_file.close()