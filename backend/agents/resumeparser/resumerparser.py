def fun():

    """
    import nltk
    nltk.download('stopwords')

    from pyresparser import ResumeParser
    import warnings

    warnings.filterwarnings("ignore", category=UserWarning)

    data = ResumeParser("resume.pdf").get_extracted_data()
    print(data)

    print("Name:", data["name"])
    print("Email:", data["email"])
    print("Mobile Number:", data["mobile_number"])
    print("Skills:", data["skills"])
    print("College Name:", data["college_name"])
    print("Degree:", data["degree"])
    print("Designation:", data["designation"])
    print("Company Names:", data["company_names"])
    print("No Of Pages:", data["no_of_pages"])
    print("Total Experience:", data["total_experience"])"""


    """from pyresparser import ResumeParser
    data = ResumeParser('resume.pdf').get_extracted_data()
    print(data)
    """


import os
from google import genai

# NOTE: Ensure your GEMINI_API_KEY environment variable is set.
client = genai.Client(api_key='AIzaSyBGOALhYMQQJcIXXqE5SgCXA4BK2L3VsZY')

PDF_FILE_PATH = 'resume.pdf' 
USER_PROMPT = "Extract details and give score and suggestions"

try:
    # 1. Upload the PDF file using the Files API
    print(f"Uploading file: {PDF_FILE_PATH}...")
    uploaded_file = client.files.upload(file=PDF_FILE_PATH)
    print(f"File uploaded successfully: {uploaded_file.name}")

    # 2. Make the multimodal API call with the file object and text prompt
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[USER_PROMPT, uploaded_file]
    )

    # 3. Print the model's response
    #print("\n--- Model Response ---")
    print(response.text)
    
except Exception as e:
    print(f"An error occurred during the API call: {e}")

finally:
    # 4. Clean up: Delete the file from the service after processing
    # Files are automatically deleted after 48 hours, but it's good practice to delete them.
    if 'uploaded_file' in locals() and uploaded_file.name:
        client.files.delete(name=uploaded_file.name)
        #print(f"\nFile {uploaded_file.name} deleted.")