import random
import raw_data_to_json
from PIL import Image, ImageDraw, ImageFont
import os
import json


raw_data_to_json.create_json_from_raw_data()


def gen_text_image(messages):
    random_pp = random.randint(1, 25)

    width, height = 3000, 3000
    background_color = (54, 57, 63)
    font_color = (220, 220, 220)
    timestamp_color = (150, 150, 150)
    font_path = "gg sans Regular.ttf"
    bold_font_path = "gg sans Bold.ttf"
    avatar_size = 40

    icon_folder = "icons"
    if not os.path.exists(icon_folder):
        print(f"Utwórz folder '{icon_folder}' i dodaj avatary użytkowników (np. Janek.png, Kasia.png).")
        exit()

    font_text = ImageFont.truetype(font_path, 16)
    font_date = ImageFont.truetype(bold_font_path, 10)
    font_name = ImageFont.truetype(bold_font_path, 16)

    img = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(img)

    y_offset = 20
    padding = 10
    max_width = 0

    for message in messages:
        user = message["user"]
        text = message["content"]
        timestamp = message["timestamp"]

        avatar_path = os.path.join(icon_folder, f"{user}.png")
        if os.path.exists(avatar_path):
            avatar = Image.open(avatar_path).resize((avatar_size, avatar_size))
        else:
            avatar = Image.open(os.path.join(icon_folder, 'random', f'{random_pp}.png')).resize((avatar_size, avatar_size))

        avatar = avatar.convert("RGBA")
        mask = Image.new("L", avatar.size, 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_center = (avatar.width // 2, avatar.height // 2)
        mask_radius = min(avatar.width, avatar.height) // 2
        mask_draw.ellipse((mask_center[0] - mask_radius, mask_center[1] - mask_radius, mask_center[0] + mask_radius, mask_center[1] + mask_radius), fill=255)

        avatar = Image.composite(avatar, Image.new("RGBA", avatar.size, background_color), mask)

        img.paste(avatar, (padding, y_offset))

        draw.text((padding + avatar_size + 10, y_offset - 5), user, font=font_name, fill=font_color)

        user_text_bbox = draw.textbbox((0, 0), user, font=font_name)
        user_text_width = user_text_bbox[2] - user_text_bbox[0]

        draw.text(
            (padding + avatar_size + 15 + user_text_width, y_offset + 1),
            timestamp,
            font=font_date,
            fill=timestamp_color
        )

        text_bbox = draw.textbbox((0, 0), text, font=font_text)
        text_width = text_bbox[2] - text_bbox[0]

        max_width = max(max_width, padding + avatar_size + 10 + user_text_width + 15 + text_width)

        y_offset += avatar_size // 2
        draw.text((padding + avatar_size + 10, y_offset), text, font=font_text, fill=font_color)


        y_offset += avatar_size + 10

        if y_offset > height - 50:
            break

    y_offset += 50
    max_width += 50

    img = img.crop((0, 0, max_width, y_offset))

    img.save(os.path.join('output', f'screen{random.randint(10000, 99999)}.png'))


with open("logi.json", "r", encoding="utf-8") as file:
    logs = json.load(file)
    for messages in logs['messages']:
        gen_text_image(messages)
print("Done. Consider tipping. LTC: ")
print("LgCoPoKDzE22pn2mZj3opd5a9sGJzc35zB")
input()
