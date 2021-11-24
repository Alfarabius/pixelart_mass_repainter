import sys

import _utils
import mass_repainter

RED = 2
GREEN = 1
BLUE = 0


def quit_prg():
	print(_utils.TermColor.RESET + 'Buy!')
	sys.exit()


def repaint_img(img, colors, func, args=None):
	new_colors = set()

	for element in img:
		for sub in element:
			if tuple(sub) in colors:
				if args is None:
					new_colors.add(tuple(func(sub)))
				else:
					new_colors.add(tuple(func(sub, *args)))
				_utils.loading()

	return list(new_colors)


def main():
	redrawer = mass_repainter.MassRedrawer()
	redrawer.run()


def make_brighter_tone_bgr(color, power):
	for i in range(3):
		color[i] = color[i] + power if color[i] < 256 - power else 255
	return color


def make_darker_tone_bgr(color, power):
	for i in range(3):
		color[i] = color[i] - power if color[i] > power else 0
	return color


def red_to_green(color):
	color[RED], color[GREEN] = color[GREEN], color[RED]
	return color


def red_to_blue(color):
	color[RED], color[BLUE] = color[BLUE], color[RED]
	return color


def any_to_black(color):
	tone = (int(color[0]) + int(color[1]) + int(color[2])) // 3
	color[0], color[1], color[2] = tone, tone, tone
	return color


def any_to_yellow(color):
	dominant = sorted(color[:-1], reverse=True)
	tone = (int(dominant[0]) + int(dominant[1])) // 2
	color[RED], color[GREEN] = tone, tone
	return color


def any_to_red(color):
	dominant = sorted(color[:-1], reverse=True)
	color[RED] = dominant[0]
	return color


if __name__ == '__main__':
	main()
