import io

# Function to read a txt file and return its contents as a list of lines
def breakdown_txt(txt):
    with io.open(txt, 'r', encoding='ISO-8859-1') as file:
        lines_txt = file.readlines()
    return lines_txt
