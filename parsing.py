import argparse
import json
from pprint import PrettyPrinter
from typing import List

pp = PrettyPrinter(indent=2, width=80)


def parse_result(path: str) -> List:
    with open(path, 'r', encoding='utf-8') as fin:
        result = json.load(fin)
    
    if result['images'][0]['inferResult'] == 'SUCCESS':
        fields = result['images'][0]['fields']
    else:
        fields = []
    
    return fields


def simplify_vertices(vertices: List[dict]) -> tuple:
    """Shapely Polygon 요구 형식에 맞도록 Naver OCR boundingPoly 변환

    :param vertices: [{'x':0.0, 'y': 1.0}, ...]
    :return: [(0.0, 1.0), ...]
    """
    return tuple((vertice['x'], vertice['y']) for vertice in vertices)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--path', type=str, help='JSON returned from NaverOCR.')
    args = parser.parse_args()
    
    path = args.path
    fields = parse_result(path)
    
    for field in fields:
        vertices = field['boundingPoly']['vertices']  # [좌상, 우상, 우하, 좌하]
        inferText = field['inferText']
        inferConfidence = field['inferConfidence']
        
        field['boundingPoly'] = simplify_vertices(vertices)
