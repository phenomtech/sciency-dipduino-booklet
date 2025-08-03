const puppeteer = require('puppeteer');
const path = require('path');

async function generatePDF() {
    console.log('Starting PDF generation...');
    
    try {
        // Launch browser
        const browser = await puppeteer.launch({
            headless: true,
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        
        const page = await browser.newPage();
        
        // Load the HTML file
        const htmlPath = `file://${path.resolve(__dirname, 'professional-booklet.html')}`;
        await page.goto(htmlPath, {
            waitUntil: 'networkidle0'
        });
        
        // Wait for images to load
        await page.waitForTimeout(2000);
        
        // Generate PDF with professional settings
        await page.pdf({
            path: 'Sciency-Dipduino-Professional-Guide.pdf',
            format: 'A4',
            printBackground: true,
            margin: {
                top: '20mm',
                right: '20mm',
                bottom: '20mm',
                left: '20mm'
            },
            displayHeaderFooter: false,
            preferCSSPageSize: true
        });
        
        console.log('PDF generated successfully: Sciency-Dipduino-Professional-Guide.pdf');
        
        await browser.close();
    } catch (error) {
        console.error('Error generating PDF:', error);
        process.exit(1);
    }
}

// Check if puppeteer is installed
try {
    require.resolve('puppeteer');
    generatePDF();
} catch (e) {
    console.log('Puppeteer not found. Installing...');
    const { execSync } = require('child_process');
    execSync('npm install puppeteer', { stdio: 'inherit' });
    console.log('Puppeteer installed. Generating PDF...');
    generatePDF();
}