# create_txt.py
def create_text_file():
    with open("data.txt", "w") as f:
        f.write("This is a sample text file generated by Python.")

if __name__ == "__main__":
    create_text_file()
    print("data.txt file has been created.")