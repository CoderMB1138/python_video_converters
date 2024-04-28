from moviepy.editor import VideoFileClip
import os

def convert_to_mpeg4(mpg_file, output_folder):
    try:
        clip = VideoFileClip(mpg_file)
        mpeg4_file = os.path.splitext(os.path.basename(mpg_file))[0] + ".mp4"
        output_path = os.path.join(output_folder, mpeg4_file)
        clip.write_videofile(output_path, codec="mpeg4")
        clip.close()
        print(f"{mpg_file} converted successfully to {mpeg4_file}")
    except Exception as e:
        print(f"Error converting {mpg_file}: {e}")

def batch_convert_to_mpeg4(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".mpg"):
                mpg_file = os.path.join(root, file)
                convert_to_mpeg4(mpg_file, output_folder)

if __name__ == "__main__":
    input_folder = "./clips"  # Update this with your input folder containing MPG files
    output_folder = "./output"  # Update this with your desired output folder for MPEG4 files
    batch_convert_to_mpeg4(input_folder, output_folder)

