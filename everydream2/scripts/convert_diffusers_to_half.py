
import argparse
import torch, diffusers
import tqdm.auto

def convert_to_fp16(in_path: str, out_path: str): 
    print("loading", in_path)
    pipe = diffusers.StableDiffusionPipeline.from_pretrained(in_path)
    print("converting to float16...")
    pipe = pipe.to(torch.float16)
    print("saving", out_path)
    pipe.save_pretrained(out_path)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("in_path", help="input folder")
    parser.add_argument("out_path", help="output folder")
    args = parser.parse_args()

    convert_to_fp16(args.in_path, args.out_path)


