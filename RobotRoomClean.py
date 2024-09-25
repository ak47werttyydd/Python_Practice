interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}

queue=[]
start_point=[0,0]
clean_record={} #if point:1 for clean None for not
BFS(start_point)
def BFS(cur_point):
	if not clean.get(cur_point,None):
		clean()
	if move(): #next cell open
		clean()