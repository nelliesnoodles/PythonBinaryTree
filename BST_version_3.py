from random import randint

""" PRIMARY BRANCH :  The first branch from the root_node
 that either points to a left, or right node. Root Node
 pointers need to be changed if a primary is being deleted.

 LEAF: Leaves are nodes with no children, left=None, right=None
 Can simple replaced with 'None'

 On the left side of the root, the right branch "greater than"
 will terminate as it reaches the same value as root_nodes key.
 On the right side of root, the left branch "less than" will terminate
 as it approaches the value as root_nodes key.
 Right sides "greater than" branch can become limitless,
 and likewise Left sides "less than" can be potentially limitless<
 depending on if a key value can be negative, or go below 0.
 So the best option when placing child nodes is to find the last
 node of a branch that we know has to terminate.  Otherwise, we might
 be searching through a very large branch to find the last node.

"""


class BinaryTreeNode(object):
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        nleft = self.left and self.left.value or None
        nright = self.right and self.right.value or None
        return f"{nleft} <--- ( {self.key} : {self.value} ) ---> {nright}"

class BinaryTree(object):
    def __init__(self, median):
        self.median = median
        self.root_node = BinaryTreeNode(self.median, 'binary_root_node', None, None)
        self._size = 0

    def set(self, akey, value):
        """
            find proper placement in the tree for the given key:value pair
            *replace value if key exists
            *add node when in the proper place
             Node = [((key)), ((value)), ((left)) 'less than', ((right)) 'greater than']
        """

        if akey < self.median:
            # key is less then root, go left
            east = self.root_node.left


            if not east:
                # east == None
                #  [None<---- newnode _---> None][<--left-- root --right-->]
                newnode = BinaryTreeNode(akey, value, None, None)
                self.root_node.left = newnode
                self._size += 1
            else:
                #east branch (possible parent) exists

                while east:
                    # if akey exists, replace value
                    if akey == east.key:
                        east.value = value
                        break
                    elif east.key < akey:
                        # if akey is greater, go right
                        if east.right == None:
                            # dead end, place node
                            newnode = BinaryTreeNode(akey, value, None, None)
                            east.right = newnode
                            self._size += 1
                            break
                        else:
                            #Not a dead end continue
                            east = east.right
                    else:
                        # akey is less then branch key

                        if east.left == None:
                            #dead end place node
                            newnode = BinaryTreeNode(akey, value, None, None)
                            east.left = newnode
                            self._size += 1
                            break
                        else:
                            #not a dead end continue
                            east = east.left

        if akey > self.median:
            west = self.root_node.right

            if not west:
                # [<---- root --right-->][None<---- newnode _---> None]
                # West branch is empty, place node
                newnode = BinaryTreeNode(akey, value, None, None)
                self.root_node.right = newnode
                self._size += 1
            else:
                # west branch is not empty, search for placement
                while west:
                    ########################
                    if akey == west.key:
                        west.value = value
                        break
                    elif west.key < akey:
                        if west.right == None:
                            newnode = BinaryTreeNode(akey, value, None, None)
                            west.right = newnode
                            self._size += 1
                            break
                        else:
                            west = west.right
                    else:

                        if west.left == None:
                            newnode = BinaryTreeNode(akey, value, None, None)
                            west.left = newnode
                            self._size += 1
                            break
                        else:
                            west = west.left

    def get(self, akey):
        node = self.root_node
        if akey < self.median:
            node = node.left
            while node:

                if akey == node.key:
                    return node.value
                else:
                    if akey < node.key:
                        node = node.left
                    else:
                        node = node.right
        else:
            node = node.right
            while node:
                if akey == node.key:
                    return node.value
                else:
                    if akey < node.key:
                        node = node.left
                    else:
                        node = node.right

    def _find_bottom_left(self, node, newleaf):
        """

        We want the left most leaf of a the node's PRIMARY
        right branch.

        """
        # change this to recurrsion when able
        while node != None:
          if node.left == None:
              node.left = newleaf
              break
          else:
              node = node.left

    def _find_bottom_right(self, node, newleaf):
        """

        We want the right most leaf of a the node's PRIMARY
        left branch.

        """
        # change this to recurrsion when able
        while node != None:
          if node.right == None:
              node.right = newleaf
              break
          else:
              node = node.right


    def _delete_node(self, node, primaryleft=False, primaryright=False):
        """
        return the replacement node, and wether or not the node is
        the primary branch of the root_node
        root_node primaries are changed in this function
        """
        #print('activating _delete_node(node)')
        root_left = self.root_node.left
        root_right = self.root_node.right
        primary_branch = False

        # check if it is LEAF
        # LEAF's do not need the limited branch involved
############ NO child nodes #############
        if node.right == None and node.left == None:
            #node_key = node.key
            #print("deleting LEAF: ", node_key)
            # check if it is a Primary Branch
            if node == root_left:
                self.root_node.left = None
                primary_branch = True

            elif node == root_right:
                self.root_node.right = None
                primary_branch = True

            # return None for all other replacements that are not primary branches
            # PRIMARY BRANCH LEAF is simply set to None in the Root_node
            return None, primary_branch

        # see which side has a child node
######## there is no right child ############
        elif node.right == None and node.left != None:
            #print("empty right child = ", node.key)
            # empty right node, left becomes replacement
            # Empty slots do not require limited or terminated branches
            replacement = node.left

            if node == root_left:
                self.root_node.left = replacement
                primary_branch = True
            elif node == root_right:
                self.root_node.right = replacement
                primary_branch = True

            return replacement, primary_branch
############### There is no left child ###########
        elif node.right != None and node.left == None:
            #print("empty left child = ", node.key)
            # empty left slot
            # limited branch not required empty slot
            replacement = node.right
            if node == root_left:
                self.root_node.left = replacement
                primary_branch = True
            elif node == root_right:
                self.root_node.right = replacement
                primary_branch = True

            return replacement, primary_branch
########  TWO child nodes are present #############
        elif primaryleft == True:
            #print("primaryleft is True: ", node.key)
            # if on the left side of root, left branches are possibly
            # limitless.  We want to find the bottom of the right node
            # the right node branch has to terminate at the limit which will
            # be the root_nodes value

            left_key = node.left.key
            left_value = node.left.value
            if node.left.left != None:
                left_left = node.left.left
            else:
                left_left = None
            if node.left.right != None:
                left_right = node.left.right
            else:
                left_right = None


            newnode = BinaryTreeNode(left_key, left_value, left_left, left_right)
            right_branch = node.right
            # left PRIMARY branch, find the limited right branch bottom
            # place newnode (left child) there with _find_bottom_right()
            ### find LEAF node on the left most of the right node
            self._find_bottom_left(right_branch, newnode)

            replacement = node.right

            # We are on the left side of the root
            if node == root_left:
                self.root_node.left = replacement
                primary_branch = True


            return replacement, primary_branch

        elif primaryright == True:
            #print("primaryright is True: ", node.key)
            # this is on the right side of root.
            # right branches are potentially limitless
            # find the bottom of left branch because it has a limit
            # that is where right child should go (newnode)
            # replacement will be the left child

            right_key = node.right.key
            right_value = node.right.value
            if node.right.left != None:
                right_left = node.right.left
            else:
                right_left = None
            if node.right.right != None:
                right_right = node.right.right
            else:
                right_right = None

            newnode = BinaryTreeNode(right_key, right_value, right_left, right_right)
            left_branch = node.left
            # We are on the RIGHT branch.
            # find the bottom most right node of the left branch
            # move the right node down
            self._find_bottom_right(left_branch, newnode)

            replacement = node.left

            # Take care of PRIMARY branches, change root_nodes pointer
            # we are on the right branch of root

            if node == root_right:
                self.root_node.right = replacement
                primary_branch = True

            return replacement, primary_branch

        else:
            #do nothing:
            node_type = type(node)
            print("else clause of delete node helper activated\n No conditions met")
            print("node type = ", node_type)
            raise ValueError






    def delete(self, akey):
        """Remove any key;Value from tree, and replace it with proper
           branch/parent  or leaf where necessary
           replacement nodes are given when applicable,
           they are modified to contain all branch leaves in _delete_node
           Primary branch Node, root left, root right are modified in _delete_node"""
        print(" -------delete called on\n\t\t", akey)
        if akey < self.median:
            east = self.root_node.left

            if not east:
                # do nothing
                # if east branch does not exist, key does not exist
                #print('key not found: ', akey)
                return None
            else:
                #run loop to find node
                node = east
                current = node
                #print('else clause of delete activated less then median')
                while node != None:
                    #print('while loop -- EAST')
                    if node.key == akey:
                        newnode, primary = self._delete_node(node, primaryleft=True)
                        if newnode == None and primary == False:
                            # It is a leaf, simply make pointer None
                            if current.left == node:
                                current.left = None
                            if current.right == node:
                                current.right = None
                            self._size -= 1
                            break
                        elif newnode != None and primary == False:
                            # It has children, Not a leaf, and not a Primary
                            node.key = newnode.key
                            node.value = newnode.value
                            node.left = newnode.left
                            node.right = newnode.right

                            #print("deleting")
                            self._size -= 1
                            break
                        elif primary == True:
                            # this was a primary node branch
                            # _delete_node has replaced, removed necessary elements
                            self._size -= 1
                            break
                        else:
                            print("else clause, while loop east of delete.")
                            #print('match found, nothing deleted')
                            break
                    elif node.key > akey:
                        #print("going left, node key is less then akey")
                        current = node
                        node = node.left
                    else:
                        #print('going right, node key = ', node.key)
                        current = node
                        node = node.right

        if akey > self.median:
            west = self.root_node.right

            if not west:
                print("NO west branch:", node.key)
                # do nothing
                # if west branch does not exist, key does not exist
                return None
            else:
                #run loop to find node
                node = west
                current = node
                #print("WEST DELETE LOOP FOR:", node.key)
                #print('else clause of delete activated more then median')
                while node != None:
                    #print('while loop -- WEST')
                    if node.key == akey:
                        newnode, primary = self._delete_node(node, primaryright=True)
                        print("deleting a West node:", node.key)
                        if newnode == None and primary == False:
                            #print("deleting a West node:", node.key)
                            if current.left == node:
                                current.left = None
                            if current.right == node:
                                current.right = None
                            self._size -= 1
                            break
                        elif newnode != None and primary == False:
                            node.key = newnode.key
                            node.value = newnode.value
                            node.left = newnode.left
                            node.right = newnode.right

                            #print("deleting")
                            self._size -= 1
                            break
                        elif primary == True:
                            # this was a primary node branch
                            # _delete_node has replaced, removed necessary elements
                            print("primary :", node.key)
                            self._size -= 1
                            break
                        else:
                            print('else clause in while loop West of delete.')
                            #print('match found, nothing deleted')
                            break
                    elif node.key > akey:
                        #print("going left, node key is greater then akey")
                        current = node
                        node = node.left
                    elif node.key < akey:
                        #print('going right, node key is less then akey')
                        current = node
                        node = node.right
                    else:
                        print("~~~~~~~~~~~~~\n")
                        print("\t\tnode not found!")
                        break




    def dump(self):

        west = self.root_node.right
        east = self.root_node.left
        if east:
            print(f"East branch: {east}")
            self.recursDump(east)
            print("********** END EAST************")

        if west:
            print(f"West branch: {west}")
            self.recursDump(west)
            print("********** END WEST************")

        if west == None and east == None:
            print("EMPTY")
            print("tree size =", self._size)


    def recursDump(self, branch):

        if branch == None:
            print(" ")
        else:
            left_child = branch.left
            right_child = branch.right
            if left_child:
                print(left_child)
            if right_child:
                print(right_child)
            self.recursDump(right_child)
            self.recursDump(left_child)
            return branch

    def count(self):
        trunk = self.root_node
        keyslist = []
        result = self.recurs_helper(trunk, keyslist)
        #print(result)
        count = len(result)
        return count

    def make_key_list(self):
        # same as count different return
        trunk = self.root_node
        keyslist = []
        result = self.recurs_helper(trunk, keyslist)
        #print(result)
        return result

    def recurs_helper(self, branch, alist):
        if branch == None:
            pass
        else:
            left_sprout = branch.left
            right_sprout = branch.right
            if left_sprout:
                self.list_add(left_sprout, alist)
            if right_sprout:
                self.list_add(right_sprout, alist)
            self.recurs_helper(left_sprout, alist)
            self.recurs_helper(right_sprout, alist)
            return alist


    def list_add(self, something, alist):
        # Why did I do this?
        # Why is it working?
        if something:
            alist.append(something.key)

### PYTEST FAIL:
### FIXED, SIMPLE typo was error

#redwood = BinaryTree(11.5)
#redlist = []
#for i in range(0, 40):
    #x = randint(0, 40)
    #if x not in redlist:
        #redlist.append(x)
    #redwood.set(x, 'not 40')
#assert redwood.count != 40
#length_redlist = len(redlist)
#for i in range(0, length_redlist):
    #redwood.delete(redlist[i])
    #print('deleting : ', redlist[i])

#redwood.dump() ## size incorrect, is empty
#assert redwood._size == 0
#countfunction = redwood.count()
#print('redwood count=', countfunction)


### LEFT MANUAL TESTS ####
### manual delete function tests, left side of median::
#oaktree = BinaryTree(10.5)
#oaktree.set(2, 'two')
#oaktree.set(9, 'nine')
#oaktree.set(1, 'one')
#oaktree.set(3, 'three')
#oaktree.set(8, 'eight')
#oaktree.set(4, 'four')
#oaktree.set(7, 'seven')
#oaktree.set(5, 'five')
#oaktree.set(6, 'six')
#oaktree.delete(9)
#print("tested tree's size before delete = ", oaktree._size)
#for i in range(0, 160):
    #oaktree.delete(i)
    #print(i)
#oaktree.dump()

#### RIGHT MANUAL TESTS ####
# change median to test both sides
#fartwaffle = BinaryTree(18.5)
#fartwaffle.set(17, 'seventeen')
#fartwaffle.set(11, 'eleven')
#fartwaffle.set(20, 'twenty')
#fartwaffle.set(12, 'twelve')
#fartwaffle.set(19, 'nineteen')
#fartwaffle.set(13, 'thirteen')
#fartwaffle.set(14, 'fourteen')
#fartwaffle.set(18, 'eighteen')
#fartwaffle.set(16, 'sixteen')
#fartwaffle.set(15, 'fifteen')
#fartwaffle.set(23, 'twenty-three')
#fartwaffle.set(22, 'twenty-two')
#fartwaffle.set(24, 'twenty-four')
#print("size of tested tree before =", fartwaffle._size)
#fartwaffle.dump()
#for i in range(0, 28):
    #fartwaffle.delete(i)
    #print(i)
#fartwaffle.dump()

##########  manual delete from pytest #####

#def test_delete():

    #redwood = BinaryTree(11.5)
    #redlist = []
    #for i in range(0, 40):
        #x = randint(0, 40)
        #if x not in redlist:
            #redlist.append(x)
        #redwood.set(x, 'not 40')
    #red_length = len(redlist)
    #print(redlist)
    #for i in range(0, red_length):
        #item = redlist[i]
        #apple = redwood.get(item)
        #if apple != 'not 40':
            #print("^^^^^^^^^^^^missing: ^^^^^^^^^^^ \n", item)
    #assert redwood.count != 40
    #length_redlist = len(redlist)
    #assert redwood._size == length_redlist
    #for i in range(0, length_redlist):
        #redwood.delete(redlist[i])
    #print(redwood._size)
    #redwood.dump()
    #assert redwood._size == 0


#test_delete()
