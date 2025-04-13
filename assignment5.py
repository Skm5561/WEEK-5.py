def modify_content(content):
    return content.upper()  # Example: make text uppercase

def file_read_write():
    try:
        filename = input("Enter the filename to read: ")

        with open(filename, 'r') as file:
            content = file.read()

        modified = modify_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified)

        print(f"✅ Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: File not found.")
    except IOError:
        print("❌ Error: Unable to read or write the file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

file_read_write()
