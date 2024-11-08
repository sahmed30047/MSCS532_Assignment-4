#Task class to represent individual tasks
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        
        #Initializing a new task with task ID, priority, arrival time and deadline.
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline
    
    def __repr__(self):
         
        #String representation of the task for debugging purposes.
          
        return f"Task(ID: {self.task_id}, Priority: {self.priority}, Arrival: {self.arrival_time}, Deadline: {self.deadline})"

#PriorityQueue class for implementing a max-heap priority queue
class PriorityQueue:
    def __init__(self):
         
        #Initialize the priority queue using a list to represent the heap.
         
        self.heap = []

    def is_empty(self):
          
        #Check if the priority queue is empty.
        #Returns True if the queue is empty or else it returns False.
         
        return len(self.heap) == 0

    def insert(self, task):
        
       #Inserting a new task into the priority queue & maintain the heap property.
        
        
        # Append the new task at the end of the heap
        self.heap.append(task)
        # Restore the heap property by bubbling the task up
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
         
        #Helper function to maintain the heap property after insertion.
        #Moves the task upwards if its priority is higher than its parent's.
         
        parent_index = (index - 1) // 2
        #Continue swapping with the parent as long as the current task's priority is higher.
        while index > 0 and self.heap[index].priority > self.heap[parent_index].priority:
            #Swap current task with parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            #Move upwards in the heap
            index = parent_index
            parent_index = (index - 1) // 2

    def extract_max(self):
        
        #Extract the task with the highest priority (the root of the heap).
        #Returns the task with the highest priority.        

        
        if self.is_empty():
             raise IndexError("Priority queue is empty")

    # If there's only one element, just pop and return it
        if len(self.heap) == 1:
           return self.heap.pop()
  
       # For more than one element replacing root with last element and heapify
        max_task = self.heap[0]
        last_task = self.heap.pop()  #Remove the last element

        if not self.is_empty():
        # Move the last element to the root if the heap is not empty otherwise it wont.
         self.heap[0] = last_task
        self._bubble_down(0) 
    
        return max_task

    def _bubble_down(self, index):
        
        #Helper function to maintain the heap property.
        #Moves the task downwards if its priority is less than its children.
        
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            #Find the largest among current, left child and right child.
            if left < n and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < n and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest != index:
                # Swap with the largest child
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                #Continuing to bubble down
                index = largest
            else:
                break

    def increase_priority(self, task_id, new_priority):
        
        # Increase the priority of an existing task in the heap and adjust its position accordingly.
      
        index = self._find_task_index(task_id)
        if index is None:
            raise ValueError("Task not found")

        old_priority = self.heap[index].priority
        self.heap[index].priority = new_priority

        if new_priority > old_priority:
            #Bubble up if the new priority is higher
            self._bubble_up(index)
        else:
            #Bubble down if the new priority is lower
            self._bubble_down(index)

    def _find_task_index(self, task_id):
        """
        Helper function to find the index of a task in the heap by its task ID.
        Returns the index if found, None otherwise.
        """
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                return i
        return None



def scheduler_simulation():
    
    #Task scheduling using a priority queue (max-heap).
    #Tasks are processed based on their priority.
    
    # Create a priority queue
    pq = PriorityQueue()

    #Inserting some tasks into the priority queue
    pq.insert(Task(1, 10, 0, 5))  # Task with priority 10
    pq.insert(Task(2, 5, 1, 7))   # Task with priority 5
    pq.insert(Task(3, 20, 2, 10))  # Task with priority 20
    pq.insert(Task(4, 15, 3, 6))  # Task with priority 15

    print("Priority Queue Simulation:")
    print(f"Initial tasks in the queue: {pq.heap}")

    #Extract tasks based on priority
    while not pq.is_empty():
        max_task = pq.extract_max()
        print(f"Processing task with highest priority: {max_task}")

#Run the scheduler simulation
scheduler_simulation()
