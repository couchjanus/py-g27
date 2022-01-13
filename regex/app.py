import os, sys
import pdfplumber

import re

invoice = {
    'invoice_number': '',
}

def setItem(pattern, string, key):
    result = re.search(pattern, string)
    if result:
        invoice[key] = result.group(1)

def find_following_line(file, pattern, slise):
    lines = []
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            lines.append(line)
    
    for i, line in enumerate(lines):
        if re.search(pattern, line):
            return lines[i+slise[0]:i+slise[1]]


def main():
    if len(sys.argv) < 2:
        print("Use <script name>.py <input file>.pdf, please")
        sys.exit(1)
    pdffile = sys.argv[1]
    basename = os.path.basename(pdffile)
    # print(basename)
    file_ext = os.path.splitext(basename)[1]
    # print(file_ext)

    if file_ext != '.pdf':
        print("Error {} invalid extension".format(file_ext))
        sys.exit(1)

    if not os.path.isfile(pdffile):
        print("Error {} does not exists".format(pdffile))
        sys.exit(1)

    file_name = os.path.splitext(basename)[0]

    file_name_in = file_name + '.in'

    if len(sys.argv) > 2:
        file_name_out = sys.argv[2]
    else:
        file_name_out = file_name + '.out'

    # print(file_name_out)

    if os.path.isfile(file_name_out):
        print("{} exists! Override (y/n)? ".format(file_name_out))
        reply = input().strip().lower()
        if reply[0] != 'y':
            sys.exit(1)
    with pdfplumber.open(basename) as pdf:
        pages = pdf.pages
        for page in pages:
            with open(file_name_in, 'w') as f:
                t = page.extract_text()
                # print(t)
                f.write(t)

    lines = []

    # with open(file_name_in) as fIn:
    #     pattern = "INV-([0-9]+)"
    #     for line in fIn:
    #         line = line.rstrip()
    #         result = re.search(pattern, line)
    #         if result:
    #             print(result.group(1))

    with open(file_name_in) as fIn:
        
        for line in fIn:
            line = line.rstrip()
            setItem("INV-([0-9]+)", line, 'invoice_number')
            setItem("Subtotal \$(\d+\.\d\d)", line, 'product_subtotal')
            setItem("Shipping \$(\d+\.\d\d)", line, 'product_shipping')
            setItem("Total \$(\d+\.\d\d)", line, 'product_total')
            setItem("(\d+\/\d+\/[0-9]{4})", line, 'invoice_date')
            setItem("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z]+)", line, 'email')

    lines = find_following_line(file_name_in, "Billing Information Shipping Information", (1,5))
    invoice['billing_info'] = lines[0:2]
    invoice['shipping_info'] = lines[2:4]

    lines = find_following_line(file_name_in, "Price", (1,3))
    invoice['product_description'] = lines[0:1]
    unit = ''.join(lines[1:2])
    setItem("\$(\d+\.\d\d)", unit, 'product_price')
    setItem("(\d+)", unit, 'product_qty')
    setItem("([a-zA-Z :_.-]+)", unit, 'product_name')
    print(invoice)    

    with open(file_name_out, 'w') as fOut:
        fOut.write(f"{invoice}\n")

if __name__ == '__main__':
    main()
