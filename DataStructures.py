class Queue:

    def __init__(self, mode, current_queue=[]):
        self._queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self._mode = mode
    
    def enqueue(self, item):
        self._queue.append(item)
        items_in_front = self.size() - 1 if self._mode == 'FIFO' else 0
        qty = 'is 1 item' if items_in_front == 1 else f'are {items_in_front} items'
        return f'{item} added to queue. There {qty} before it.'

    def dequeue(self):
        item = self._queue.pop(0) if self._mode == 'FIFO' else self._queue.pop()
        
        return f'{item} has been removed from queue'

    def get_queue(self):
        return self._queue

    def size(self):
        return len(self._queue) 