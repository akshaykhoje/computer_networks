# python script to merge all text files into a single md file\

import os

def create_markdown_from_txt(folder_path, output_file):
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    with open(output_file, 'w') as 
        for txt_file in txt_files:
            section_heading = os.path.splitext(txt_file)[0]
            markdown_file.write(f"# {section_heading}\n\n")

            with open(os.path.join(folder_path, txt_file), 'r') as txt_content:
                markdown_file.write(txt_content.read())

            markdown_file.write('\n\n')

    print(f"Markdown file '{output_file}' created successfully.")

# Example usage:
folder_path = '/path/to/your/txt/files'
output_file = 'output.md'
create_markdown_from_txt(folder_path, output_file)
