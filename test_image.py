from image_service import generate_image


def main():
    image_prompt = (
        "A cute kitten sitting by the window, soft golden sunlight, "
        "warm cozy home, detailed fur, cinematic lighting, high quality"
    )

    image_path = generate_image(
        image_prompt=image_prompt,
        scene_number=1,
        width=512,
        height=512,
        num_inference_steps=25,
        guidance_scale=7.5,
    )

    print("图片生成成功！")
    print("保存路径：", image_path)


if __name__ == "__main__":
    main()