#!/usr/bin/python

Mark Roberts - data engineer/SWE

45 min

coding/SQL

- - - - - - - - - - - - - - - - - - -

Mark Roberts (Data Engineer) - Ninja - Coding

Question 1: Date Compare

This is a good warm up question that appears super simple at first glance, but trips people up with unexpected complexity.
In general a successful candidate shouldn't spend more than 10-15 minutes on this question,
even if they implement both naive and advanced solutions. The signals the question provides:


Does the candidate have a basic knowledge of coding (good for warm up on a phone screen)
Can the candidate think through problems logically
Is the candidate happy with ugly code that works


Suppose you have two dates and you want to know which comes first. Well, obviously you first compare the year.
If the years the same, then compare the month. If they are the same, then compare the date.
If the date is the same and there is time involved, you then compare the hours.
If those are the same then compare the minutes.
If those are the same, then compare the seconds. If those are the same, then compare the milliseconds. And so on.


You could also convert the two dates into seconds or milliseconds from some reference date. An easy one is 1/1/00 00:00.
Then compare the number for each. Or, you could convert the date into years and some change and compare those.

You could also convert the dates into strings of the format "YYYYMMDDHHSS" and then compare them lexicographically.

Python solution:

Typical setup

class DateObj(object):
	def __init__(self, year, month, day, hour, minute, second, msec):
		self.year = int(year)
		self.month = int(month)
		self.day = int(day)
		self.hour = int(hour)
		self.minute = int(minute)
		self.second = int(second)
		self.msec = int(msec)
		self.ensure_valid()

People often start with a solution that looks like this because it's the obvious one.
It's also horribly ugly and makes for very unmaintainable code.

def max_date__nested(d1, d2):
	if d1.year > d2.year:
		return d1
	elif d2.year > d1.year:
		return d2
	else:
		if d1.month > d2.month:
			return d1
		elif d2.month > d1.month:
			return d2
			...
			return d1

This is a solid solution that shows an elegant solution to the problem.

def max_date__loops(d1, d2):
	d1_arr = [d1.year, d1.month, d1.day, ...]
	d2_arr = [d2.year, d2.month, d2.day, ...]
	return d1 if d1 > d2 else d2

A lexical sorting solution. This has the advantage of being "always right" and not worrying about calendar oddities.
 Make sure that the candidate doesn't forget format specifiers so that the strings can actually be compared.

def max_date__lexical(d1, d2):
	d1_str = "{year:04}-{month:02}-{day:02} {hour:02}:{minute:02}:{second:02}.{msec:06}.format(**d1.__dict__())
	d2_str = "{year:04}-{month:02}-{day:02} {hour:02}:{minute:02}:{second:02}.{msec:06}.format(**d2.__dict__())
	return d1 if d1_str > d2_str else d1







Question 2: TreePrintAllPath

For a given a binary tree, print paths from root to all leaf nodes, one path per line.
This is basically a depth-first-traversal with "seen-so-far" memory. For example:

For tree:

A
/ \
B   C
/   / \
D   E   F

The expected output is:

ABD
ACE
ACF

Sample solution to this problem in C++:

void printPathsDFS(Node* node, list<Node*>& path)
{
if (node->leftChild() == NULL && node->rightChild() == NULL) {
// This will do the actual printing from a list.
printNodeList(path);
return;
}

if (node->leftChild() != NULL) {
path.push_back(node->leftChild());
printPathsDFS(node->leftChild(), path);
path.pop_back();
}

if (node->rightChild() != NULL) {
path.push_back(node->rightChild());
printPathsDFS(node->rightChild(), path);
path.pop_back();
}
}

void printPaths(Node* root)
{
list<Node*> path;
if (root == NULL) {
return;
}
path.push_back(root);
printPathsDFS(root, path);
}



A more condensed version in Javascript

function printPaths(root, path) {

path = path || []; // no need for a helper function
path.push(root);
if (!root.left && !root.right) { // leaf check
// print out names of path
console.log(path.map(function(node) { return node.name }).join(''));
}
if (root.left) {
printPaths(root.left, path);
}
if (root.right) {
printPaths(root.right, path);
}
path.pop();
}
printPaths(A);


A few points to note:

1. the ending condition. A node is a leaf only if both of its children are NULL.
2. The list should be passed as a reference. Candidates sometimes decide to pass a cloned list into every recursive function call
 -- while this works, it incurs a large memory overhead for no good reason.
 See if you can encourage them to optimize memory if they pursue this route (they basically just need a pop call).

Iterative Solution

Candidates often decide to approach this problem with a DFS iterative approach.
This is tricky since you need to maintain the current path variable (aka call stack) inside the iterative loop.
Candidates either keep cloning the current path when pushing children on (aka maintaing an array of arrays)
or they use a peek method with a seen state hashmap.

Cloning iterative approach in Javascript:

function printPaths2(root) {
var queue = [[root]];

while (queue.length) {
var path = queue.shift();
var lastNode = path[path.length - 1];
if (!lastNode.left && !lastNode.right) {
// leaf node, so print out this path
console.log(path.map(function(node) { return node.name; }).join(''));
}
// cloning here
if (lastNode.left) {
queue.push(path.slice().concat([lastNode.left]));
}
if (lastNode.right) {
queue.push(path.slice().concat([lastNode.right]));
}
}
}
printPaths2(A);

And lastly, an iterative solution that uses seen state:

function printPaths3(root) {
var seen = {};
var queue = [root];

while (queue.length) {
var node = queue[queue.length - 1]; // peek
if (!node.left && !node.right) {
// print path
console.log(queue.map(function(node) { return node.name; }).join(''));
}

// here we check for seen state so we can explore the whole tree
if (node.left && !seen[node.left.name]) {
seen[node.left.name] = true;
queue.push(node.left);
} else if (node.right && !seen[node.right.name]) {
seen[node.right.name] = true;
queue.push(node.right);
} else {
queue.pop();
}
}
}

printPaths3(A);










Question Extensions
Follow up question:
What if it's a directed graph instead of a tree?

In that case, we will need to handle paths with cycle. Those nodes that form a cycle are not leaf nodes
and we need to skip them. One way to do that is to check if a node is in the path or not.

A generic version of this problem is to implement an improved version of "ls -R".
But instead of printing the file name (that's what "ls -R" do),
we want to print relative path from every file to the root node.
This will be a good test to see if the candidate can think through corner cases (like circular links).






Question 3: SQL

Q1: Walk me through current project experience. and the most impactful project and how it was impactful.
(Make sure the example you pick illustrates REAL impact)

Q2: Spawning the first question, asked how she would deal with bad data?


Q3: How is a many-to-many relationship modeled?


Q4: How is a ragged hierarchy handled in a data model?


Q5: Any questions for me?


Q6: What is the difference between a left join and outer join?



Q7: find the highest grosser per dept from Employee(EmpID, DeptID, salary) using ANSI SQL.
		select
		  max(employees.salary),
		  employees.department_id
		from
		  employees,
		  departments
		where
		  employees.department_id = departments.id
		group by
		  employees.department_id




Q8: find the highest grosser per dept from Employee(EmpID, DeptID, salary) using code


EmpID, DeptID, Salary

001 1 5000
002 2 3000
003 1 7000
004 2 6000
005 3 1500
006 1 7000
