def countWords(file):
    #Open the file
    with open(file, "r") as file:
        content = file.read()

    #Split the words by space

    return (len(content.split()))

#Only fif this file is called for testing
if __name__ == "__main__":
    #print the data
    print("The total word count is", countWords("../task6_read_me . txt"))