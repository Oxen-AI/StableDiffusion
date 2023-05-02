# StableDiffusion

Make sure that src is in your python path

```bash
export PYTHONPATH=src 
```

Generate an image

```bash
python tools/generate.py -m 'runwayml/stable-diffusion-v1-5' -p 'a 35mm color photo of a ox in a field' -o data/images/
```

Train a model

```bash
python tools/train.py -d data_dir -o my_model
```