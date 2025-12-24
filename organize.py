import os
import shutil
import pickle
import re

# Load model
model = pickle.load(open('document_tagger.pkl', 'rb'))

def clean(text):
    text = text.lower()
    text = re.sub(r'[\\/_\-\.\(\)\[\]]', ' ', text)
    return text

folder = r"C:\Users\PMYLS\Downloads" 

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    
    if os.path.isfile(filepath):
        tag = model.predict([clean(filepath)])[0]
        
        tag_folder = os.path.join(folder, tag)
        os.makedirs(tag_folder, exist_ok=True)
        
        shutil.move(filepath, os.path.join(tag_folder, filename))
        print(f"✅ {filename} → {tag}/")

print("\n🎉 Done!")