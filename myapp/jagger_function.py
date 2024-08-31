import jagger
import requests
import pdfplumber  # PyMuPDF

model_path = "model/kwdlc/patterns"

tokenizer = jagger.Jagger()
tokenizer.load_model(model_path)

text = "吾輩は猫である。名前はまだない。"
toks = tokenizer.tokenize(text)

for tok in toks:
    print(tok.surface(), tok.feature())
print("EOS")
url = 'https://serpapi.com/playground?engine=google_scholar&q=経済&hl=ja'
response = requests.get(url)
if response.status_code == 200:
    # Print the response content (HTML, JSON, etc.)
    pdf = pdf_to_text(response)
    print(pdf)
else:
    print(f"Error: {response.status_code}")


def pdf_to_text(pdf_path):
    doc = pdfplumber.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

pdf_path = 'example.pdf'
text = pdf_to_text(pdf_path)
print(text)
