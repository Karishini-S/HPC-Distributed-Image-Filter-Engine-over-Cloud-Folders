import os
from filters.filter import grayscale_filter, blur_filter, edge_filter, save_image
import cv2
import multiprocessing as mp
from queue_manager import QueueManager
import threading
from workers.worker import worker_run 

'''def process_image(input_path, output_folder, filters):
    img = cv2.imread(input_path)
    if img is None:
        print(f"Error: Could not load image {input_path}")
        return

    base_name = os.path.splitext(os.path.basename(input_path))[0]
    for f in filters:
        processed = f(img)
        save_image(processed, output_folder, f"{base_name}_{f.__name__}.jpg")'''

def create_tasks(input_folder, output_folder, filters, task_queue):
    for file in os.listdir(input_folder):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(input_folder, file)
            print(f"Master: Queuing task: {img_path}")
            task_queue.put((img_path, output_folder, filters))
    print("Master: All tasks queued.")

if __name__ == "__main__":
    input_folder = "inputs"
    output_folder = "outputs"

    filters = [grayscale_filter, blur_filter, edge_filter]

    '''for file in os.listdir(input_folder):
        if file.lower().endswith((".jpg", ".png", ".jpeg")):
            img_path = os.path.join(input_folder, file)
            print(f"Processing {img_path} ...")
            process_image(img_path, output_folder, filters)

    print("Sequential processing finished!")'''

    manager = QueueManager(address=("127.0.0.1", 5000), authkey=b"abc")
    server = manager.get_server()
    print("Master: Starting manager server...")

    threading.Thread(target=server.serve_forever, daemon=True).start()

    manager_client = QueueManager(address=("127.0.0.1", 5000), authkey=b"abc")
    manager_client.connect()
    task_queue = manager_client.get_task_queue()

    # Start workers as separate processes (instead of manual run)
    num_workers = 3
    workers = []
    for wid in range(num_workers):
        p = mp.Process(target=worker_run, args=(wid, output_folder))
        p.start()
        workers.append(p)

    # Queue tasks
    create_tasks(input_folder, output_folder, filters, task_queue)

    # Send STOP signals
    for _ in range(num_workers):
        task_queue.put("STOP")

    # Wait for workers to finish
    for p in workers:
        p.join()

    print("Master: All tasks completed.")
