import json
import os

def save_result(request_id, data):
    os.makedirs('reports', exist_ok=True)
    with open(f'reports/{request_id}.json', 'w') as f:
        json.dump(data, f, indent=2)