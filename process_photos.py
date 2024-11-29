import os
import csv
import requests
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse

def load_image(path_or_url):
    """Load image from URL or local path and return as PIL Image object."""
    try:
        # Check if the path is a URL
        parsed = urlparse(path_or_url)
        if parsed.scheme in ('http', 'https'):
            # Handle URL
            response = requests.get(path_or_url)
            response.raise_for_status()
            return Image.open(BytesIO(response.content))
        else:
            # Handle local path - remove leading slash and make relative to current directory
            local_path = path_or_url.lstrip('/')
            if not os.path.isfile(local_path):
                local_path = os.path.join('.', local_path)
            if os.path.isfile(local_path):
                return Image.open(local_path)
            else:
                print(f"File not found: {local_path}")
                return None
    except Exception as e:
        print(f"Error loading image from {path_or_url}: {str(e)}")
        return None

def detect_face(image):
    """Detect face in image using OpenCV and return the face rectangle."""
    # Convert PIL Image to OpenCV format
    opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Load pre-trained face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Detect faces
    faces = face_cascade.detectMultiScale(
        cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY),
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    if len(faces) > 0:
        # Return the first (presumably largest) face
        return faces[0]
    return None

def crop_and_resize(image, face_rect=None, target_size=(320, 320)):
    """
    Crop image to square, centering on face if detected,
    and resize to target size.
    """
    width, height = image.size
    new_size = min(width, height)
    
    if face_rect is not None:
        # Convert face rectangle to PIL coordinates
        x, y, w, h = face_rect
        face_center_x = x + w//2
        face_center_y = y + h//2
        
        # Calculate crop box centered on face
        left = max(face_center_x - new_size//2, 0)
        top = max(face_center_y - new_size//2, 0)
        
        # Adjust if crop box goes beyond image boundaries
        if left + new_size > width:
            left = width - new_size
        if top + new_size > height:
            top = height - new_size
    else:
        # If no face detected, crop from top
        left = (width - new_size) // 2
        top = 0
    
    right = left + new_size
    bottom = top + new_size
    
    # Crop to square
    cropped = image.crop((left, top, right, bottom))
    
    # Resize to target size using high-quality resampling
    resized = cropped.resize(target_size, Image.Resampling.LANCZOS)
    
    return resized

def process_team_images(input_csv, output_dir, output_csv):
    """Process all team member images and create new CSV."""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read input CSV and process each row
    with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            if row['image'] and row['username']:
                print(f"Processing image for {row['username']}...")
                
                # Load image from URL or local path
                image = load_image(row['image'])
                if image:
                    # Detect face
                    face_rect = detect_face(image)
                    
                    # Crop and resize image
                    processed_image = crop_and_resize(image, face_rect, target_size=(320, 320))
                    
                    # Save processed image
                    output_path = os.path.join(output_dir, f"{row['username']}.jpg")
                    processed_image = processed_image.convert('RGB')  # Convert to RGB if necessary
                    processed_image.save(output_path, 'JPEG', quality=85, optimize=True)
                    
                    # Update image path in CSV
                    row['image'] = f"/{output_dir}/{row['username']}.jpg"
                
            writer.writerow(row)

# Main execution
if __name__ == "__main__":
    input_csv = "_data/team.csv"
    output_dir = "assets/images/team"
    output_csv = "_data/team_new.csv"
    
    process_team_images(input_csv, output_dir, output_csv)