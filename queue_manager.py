from multiprocessing.managers import BaseManager
import multiprocessing as mp

task_queue = mp.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register("get_task_queue", callable=lambda: task_queue)