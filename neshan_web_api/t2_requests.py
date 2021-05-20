import requests
import json
from pprint import pprint
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Neshan')
    parser.add_argument('-la', '--lat', metavar='LAT', action='store', type=float, required=True,
                        help='arze joghrafiayei')
    parser.add_argument('-ln', '--lng', metavar='LNG', action='store', type=float, required=True,
                        help='toole joghrafiayei')
    args = parser.parse_args()

    search_location_api = "https://api.neshan.org/v2/reverse"
    api_key = "service.GDwNbS3U7svILS8SwBIYqpH5PpL3rrq2Fz9v3kK8"
    params = {
        'lat': args.lat,
        'lng': args.lng,

    }
    resp = requests.get(search_location_api, params=params, headers={'Api-key': api_key})
    pprint(resp.json())
