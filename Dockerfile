# Use the official Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages
RUN pip install PyMuPDF Pillow

# Run the Python script by default when the container starts
CMD ["python", "merger.py"]
