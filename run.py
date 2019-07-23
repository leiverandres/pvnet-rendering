import torch
import argparse

from blender.render_utils import Renderer, YCBRenderer
from config import cfg
from fuse.fuse import run

parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["rendering", "fuse"])
parser.add_argument("--model_type", type=str, default="cat")
args = parser.parse_args()


def run_rendering():
    # YCBRenderer.multi_thread_render()
    # renderer = YCBRenderer('037_scissors')
    renderer = Renderer(args.model_type)
    renderer.run()


def run_fuse():
    run()


if __name__ == "__main__":
    globals()["run_" + args.type]()
    if args.type == "rendering":
        run_rendering()
    elif args.type == "fuse":
        run_rendering()
    else:
        raise ValueError("Rendering option not implemented")
