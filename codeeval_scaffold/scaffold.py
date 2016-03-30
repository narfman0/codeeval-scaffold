from bs4 import BeautifulSoup
from jinja2 import Template
import argparse
import os
import requests


def scaffold(challenge, text='', output_dir='./'):
    """ Parse a particular challenge """
    if not text:
        url = 'https://www.codeeval.com/open_challenges/' + challenge + '/'
        text = requests.get(url).text
    soup = BeautifulSoup(text, "html.parser")
    description, input, output, title = scrape(soup)
    write_project(output_dir, challenge, description, input, output, title)


def write_project(output_dir, challenge, description, input, output, title):
    """ Write template files to project output directory """
    try:
        os.makedirs(output_dir)
    except OSError:
        # probably already created
        pass
    # main
    with open(os.path.join(os.path.dirname(__file__), 'templates/main.py.txt')) as f:
        template = Template(f.read())
    result = template.render(challenge=challenge, description=description)
    with open(os.path.join(output_dir, 'main.py'), 'w') as f:
        f.write(result.encode('ascii','ignore'))
    # test
    with open(os.path.join(os.path.dirname(__file__), 'templates/test.py.txt')) as f:
        template = f.read()
    with open(os.path.join(output_dir, 'test.py'), 'w') as f:
        f.write(template)
    # data
    with open(os.path.join(output_dir, 'input.txt'), 'w') as f:
        f.write(input)
    with open(os.path.join(output_dir, 'output.txt'), 'w') as f:
        f.write(output)


def scrape(soup):
    """ Scrape page data and return description, input, output """
    description = None
    input = None
    output = None
    title = None
    last_h3 = ''
    container = (soup.select('.maincontent') or soup.select('.public_content_section'))[0]
    for child in container.children:
        if not str(child).strip():
            continue
        if 'class' in child.attrs and 'title-wrapper' in child['class']:
            title = child.text
        if 'h3' in child.name:
            last_h3 = child.text
        else:
            if 'escription' in last_h3:
                description = (description + '\n' if description else '') + child.text
            elif 'nput' in last_h3:
                if 'class' in child.attrs and 'description-input-output' in child['class']:
                    input = child.text
            elif 'utput' in last_h3:
                if 'class' in child.attrs and 'description-input-output' in child['class']:
                    output = child.text
    return description, input, output, title


def main():
    parser = argparse.ArgumentParser(description='Generate codeeval skeleton project for python')
    parser.add_argument('--challenge', help='number representing the challenge')
    parser.add_argument('--output_dir', default='./', help='output directory (default ./)')
    args = parser.parse_args()
    scaffold(challenge=args.challenge, output_dir=args.output_dir)


if __name__ == '__main__':
    main()
