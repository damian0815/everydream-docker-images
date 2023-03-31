import argparse
import traceback
import os
from huggingface_hub import HfApi

parser = argparse.ArgumentParser()
parser.add_argument("local_path")
parser.add_argument("--repo_id", required=True)
parser.add_argument("--remote_path", default=None)

args = parser.parse_args()

api = HfApi()
try:
    api.create_repo(args.repo_id)
except Exception as e:
    traceback.print_exc()

if os.path.isfile(args.local_path):
    api.upload_file(
            path_or_fileobj=f,
            path_in_repo=args.remote_path or args.local_path,
            repo_id=args.repo_id,
            repo_type="model",
            create_pr=True,
            )
elif os.path.isdir(args.local_path):
    api.upload_folder(
            folder_path=args.local_path,
            path_in_repo=args.remote_path,
            repo_id=args.repo_id,
            create_pr=True
            )
else:
    print(f"Path {args.local_path} not found")

