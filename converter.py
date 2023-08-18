from flask import Flask, render_template, request
import moviepy.editor as mp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'video' not in request.files:
        return "No file part"
    
    video_file = request.files['video']
    if video_file.filename == '':
        return "No selected file"
    
    video_path = f"uploads/{video_file.filename}"
    video_file.save(video_path)

    # Convert the video
    clip = mp.VideoFileClip(video_path)
    converted_path = f"converted/{video_file.filename.replace('.','_')}.mp4"
    clip.write_videofile(converted_path)
    clip.close()

    return converted_path

if __name__ == '__main__':
    app.run(debug=True)
