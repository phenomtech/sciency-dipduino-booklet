#!/usr/bin/env python3
"""
Generate PDF from HTML using weasyprint or alternative methods
"""
import os
import sys
import subprocess

def check_and_install_dependencies():
    """Check if required packages are installed"""
    try:
        import weasyprint
        return True, "weasyprint"
    except ImportError:
        print("WeasyPrint not found. Checking for alternatives...")
        
    try:
        import pdfkit
        return True, "pdfkit"
    except ImportError:
        print("PDFKit not found. Checking for wkhtmltopdf...")
        
    # Check if wkhtmltopdf is installed
    try:
        subprocess.run(["wkhtmltopdf", "--version"], capture_output=True, check=True)
        return True, "wkhtmltopdf"
    except:
        pass
    
    return False, None

def generate_with_weasyprint():
    """Generate PDF using WeasyPrint"""
    import weasyprint
    
    print("Generating PDF with WeasyPrint...")
    html_file = os.path.join(os.path.dirname(__file__), 'professional-booklet.html')
    pdf_file = os.path.join(os.path.dirname(__file__), 'Sciency-Dipduino-Professional-Guide.pdf')
    
    # Create PDF
    html = weasyprint.HTML(filename=html_file, base_url=os.path.dirname(html_file))
    html.write_pdf(pdf_file)
    
    print(f"PDF generated successfully: {pdf_file}")

def generate_with_pdfkit():
    """Generate PDF using pdfkit"""
    import pdfkit
    
    print("Generating PDF with PDFKit...")
    html_file = os.path.join(os.path.dirname(__file__), 'professional-booklet.html')
    pdf_file = os.path.join(os.path.dirname(__file__), 'Sciency-Dipduino-Professional-Guide.pdf')
    
    options = {
        'page-size': 'A4',
        'margin-top': '20mm',
        'margin-right': '20mm',
        'margin-bottom': '20mm',
        'margin-left': '20mm',
        'encoding': "UTF-8",
        'enable-local-file-access': None
    }
    
    pdfkit.from_file(html_file, pdf_file, options=options)
    print(f"PDF generated successfully: {pdf_file}")

def generate_with_wkhtmltopdf():
    """Generate PDF using wkhtmltopdf directly"""
    print("Generating PDF with wkhtmltopdf...")
    html_file = os.path.join(os.path.dirname(__file__), 'professional-booklet.html')
    pdf_file = os.path.join(os.path.dirname(__file__), 'Sciency-Dipduino-Professional-Guide.pdf')
    
    cmd = [
        "wkhtmltopdf",
        "--page-size", "A4",
        "--margin-top", "20mm",
        "--margin-right", "20mm",
        "--margin-bottom", "20mm",
        "--margin-left", "20mm",
        "--enable-local-file-access",
        html_file,
        pdf_file
    ]
    
    subprocess.run(cmd, check=True)
    print(f"PDF generated successfully: {pdf_file}")

def main():
    """Main function"""
    print("Sciency Dipduino PDF Generator")
    print("="*50)
    
    # Check dependencies
    available, method = check_and_install_dependencies()
    
    if not available:
        print("\nNo PDF generation tools found!")
        print("Please install one of the following:")
        print("1. pip install weasyprint")
        print("2. pip install pdfkit (also requires wkhtmltopdf)")
        print("3. Install wkhtmltopdf directly from: https://wkhtmltopdf.org/downloads.html")
        sys.exit(1)
    
    # Generate PDF based on available method
    try:
        if method == "weasyprint":
            generate_with_weasyprint()
        elif method == "pdfkit":
            generate_with_pdfkit()
        elif method == "wkhtmltopdf":
            generate_with_wkhtmltopdf()
    except Exception as e:
        print(f"Error generating PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()