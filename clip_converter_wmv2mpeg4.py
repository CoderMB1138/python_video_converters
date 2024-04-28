from moviepy.editor import VideoFileClip
import os

def convert_to_mp4(wmv_file, output_folder):
    try:
        clip = VideoFileClip(wmv_file)
        mp4_file = os.path.splitext(os.path.basename(wmv_file))[0] + ".mp4"
        output_path = os.path.join(output_folder, mp4_file)
        clip.write_videofile(output_path, codec="libx264")
        clip.close()
        print(f"{wmv_file} converted successfully to {mp4_file}")
    except Exception as e:
        print(f"Error converting {wmv_file}: {e}")

def batch_convert_to_mp4(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".wmv"):
                wmv_file = os.path.join(root, file)
                convert_to_mp4(wmv_file, output_folder)

if __name__ == "__main__":
    input_folder = "./clips"  # Update this with your input folder containing WMV files
    output_folder = "./output"  # Update this with your desired output folder for MP4 files
    batch_convert_to_mp4(input_folder, output_folder)

