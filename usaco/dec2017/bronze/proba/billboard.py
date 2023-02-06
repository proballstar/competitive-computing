fin = open("billboard.in", "r")
fout = open("billboard.out", "w")
    
ax1, ay1, ax2, ay2 = map(int, fin.readline().strip().split(" "))

bx1, by1, bx2, by2 = map(int, fin.readline().strip().split(" "))

tx1, ty1, tx2, ty2 = map(int, fin.readline().strip().split(" "))

def inter_area(s1, s2) -> int:
	bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
	bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]
	
	return (
		(min(tr_a_x, tr_b_x) - max(bl_a_x, bl_b_x))
		* (min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y))
	)

def intersect(s1, s2) -> bool:
	bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
	bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]
	
	# no overlap
	if (bl_a_x >= tr_b_x or tr_a_x <= bl_b_x
			or bl_a_y >= tr_b_y or tr_a_y <= bl_b_y):
		return False
	else:
		return True


# Area for each billboard
total_intersect = 0

a_p = [ax1, ay1, ax2, ay2]
b_p = [bx1, by1, bx2, by2]
t_p = [tx1, ty1, tx2, ty2]

a_area = abs(ax2-ax1) * abs(ay2-ay1)
b_area = abs(bx2-bx1) * abs(bx2-bx1)

total_intersect = 0

for x in [a_p, b_p]:
    if intersect(t_p, x):
        total_intersect += inter_area(x, t_p)

total_area = a_area + b_area

fout.write(f"{total_area-total_intersect}\n")