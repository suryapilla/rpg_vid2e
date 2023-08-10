# Apply PSF to Event camera data

## Steps
1. Setup RGB to Event camera conversion as per the instructions in README.md file in rpg_vid2e directory

2. Navigate to psf directory

3. Download the video and convert to images, this python script populates the images and timestamps.txt file in the required dataset structure.
```
python vid2img.py
```

4. Open psf.ipynb file and run the code blocks to generate horizontal psf and then convole with image 

5. The final image after applying psf is stored in psf_img directory

