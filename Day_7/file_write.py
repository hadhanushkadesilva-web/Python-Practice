# Open a file in write mode (creates it)
file = open("my_first_file.txt", "w")

# Write 3 lines
file.write("Hello from Python!\n")
file.write("This is line 2.\n")
file.write("And this is the third line.\n")

# Close the file
file.close()

print("✓ File written. Check your folder for 'my_first_file.txt'")