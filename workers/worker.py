import os
import cv2
from queue_manager import QueueManager
from filters.filter import save_image

def process_image(input_path, output_folder, filters, worker_id):
    img = cv2.imread(input_path)
    if img is None:
        print(f"Worker: Error loading {input_path}")
        return
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    for f in filters:
        processed = f(img)
        out_name = f"{base_name}_{f.__name__}_w{worker_id}.jpg"
        save_image(processed, output_folder, out_name)
        print(f"Worker: Saved {out_name} in {output_folder}")

def worker_run(worker_id, output_folder):
    # Connect to manager
    manager = QueueManager(address=("127.0.0.1", 5000), authkey=b"abc")
    manager.connect()
    task_queue = manager.get_task_queue()

    print(f"Worker {worker_id}: Connected. Waiting for tasks...")
    while True:
        task = task_queue.get()
        if task == "STOP":
            print(f"Worker {worker_id}: Stopping...")
            break
        img_path, output_folder, filters = task
        print(f"Worker {worker_id}: Processing {img_path}")
        process_image(img_path, output_folder, filters, worker_id)
