import os
import re
import colorsys
import xml.etree.ElementTree as ET

# Adjustments
BRIGHTNESS_FACTOR = 0.85      # Decrease brightness by 10%
SATURATION_FACTOR = 1.75      # Increase saturation by 20%
CONTRAST_FACTOR = 1.25        # Increase contrast by 10%

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16)/255.0 for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*(int(max(0, min(1, c)) * 255) for c in rgb))

def adjust_color(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    h, l, s = colorsys.rgb_to_hls(r, g, b)

    # Apply saturation and brightness changes
    s = max(0, min(1, s * SATURATION_FACTOR))
    l = max(0, min(1, l * BRIGHTNESS_FACTOR))

    # Convert back to RGB
    r, g, b = colorsys.hls_to_rgb(h, l, s)

    # Apply contrast (simple method: move away from 0.5)
    def apply_contrast(c):
        return max(0, min(1, 0.5 + CONTRAST_FACTOR * (c - 0.5)))

    r, g, b = apply_contrast(r), apply_contrast(g), apply_contrast(b)
    return rgb_to_hex((r, g, b))

def process_svg(file_path):
    ET.register_namespace('', "http://www.w3.org/2000/svg")
    tree = ET.parse(file_path)
    root = tree.getroot()

    def update_color(attr_value):
        hex_match = re.fullmatch(r"#([0-9a-fA-F]{6})", attr_value)
        if hex_match:
            return adjust_color(attr_value)
        return attr_value  # Keep as-is if not a valid hex

    for elem in root.iter():
        for attr in ['fill', 'stroke', 'stop-color']:
            if attr in elem.attrib:
                elem.attrib[attr] = update_color(elem.attrib[attr])

    tree.write(file_path)

def process_folder(folder_path):
    import os
    for filename in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, filename)) is True:
            print("Yes Dir:")
            continue;
        print(filename)
        name, ext = filename.rsplit('.', maxsplit=1)
        if ext.startswith("svg"):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing: {filename}")
            process_svg(file_path)

if __name__ == "__main__":
    import sys
    import shutil
    import os
    if len(sys.argv) != 2:
        print("Usage: python enhance_svg_colors.py <svg_folder_path>")
        exit(1)

    folder = sys.argv[1]
    path, name = folder.rsplit('/', maxsplit=1)
    new_name = '%s/%s%s' % (path, name, 'old')
    shutil.copytree(folder, new_name)
    process_folder(folder)
