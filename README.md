# Predefined Image Classifier to Identify Dog Breeds

This project classifies pet images with a pretrained ImageNet CNN model and compares the classifier output with ground-truth pet labels to report classification statistics.

## Run the project

Run a single model (example with VGG):

```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

Run batch scripts:

```bash
./run_models_batch.sh
./run_models_batch_uploaded.sh
```

## Accuracy results

- pet_images/: [fill in after re-running]
- uploaded_images/: [fill in after re-running]

## Label matching

Label comparison now uses whole-word/phrase matching instead of substring matching, which avoids false positives such as matching `cat` inside `catamount`.

## Run tests

```bash
python -m unittest -v
```
