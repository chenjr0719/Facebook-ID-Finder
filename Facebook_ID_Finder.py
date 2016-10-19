import requests, re, argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument("target", help="Set the target.")

args = parser.parse_args()

target = args.target
result = requests.get(target)

if result.ok:
    result = result.text
    profile_id = re.search(r"profile_id=[0-9]+", result)
    profile_id = re.search(r"[0-9]+", profile_id.group()).group() if profile_id else 'permission denied'
    print(profile_id)
else:
    print('The target is invalid page.')


