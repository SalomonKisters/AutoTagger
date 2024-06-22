from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM 
import os 
import csv
from tqdm import tqdm
import random

directory = "C:\\"
image_endings = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]
random_number = random.randint(0,1000)

def find_images(base_folder):
    images = []
    for path, subdirs, files in os.walk(base_folder):
        for file in files:
            if os.path.splitext(file)[-1].lower() in image_endings:
                images.append(os.path.join(path, file))
    return images

print("Locating images")
images = find_images(directory)
print(f"Found {len(images)} images.")

print("Initializing model")
model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-large-ft", trust_remote_code=True)
processor = AutoProcessor.from_pretrained("microsoft/Florence-2-large-ft", trust_remote_code=True)

print("Processing images")
with open(f'image_analysis_results_{random_number}.tsv', 'w', newline='', encoding='utf-8') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')

    writer.writerow(['File Path', 'Parsed Answer'])

    for image_path in tqdm(images, desc="Processing Images", unit="image"):
        try:
            image = Image.open(image_path)

            inputs = processor(text="<OD>", images=image, return_tensors="pt")

            generated_ids = model.generate(
                input_ids=inputs["input_ids"],
                pixel_values=inputs["pixel_values"],
                max_new_tokens=1024,
                do_sample=False,
                num_beams=3
            )
            generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]

            parsed_answer = processor.post_process_generation(generated_text, task="<OD>", image_size=(image.width, image.height))

            writer.writerow([image_path, parsed_answer])
        except Exception as e:
            print(f"Error processing {image_path}: {str(e)}")

print(f"Processing complete. Results saved in 'image_analysis_results_{random_number}.tsv'")