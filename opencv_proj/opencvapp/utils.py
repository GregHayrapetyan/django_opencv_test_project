import cv2
import numpy as np
from django.conf import settings
import base64
from random import randint
import asyncio

def opencv_func(video_file):
	video = cv2.VideoCapture(video_file)
	logo_path = str(settings.BASE_DIR) + '/media/logo/logo.png'
	video_path = str(settings.BASE_DIR) + '/media/finished_videos/'
	logo = cv2.imread(logo_path)
	size = 100
	logo = cv2.resize(logo, (size, size))
	img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
	ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
	frame_width = int(video.get(3))
	frame_height = int(video.get(4))
	sized = (frame_width, frame_height)
	num = randint(1, 999999)
	message = str(num)
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	filename = str(base64_bytes.decode('ascii')) + '.avi'
	path = video_path + f'{filename}'
	result = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'MJPG'),20, sized)
	while True:
		ret, frame = video.read()
		if ret:
			roi = frame[-size-10:-10, -size-10:-10]
			roi[np.where(mask)] = 0
			roi += logo
			result.write(frame)
		else:
			break

	video.release()
	result.release()
	cv2.destroyAllWindows()
	return filename