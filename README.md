# Distributed Image Filter Engine Over Cloud Folders

## Problem Statement
The goal of this project is to design and implement a **distributed image filtering engine** that automatically processes images uploaded to a cloud folder.  
When a new image is uploaded, the system applies a set of predefined filters (e.g., grayscale, blur, and edge detection) and stores the processed results in the appropriate output folder.  

Traditional sequential processing becomes inefficient when handling large volumes of images. This project leverages **High-Performance Computing (HPC) techniques** such as **task parallelism, distributed memory computing (MPI), and multiprocessing** to speed up the workflow.  
Additionally, the system integrates with **cloud storage** to enable automation and scalability.  

The final deliverable will be a **comparative analysis** of sequential vs distributed processing performance, demonstrating improvements in throughput, scalability, and fault tolerance.  

---

## Project Plan

### **Phase 1: Core Image Processing Module, Parallelization & Worker Logic (Week 1-3)**
The first step is to build a working sequential pipeline with OpenCV. This ensures basic functionality is correct before scaling to distributed execution.

1. **Understand Image Filters**  
   - Grayscale conversion  
   - Gaussian blur  
   - Edge detection (Canny filter)  

2. **Setup Development Environment**  
   - Install Python and dependencies (`opencv-python`, `numpy`, `multiprocessing`, `mpi4py`).  

3. **Implement Sequential Version (Python + OpenCV)**  
   - Write functions for each filter.  
   - Implement a pipeline:  
     ```
     Input Image → Apply Filter → Save Output
     ```  
   - Test correctness on small sets of images.  

Now that the pipeline works, we introduce **parallel workers** to handle multiple images simultaneously.

4. **Design Master–Worker Model**  
   - Master process pushes tasks (image + filter) into a **queue**.  
   - Worker processes fetch tasks, apply filters, and save results.  

5. **Implement Parallel Processing**  
   - Use **Python Multiprocessing** for shared-memory parallelism.  
   - Optionally use **MPI4Py** to simulate distributed memory parallelism.  

6. **Benchmark Performance**  
   - Measure sequential vs parallel execution times.  
   - Scale with number of workers (1, 2, 4, 8).  

---

### **Phase 2: HPC Enhancements & Cloud Storage Integration (Weeks 4–7)**
To make the system robust and closer to real HPC applications, enhancements are introduced.

1. **Load Balancing**  
   - Ensure tasks are evenly distributed across workers using queues.  

2. **Fault Tolerance**  
   - Implement retry mechanisms for failed tasks.  
   - Worker health monitoring (if a worker fails, tasks get reassigned).  

3. **Hybrid Parallelism**  
   - Combine **multiprocessing** (across workers) with **threading** (inside each worker).  

4. **Memory Optimization**  
   - For very large images, process them in **chunks** instead of loading entirely.  

To make the system practical, we integrate with cloud storage.

5. **Cloud Folder Monitoring**  
   - Detect when a new image is uploaded (polling/trigger simulation).  

6. **Automation**  
   - Automatically send images through the processing pipeline.  
   - Place processed results in output folder(s).  

7. **Job Tracking & Monitoring**  
   - Log jobs for success/failure.  
   - Track processing times for analysis.  

---

### **Phase 3: Performance Evaluation (Weeks 8–9)**
Finally, evaluate performance, scalability, and reliability.

1. **Performance Tests**  
   - Sequential vs parallel execution time.  
   - Scalability test with 1, 2, 4, 8 workers.  
   - Latency per image.  

2. **Fault Tolerance Validation**  
   - Simulate worker failures.  
   - Check system recovery and task reassignment.  

---

## Project Architecture

     ┌─────────────┐        ┌─────────────┐
     │ Cloud Input │───────>│   Listener  │
     └─────────────┘        └──────┬──────┘
                                   │
                                   ▼
                          ┌─────────────────┐
                          │ Task Queue (MQ) │
                          └────────┬────────┘
                                   │
        ┌─────────────┬─┬──────────┴──┬───────┬─────────────┐
        │ Worker 1    │ │ Worker 2    │  ...  │  Worker N   │
        │ (MPI/Proc)  │ │ (MPI/Proc)  │       │  (MPI/Proc) │
        └─────┬───────┘ └─────┬───────┘       └─────┬───────┘
              │               │                     │
              ▼               ▼                     ▼
        ┌─────────────┐ ┌─────────────┐       ┌─────────────┐
        │  Output 1   │ │  Output 2   │  ...  │  Output N   │
        └─────────────┘ └─────────────┘       └─────────────┘



---

## Timeline (8–9 Weeks)

| Phase | Task | Duration |
|-------|------|----------|
| Phase 1 | Core Image Processing & Parallelization with Workers | Weeks 1–3 |
| Phase 2 | HPC Enhancements & Cloud Storage Integration | Weeks 4–7 |
| Phase 3 | Performance Evaluation | Weeks 8–9 |

---

## Technologies Used
- **Languages**: Python  
- **Libraries**: OpenCV, NumPy, Multiprocessing, MPI4Py  
- **Cloud Services**: Google Drive / AWS S3 (storage integration)  
- **Tools**: GitHub, Docker (optional for workers), Linux HPC cluster  

---

## Contributors
- **Karishini S&nbsp;&nbsp;- [CB.AI.U4AID23013]**
- **Gowri J S&nbsp;&nbsp;&nbsp;&nbsp;- [CB.AI.U4AID23055]** 
- **Akshaya V&nbsp;&nbsp;- [CB.AI.U4AID23064]**

---
