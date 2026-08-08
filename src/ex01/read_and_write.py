def open_files():
    result_file = open("ds.tsv", "w", encoding="utf-8")
    file = open("ds.csv", "r", encoding="utf-8")
    for line in file:
        line = change_line(line)
        result_file.write(line)
    file.close()
    result_file.close()
 
def change_line(line):
    inside_quotes = False
    result = []
    for char in line:
        if char == '"':
            inside_quotes = not inside_quotes
        
        if inside_quotes == False and char == ',':
            result.append("\t")
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    open_files()