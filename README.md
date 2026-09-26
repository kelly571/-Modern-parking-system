#DSA task one - modern parking system

# Automated Garage Tracking Logistics System

## System Overview
This project provides a modular automated solution for monitoring parking lot infrastructure, managing incoming vehicle traffic loops, computing billing durations on exit, and processing analytical mathematical data structures.

The codebase implements custom Abstract Data Types (ADTs) built from first principles without tracking shortcuts, fulfilling standard Data Structures & Algorithms execution criteria.

## Program Architecture
The system components are split across specialized modules:
* `custom_stack.py` - Custom array-backed and linked node LIFO implementations.
* `custom_queue.py` - Custom sequence and node-backed FIFO queue pipelines.
* `recursion_vs_stack.py` - Evaluation of frame allocations via loop arithmetic, recursion, and ADT stacks.
* `db_manager.py` - Persistent transactional SQLite engine wrapper storage nodes.
* `parking_operations.py` - Automated integration module linking structures to runtime garage logic.
* `run_system.py` - Unified terminal command console user interface entry point.

## Abstract Data Type Implementations
1. Bounded Array Stack: Employs standard list buffers to maintain LIFO execution tracks within set boundaries.
2. Link Chain Stack: Allocates dynamic node pointers to manage memory storage paths efficiently.
3. Linear Queue: Performs sequential index extractions to coordinate FIFO wait lines.
4. Linked Queue: Couples double-ended terminal references to drive smooth transit flow patterns.

## Local Execution Instructions
Launch the central console management terminal script from your command prompt:
```bash
python3 run_system.py
```
