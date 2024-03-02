## Scripts
This is the folder that contains useful scripts that can be used to automate you process.

### Automated Cover Letter
This script is used to regenerate pdf file for the cover letter. You have to provide following arguments in the `./automated_cover_letter.py` file to generate template based cover lettes:
- `source_docx`: This is the actual cover letter that is saved with template strings. Enter the absolute path of the document file.
- `destination_docx`: This is the destination file where new document file will be saved.
- `destination_pdf`: This is the absolute path of the new cover letter pdf file.
- `company`: Enter the name of a company that will be shown in pdf.
- `Today_Date`: Enter date that will be mentioned in the pdf.
- `Company_Location`: Enter the company location.

Perform following steps to run this script:
1. cd scripts
2. Create a virtual environment `virtualenv venv`.
3. Install the depedencies `pip install -r requirements.txt`.
4. Start the script `py automated_cover_letter.py`