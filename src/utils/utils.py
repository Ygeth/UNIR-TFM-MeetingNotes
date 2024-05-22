import json
def dict2Json(dict):
    return json.dumps(dict, indent=4)
  
def json2Dict(jsonStr):
    return json.loads(jsonStr)