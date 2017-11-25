import json






parsed = json.loads(your_json)
print json.dumps(parsed, indent=4, sort_keys=True)