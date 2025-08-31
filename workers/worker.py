import os
import cv2
from queue_manager import QueueManager
from filters.filter import save_image

def process_image(input_path, output_folder, filters):
    img = cv2.imread(input_path)
    if img is None:
        print(f"Worker: Error loading {input_path}")
        return
    
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    for f in filters:
        processed = f(img)
        save_image(processed, output_folder, f"{base_name}_{f.__name__}.jpg")

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
        
        img_path, filters = task
        print(f"Worker {worker_id}: Processing {img_path}")
        process_image(img_path, output_folder, filters)
        print(f"Worker {worker_id}: Completed {img_path}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python worker.py <worker_id> <output_folder>")
        sys.exit(1)
    
    worker_id = int(sys.argv[1])
    output_folder = sys.argv[2]
    
    # Ensure output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    print(f"Starting Worker {worker_id}...")
    worker_run(worker_id, output_folder)