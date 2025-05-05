import cv2

def get_video_fps(video_path):
    # Intentional error: misspelled variable 'video'
    video = cv2.VideoCapture(vido_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    return fps

def main():
    input_video_path = 'test.mp4'
    output_video_path = 'output.mp4'

    # Capture video
    video = cv2.VideoCapture(input_video_path)
    fps = get_video_fps(input_video_path)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (int(video.get(3)), int(video.get(4))))

    # Main processing loop
    while True:
        ret, frame = video.read()

        # Check if frame is read correctly
        if not ret:
            break

        # Display the FPS on the frame
        # Intentional error: incorrect function name 'putText'
        cv2.putText(frame, 'FPS: {}'.format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Write the frame
        out.write(frame)

    # Release everything when job is finished
    video.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()