import os
import shutil


source_path = 'path_to_the_video_folder' 
# dest_path = 'C:\\Users\\d33ps3curity\\Desktop\\test\\new_videos'
# source_path = 'C:\\Users\\d33ps3curity\\Desktop\\test\\test_videos'

dir_str = os.listdir(source_path)

dir_path_list = []

for dir_path in dir_str:
	dir_path_list.append(os.path.join(source_path, dir_path))

 

dir_dict = {}

for dir_path in dir_path_list:
	dir_dict[dir_path] = os.listdir(dir_path)


final_list = []
for directory, video in dir_dict.items():
	for text in video:
		# if '.pdf' in text:
		# 	final_list.append(os.path.join(directory, text)) 
		if '(' not in text:
			if '.mp4' in text:
				final_list.append(os.path.join(directory, text))
			
			if '.mkv' in text:
			  	final_list.append(os.path.join(directory, text))  		


# for video in final_list:
# 	try:
# 		if os.path.exists(video):
# 			shutil.move(video, dest_path)
# 	except FileNotFoundError:
# 		pass
