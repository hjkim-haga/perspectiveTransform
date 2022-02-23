import json
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--path', type=str, help='JSON returned from NaverOCR.')
args = parser.parse_args()

if __name__ == '__main__':
    path = args.path
    with open(path, 'r', encoding='utf-8') as fin:
        result = json.load(fin)
    
    if result['images'][0]['inferResult']  == 'SUCCESS':
        fields = result['images'][0]['fields']
    else:
        fields = []
    
    for field in fields:
        vertices = field['boundingPoly']['vertices']  # [좌상, 우상, 우하, 좌하]
        inferText = field['inferText']
        inferConfidence = field['inferConfidence']
        