FROM python:3.9-slim
COPY . .
RUN apt-get update && apt-get install -y libglib2.0-0 libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
CMD ["python","demo_simple_ocr_en.py"]