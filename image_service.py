from pathlib import Path
from datetime import datetime

import torch
from diffusers import StableDiffusionPipeline


MODEL_ID = "runwayml/stable-diffusion-v1-5"
OUTPUT_DIR = Path("outputs/images")

_DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
_PIPELINE = None


def _load_pipeline():
    global _PIPELINE

    if _PIPELINE is None:
        torch_dtype = torch.float16 if _DEVICE == "cuda" else torch.float32

        _PIPELINE = StableDiffusionPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch_dtype,
            safety_checker=None,
            requires_safety_checker=False,
        )

        _PIPELINE = _PIPELINE.to(_DEVICE)

        if _DEVICE == "cuda":
            _PIPELINE.enable_attention_slicing()

    return _PIPELINE


def generate_image(
    image_prompt: str,
    scene_number: int = 1,
    width: int = 512,
    height: int = 512,
    num_inference_steps: int = 25,
    guidance_scale: float = 7.5,
    negative_prompt: str = (
        "blurry, low quality, worst quality, distorted, deformed, "
        "extra fingers, extra limbs, bad anatomy, text, watermark, logo"
    ),
) -> str:
    if not image_prompt or not image_prompt.strip():
        raise ValueError("image_prompt 不能为空。")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pipe = _load_pipeline()

    image = pipe(
        prompt=image_prompt,
        negative_prompt=negative_prompt,
        width=width,
        height=height,
        num_inference_steps=num_inference_steps,
        guidance_scale=guidance_scale,
    ).images[0]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"scene_{scene_number}_{timestamp}.png"
    file_path = OUTPUT_DIR / file_name

    image.save(file_path)

    return str(file_path)


def generate_scene_image(scene: dict) -> str:
    scene_number = scene.get("scene_number", 1)
    image_prompt = scene.get("image_prompt", "")

    return generate_image(
        image_prompt=image_prompt,
        scene_number=scene_number,
    )