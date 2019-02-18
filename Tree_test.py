from random import randint
from BST_version_3 import BinaryTreeNode, BinaryTree
# I have to keep the build of lists under 3,000 total
# my computer starts to freak out about memory at 10,000
# it slows at 3000.
# recursion depth happens on count at 2000 items
def test_set():
	oaktree = BinaryTree(50.5)
	for i in range(0, 50):
		oaktree.set(i, 'crunchy leaves')
	assert oaktree._size == 50
	for i in range(50, 100):
		oaktree.set(i, 'acorns')
	assert oaktree._size == 100
	for i in range(0, 50):
		oaktree.set(i, 'gypsy moths')
	assert oaktree._size == 100

def test_count():
	mapletree = BinaryTree(75.5)
	for i in range(0, 100):
		x = randint(1, 100)
		mapletree.set(x, 'climbable')
	assert mapletree._size == mapletree.count()
	for i in range(0, 50):
		x = randint(100, 150)
		mapletree.set(x, 'shade')
	assert mapletree._size == mapletree.count()
	pinetree = BinaryTree(80.5)
	for i in range(0, 160):
		pinetree.set(i, 'christmas')
	assert pinetree.count() == 160
	pinetree.set(161, 'needles')
	assert pinetree.count() == 161

def test_delete():
	oaktree = BinaryTree(50.5)
	for i in range(0, 50):
		oaktree.set(i, 'crunchy leaves')
	pinetree = BinaryTree(80.5)
	for i in range(0, 160):
		pinetree.set(i, 'christmas')
	oaktree.delete(1)
	assert oaktree.count() == 49
	assert oaktree._size == 49
	oaktree.delete(25)
	assert oaktree.count() == 48
	assert oaktree._size == 48
	for i in range(0, 160):
		pinetree.delete(i)
	assert pinetree.count() == 0
	assert pinetree._size == 0
	for i in range(2, 25):
		oaktree.delete(i)
	assert oaktree.count() == 25
	assert oaktree._size == 25
	redwood = BinaryTree(11.5)
	redlist = []
	for i in range(0, 40):
		x = randint(0, 40)
		if x not in redlist:
			redlist.append(x)
		redwood.set(x, 'not 40')
	assert redwood.count != 40
	length_redlist = len(redlist)
	assert redwood._size == length_redlist
	for i in range(0, length_redlist):
		redwood.delete(redlist[i])

	assert redwood._size == 0
	## was a FAIL...
	##  fixed.  was removing the temp.left and temp.right
	## only should remove the temp link that matched the (akey)
	## that we want to delete.
	assert redwood.count() == redwood._size
	rightsided = BinaryTree(5.5)
	righty = []
	for i in range(0, 50):
		rightsided.set(i, "slide to the right.")
		righty.append(i)
	assert len(righty) == rightsided._size
	for i in range(0, 50):
		rightsided.delete(i)
	assert rightsided._size == 0
	leftsided = BinaryTree(100.5)
	lefty = []
	for i in range(0, 50):
		leftsided.set(i, "slide to the left")
		lefty.append(i)
	assert len(lefty) == leftsided._size
	#### random leftsided rightsided

	for i in range(0, 50):
		x = randint(6, 50)
		rightsided.set(x, "one hop this time")
	righty2 = rightsided.make_key_list()
	assert len(righty2) == rightsided._size
	jump_jump = rightsided._size
	for i in range(0, jump_jump):
		x = righty2[i]
		rightsided.delete(x)
	assert rightsided._size == rightsided.count() == 0
	for i in range(0, 50):
		x = randint(0, 90)
		leftsided.set(x, "cha-cha now ya'all.")
	lefty2 = leftsided.make_key_list()
	assert len(lefty2) == leftsided._size
	cha_cha = leftsided._size
	for i in range(0, cha_cha):
		x = lefty2[i]
		leftsided.delete(x)
	assert leftsided._size == leftsided.count() == 0
	###  TEST A LARGE TREE  ###
	rainforest = BinaryTree(500.5)
	for i in range(0, 1000):
		x = randint(0, 1000)
		rainforest.set(x, "oxygen")
	rainy = rainforest.make_key_list()
	assert len(rainy) == rainforest._size
	cha_cha = rainforest._size
	for i in range(0, cha_cha):
		x = rainy[i]
		rainforest.delete(x)
	assert rainforest._size == rainforest.count() == 0


def test_make_list():
	willow = BinaryTree(50.5)
	messy_tree = []
	### willow, lopsidded
	for i in range(0, 50):
		willow.set(i, "weeping")
		messy_tree.append(i)
	will_list = willow.make_key_list()
	willow_size = willow.count()
	assert len(will_list) == willow_size
	for i in range(0, 50):
		assert will_list[i] in messy_tree
	## make_list_ appends from root.left, root.right down the branches
	## the lists will have a different order, root.right will be second in the
	## make_list,  as it will most likely not be the second appended to manual list
	for i in range(0, 50):
		assert messy_tree[i] in will_list
	## silver_spruce more even
	silver_spruce = BinaryTree(40.5)
	decor = []
	for i in range(0, 82):
		silver_spruce.set(i, 'firewood')
		decor.append(i)
	pine = silver_spruce.make_key_list()
	spruce_count = silver_spruce.count()
	assert len(pine) == spruce_count
	for i in range(0, 82):
		assert decor[i] in pine
	for i in range(0, 82):
		assert pine[i] in decor
	### random made even tree
	apple = BinaryTree(30.5)
	pie = []
	for i in range(0, 40):
		x = randint(0, 62)
		apple.set(x, "buggy")
		pie.append(x)
	juice = apple.make_key_list()
	apple_size = apple.count()
	assert apple_size == len(juice)
	for i in range(0, apple_size):
		assert juice[i] in pie
		assert pie[i] in juice

def test_get():
	oaktree = BinaryTree(-511.5)
	oaklist = []
	oaktree.set(-211, "spam1")
	oaklist.append(-211)
	oaktree.set(-739, "spam2")
	oaklist.append(-739)
	oaktree.set(-279, "spam3")
	oaklist.append(-279)
	oaktree.set(-417, "spam4")
	oaklist.append(-417)
	oaktree.set(-419, "spam5")
	oaklist.append(-419)
	oaktree.set(-969, "spam6")
	oaklist.append(-969)
	oaktree.set(-14, "spam7")
	oaklist.append(-14)
	oaktree.set(-715, "spam8")
	oaklist.append(-715)
	oaktree.set(-351, "spam9")
	oaklist.append(-351)
	oaktree.set(-349, "spam10")
	oaklist.append(-349)
	oaktree.set(-893, "spam11")
	oaklist.append(-893)
	oaktree.set(-672, "spam12")
	oaklist.append(-672)
	oaktree.set(-455, "spam13")
	oaklist.append(-455)
	oaktree.set(-21, "spam14")
	oaklist.append(-21)
	oaktree.set(-463, "spam15")
	oaklist.append(-463)
	######################
	oaktree.set(-321, "spam16")
	oaklist.append(-321)
	oaktree.set(-6, "spam17")
	oaklist.append(-6)
	oaktree.set(-741, "spam18")
	oaklist.append(-741)
	oaktree.set(-494, "spam19")
	oaklist.append(-494)
	oaktree.set(-595, "spam20")
	oaklist.append(-595)
	oaktree.set(-452, "spam21")
	oaklist.append(-452)
	oaktree.set(-36, "spam22")
	oaklist.append(-36)
	oaktree.set(-358, "spam23")
	oaklist.append(-358)
	oaktree.set(-796, "spam24")
	oaklist.append(-796)
	oaktree.set(-625, "spam25")
	oaklist.append(-625)
	oaktree.set(-61, "spam26")
	oaklist.append(-61)
	oaktree.set(-329, "spam27")
	oaklist.append(-329)
	############################
	oaktree.set(-35, "spam28")
	oaklist.append(-35)
	oaktree.set(-106, "spam29")
	oaklist.append(-106)
	oaktree.set(-393, "spam30")
	oaklist.append(-393)
	oaktree.set(-57, "spam31")
	oaklist.append(-57)
	oaktree.set(-314, "spam32")
	oaklist.append(-314)
	oaktree.set(-51, "spam33")
	oaklist.append(-51)
	oaktree.set(-62, "spam34")
	oaklist.append(-62)
	oaktree.set(-689, "spam35")
	oaklist.append(-689)
	oaktree.set(-366, "spam36")
	oaklist.append(-366)
	oaktree.set(-344, "spam37")
	oaklist.append(-344)
	oaktree.set(-463, "spam38")
	oaklist.append(-463)
	oaktree.set(-663, "spam39")
	oaklist.append(-663)
	oaktree.set(-318, "spam40")
	oaklist.append(-318)
	assert oaktree.get(-318) == "spam40"
	assert oaktree.get(100) == None
	assert oaktree.get(-393) == "spam30"
	assert oaktree.get(-969) == "spam6"
	assert oaktree.get(-6) =="spam17"
	assert oaktree.get(-211) == "spam1"
	assert oaktree.get(-279) == "spam3"
	assert oaktree.get(-969) == "spam6"
	for akey in oaklist:
		assert oaktree.get(akey) != None
	oaktree.delete(-211)
	oaktree.delete(-739)
	assert oaktree.get(-211) == None
	assert oaktree.get(-739) == None
