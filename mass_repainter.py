import inspect
import json
import os
import shutil
import cv2.cv2 as cv

from inspect import signature

import _utils
import color_utils


class MassRedrawer:
	SRC = './source/'
	RESULT = './result/'
	TMP = './tmp/'

	def __init__(self):
		os.system('')

		if not os.path.exists(self.SRC):
			os.mkdir(self.SRC)

		if not os.path.exists(self.RESULT):
			os.mkdir(self.RESULT)

		if not os.path.exists(self.TMP):
			os.mkdir(self.TMP)

		self.funcs = {
			0: color_utils.quit_prg,
			1: color_utils.red_to_green,
			2: color_utils.make_brighter_tone_bgr,
			3: color_utils.make_darker_tone_bgr,
			4: color_utils.any_to_black,
			5: color_utils.red_to_blue,
			6: color_utils.any_to_yellow,
			7: color_utils.any_to_red,
			8: self.move_res_to_src,
			9: self._source_palette_to_json
		}

		self.colors_to_change = self.__get_colors_to_change()
		self.changed_colors = None

		self.files = os.listdir(self.SRC)

		for file in self.files:
			shutil.copy2(self.SRC + file, self.TMP)

	def run(self):
		while True:
			arg = None

			_utils.start_menu()
			func = self.funcs.get(_utils.get_menu_choice(self.funcs))

			if func.__name__ == 'quit_prg' or inspect.ismethod(func):
				func()
				continue

			if len(signature(func).parameters) > 1:
				arg = [_utils.user_input('Enter the value: ', 'Not correct value')]

			for file in self.files:
				img = cv.imread(self.SRC + file, cv.IMREAD_UNCHANGED)
				self.changed_colors = color_utils.repaint_img(img, self.colors_to_change, func, arg)
				cv.imwrite(self.RESULT + file, img)

	def _update(self):
		self.files = os.listdir(self.SRC)

	def move_res_to_src(self):
		if self.changed_colors is None:
			return

		if not os.path.exists(self.TMP):
			os.mkdir(self.TMP)

		res_files = os.listdir(self.RESULT)
		for file in res_files:
			shutil.copy2(self.RESULT + file, self.SRC)

		if self.changed_colors is not None:
			self.colors_to_change = self.changed_colors

	@staticmethod
	def __get_colors_to_change():
		colors_to_change = []

		with open('colors_to_change.json', 'r') as file:
			reader = json.load(file).get('colors')
			for color in reader:
				colors_to_change.append(tuple(color))

		return colors_to_change

	def _source_palette_to_json(self):
		palette = set()

		for file in self.files:
			img = cv.imread(self.SRC + file, cv.IMREAD_UNCHANGED)
			for element in img:
				for color in element:
					palette.add(tuple(map(int, color)))

		with open('palette.json', 'w') as write_file:
			json.dump({"colors": sorted(palette, reverse=True)}, write_file, indent=4)
