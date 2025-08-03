# Sciency Dipduino Professional Booklet - PDF Generation Guide

## Overview
This directory contains the professionally designed Sciency Dipduino booklet with fixed image links and enhanced styling optimized for PDF generation.

## Files
- `professional-booklet.html` - The enhanced HTML file with proper image links and professional styling
- `generate-pdf.js` - Node.js script for PDF generation using Puppeteer
- `generate-pdf.py` - Python script for PDF generation using various methods
- `circuit-diagrams/` - Directory containing all circuit diagram images
- `mblock-code-screenshots/` - Directory containing all mBlock code screenshots

## Methods to Generate PDF

### Method 1: Browser Print (Easiest - Recommended)
1. Open `professional-booklet.html` in Chrome or Edge browser
2. Press `Ctrl+P` (Windows/Linux) or `Cmd+P` (Mac)
3. Configure print settings:
   - Destination: Save as PDF
   - Layout: Portrait
   - Paper size: A4
   - Margins: Default
   - Options: Check "Background graphics"
4. Click "Save" and choose your filename

### Method 2: Using Node.js Script
```bash
# Navigate to this directory
cd "client/public/SCIENCY DIPDUINO BOOKLET"

# Run the Node.js script (will auto-install puppeteer if needed)
node generate-pdf.js
```

### Method 3: Using Python Script
```bash
# Navigate to this directory
cd "client/public/SCIENCY DIPDUINO BOOKLET"

# Make the script executable (Mac/Linux)
chmod +x generate-pdf.py

# Run the script
python3 generate-pdf.py
```

The Python script will check for available PDF libraries and use the first one found:
- WeasyPrint (recommended): `pip install weasyprint`
- PDFKit: `pip install pdfkit` (also requires wkhtmltopdf)
- wkhtmltopdf: Download from https://wkhtmltopdf.org/downloads.html

### Method 4: Using command line tools directly

#### With wkhtmltopdf:
```bash
wkhtmltopdf --page-size A4 --margin-top 20mm --margin-right 20mm --margin-bottom 20mm --margin-left 20mm --enable-local-file-access professional-booklet.html Sciency-Dipduino-Guide.pdf
```

#### With WeasyPrint:
```bash
weasyprint professional-booklet.html Sciency-Dipduino-Guide.pdf
```

## Output
The generated PDF will be named `Sciency-Dipduino-Professional-Guide.pdf` and will be saved in the same directory.

## Features of the Professional Booklet
- Fixed all broken image links
- Enhanced typography and layout
- Professional color scheme
- Optimized for A4 printing
- Page break controls for better formatting
- Enhanced image styling with borders and shadows
- Responsive design that works well in PDF format

## Troubleshooting
- If images don't appear in the PDF, ensure you're running the generation from the correct directory
- For best results, use Chrome or Edge browser's print-to-PDF feature
- If using command line tools, ensure they have access to local files (--enable-local-file-access flag)