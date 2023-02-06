def area(bl_x: int, bl_y: int, tr_x: int, tr_y: int) -> int:
	length = tr_y - bl_y
	width = tr_x - bl_x
	return length * width