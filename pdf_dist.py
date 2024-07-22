import os
import PyPDF2
import matplotlib.pyplot as plt

def count_pdf_pages(folder_path):
    pdf_page_counts = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                try:
                    with open(pdf_path, 'rb') as pdf_file:
                        reader = PyPDF2.PdfReader(pdf_file)
                        num_pages = len(reader.pages)
                        pdf_page_counts.append(num_pages)
                except Exception as e:
                    print(f"Error reading {pdf_path}: {e}")

    return pdf_page_counts

def plot_page_distribution(page_counts):
    plt.hist(page_counts, bins=range(1, max(page_counts) + 2), edgecolor='black')
    plt.title('Distribution of PDF Page Counts')
    plt.xlabel('Number of Pages')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ")
    pdf_page_counts = count_pdf_pages(folder_path)
    if pdf_page_counts:
        plot_page_distribution(pdf_page_counts)
    else:
        print("No PDF files found.")
