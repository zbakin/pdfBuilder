# PNG to PDF Converter

This application converts a series of PNG images into individual PDF files and then merges those PDFs into a single, combined PDF document. The application is containerized using Docker for easy deployment and consistent environment management.

## Features

- Converts multiple PNG images to individual PDF files.
- Merges all generated PDFs into a single document.
- Easily configurable and deployable using Docker.

## Requirements

- Docker installed on your machine.
- A folder containing the PNG images you wish to convert.

## Getting Started

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository_url>
cd <repository_folder>
```
### 2. Build Docker image

```bash
docker build -t image-to-pdf .
```
### 2. Run Docker container to build combined PDF

```bash
docker run --rm -v "$(pwd):/app" image-to-pdf
```

## Motivation

The idea to create such application was due to preparation for multiple visa applications, where they all require PDF formatted documents. Most of the offline PDF converters were either paid or had very limited number of conversions available. 

I decided to use Python for quick and simple developement. On my personal Macbook with Apple Silicon, the use of PyMuPDF was not easy as it required quite a setup or not possible at all.

https://www.reddit.com/r/learnpython/comments/x5nd2f/m1_mac_myupdf_install_wheel/

For this reason I decided to use Docker.