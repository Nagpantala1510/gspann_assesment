  def justify_paragraph(paragraph, page_width):
    # Check if page_width is a positive integer
    if not isinstance(page_width, int) or page_width <= 0:
         raise ValueError("Page width should be a positive integer.")
    # Check if paragraph is a non-empty string
    if not isinstance(paragraph, str) or not paragraph.strip():
        raise ValueError("Paragraph should be a non-empty string.")
    # Split the paragraph into individual words
    words = paragraph.split()
    
    # Initialize variables to store lines of justified text
    lines = []
    current_line = []
    current_line_length = 0

    # Iterate through each word in the paragraph that are given by user
    for word in words:

        # checking if the current line exceeds the given page width on adding current word
        if current_line_length + len(current_line) + len(word) <= page_width:
            
            
            # if current line does not exceeds then adding word to current line
            current_line.append(word)
            current_line_length += len(word)
        else:
            # If adding the word exceeds the page width, start a new line
            # if current line exceeds the given page width, the nadding a new line
            lines.append(current_line)
            current_line = [word]
            current_line_length = len(word)

    # Append the last line to the list of lines
    if current_line:
        lines.append(current_line)

    # Initializing a list variable to store the justified lines
    justified_lines = []

    # Iterate through each line and justify the text
    for i, line in enumerate(lines, 1):

        if len(line) == 1:
            # If the line contains only one word then, left justify it
            justified_lines.append(f"Array[{i}] = \"{line[0].ljust(page_width)}\"")

        else:

            # for lines with multiple words, will calculate the spaces between the words
            total_spaces = page_width - sum(len(word) for word in line)
            word_spaces = total_spaces // (len(line) - 1)
            extra_spaces = total_spaces % (len(line) - 1)

            justified_line = ''
            
            # Iterating through each word in the line and adding spaces as per required length
            for j, word in enumerate(line):
                justified_line += word
                if j < len(line) - 1:
                    justified_line += ' ' * word_spaces
                    if j < extra_spaces:
                        justified_line += ' '
            
            # Appending the justified lines to the list
            justified_lines.append(f"Array[{i}] = \"{justified_line}\"")

    return justified_lines

# Prompt message to ask user input for paragraph and page width
paragraph = input("Enter the paragraph: ")
page_width = int(input("Enter the page width: "))


# Calling justifed lines and printing the lines
justified_lines = justify_paragraph(paragraph, page_width)
for line in justified_lines:
    print(line)

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")    
