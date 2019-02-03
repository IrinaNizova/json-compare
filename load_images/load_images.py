import argparse
import os
import requests
import io
import builtins

ip = 'http://localhost'
parser = argparse.ArgumentParser(description='Image loader')
parser.add_argument('path', help='Path to folder')
parser.add_argument('--ip', help='Server ip')
args = parser.parse_args()
if args.ip:
	ip = args.ip
if not os.path.isdir(args.path):
	print('It is not a directory')
else:
	for f in os.listdir(args.path):
		full_path = os.path.join(args.path, f)
		if os.path.isfile(full_path) and os.path.splitext(f)[-1].lower() in ('.jpg', '.png', '.jpeg'):
			try:
				out = open(full_path, 'rb')
				r = requests.post(ip + '/image', data={'file': f, 'data': out.read()})
				if r.status_code >= 400:
					print('{} did not load. Code {}'.format(f, r.status_code))
			finally:
				out.close()
			