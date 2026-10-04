# POLITECNICO DI MILANO • DETAILED COURSE SYLLABUS
## Academic Prerequisites & Undergraduate Course Descriptions for MSc in Computer Science and Engineering

> **Applicant:** FUAD AHMED (TUBA, FUAD AHMED) | Passport: `E00340202` | Email: `fuadahmedt@gmail.com`  
> **Conferring Institution:** St. Mary’s University (Faculty of Informatics), Addis Ababa, Ethiopia  
> **Degree Conferred:** Bachelor of Science in Computer Science (4-Year, Full-Time, 100% English MOI)  
> **Target Program:** Laurea Magistrale in Computer Science and Engineering (*Ingegneria Informatica*)  

---

## 1. Core Computer Systems, Architecture & Operating Systems

### **Operating Systems Architecture (CoSc 3011)** — *4 Credits (7 ECTS Equiv)*
* **Category:** Operating Systems & Low-Level Computing (3 hrs lecture, 3 hrs lab/wk)
* **Topics Covered:** Multi-programming kernel architectures, process scheduling (round-robin, multi-level feedback queues), thread lifecycles, POSIX threads, IPC (pipes, message queues, shared memory).
* **Synchronization & Concurrency:** Race conditions, critical sections, semaphores, mutexes, monitors, deadlocks, Banker's algorithm, deadlock detection and recovery.
* **Memory & Storage:** Virtual memory, paging, segmentation, page fault handling, page replacement (LRU, clock algorithm), VFS, inodes, disk scheduling algorithms.
* **Lab:** C/Linux programming for kernel system calls, fork-exec routines, POSIX synchronization, and custom memory management routines.

### **Computer Organization and Architecture (CoSc 2032)** — *4 Credits (6 ECTS Equiv)*
* **Category:** Hardware-Software Interface & Architecture (3 hrs lecture, 2 hrs lab/wk)
* **Topics:** Von Neumann model, CPU datapath and control unit design, ALU operations, instruction pipelining, hazards (data, control, structural), branch prediction.
* **Memory Hierarchy:** Cache mapping (direct, set-associative, fully associative), cache coherence, write-through/write-back policies, virtual memory translation, bus protocols, DMA controllers.
* **Assembly:** MIPS/x86 assembly language programming, register allocation, stack frame manipulation, hardware interrupt servicing.

### **Distributed Systems (CoSc 4011)** — *3 Credits (6 ECTS Equiv)*
* **Category:** Distributed Systems & Scalable Architectures (3 hrs lecture, 2 hrs lab/wk)
* **Foundations:** Characterization of distributed systems, client-server vs peer-to-peer topologies, remote procedure calls (RPC), message passing interfaces, network socket programming.
* **Time & State:** Physical and logical clocks (Lamport timestamps, vector clocks), causal ordering, global state snapshot algorithms.
* **Coordination & Fault Tolerance:** Distributed mutual exclusion, leader election (Bully, Ring), consensus protocols, replication models (primary-backup, active replication), Paxos/Raft overview, Byzantine fault models.

---

## 2. Algorithms, Data Structures & Software Engineering

### **Data Structures and Algorithms (CoSc 2011)** — *4 Credits (7 ECTS Equiv)*
* **Category:** Foundational Computer Science (3 hrs lecture, 3 hrs lab/wk)
* **Structures:** Linked lists, stacks, queues, binary search trees, AVL trees, Red-Black trees, B-Trees, min/max binary heaps, hash tables, collision resolution.
* **Analysis:** Asymptotic notation ($O, \Omega, \Theta$), divide-and-conquer, greedy algorithms, dynamic programming, sorting algorithms (QuickSort, MergeSort, HeapSort).
* **Graph Algorithms:** Graph representations, BFS, DFS, Dijkstra’s shortest path, Bellman-Ford, Kruskal’s and Prim’s minimum spanning trees.

### **Object-Oriented Programming (CoSc 2021)** — *4 Credits (6 ECTS Equiv)*
* **Category:** Software Development (3 hrs lecture, 3 hrs lab/wk)
* **Core Paradigms:** Encapsulation, inheritance, polymorphism, abstract classes, interfaces, generic programming, exception handling, multithreading in Java and C++.
* **Design Patterns:** Creational (Singleton, Factory), Structural (Adapter, Decorator), and Behavioral (Observer, Strategy) design patterns.

### **Database Management Systems (CoSc 2042)** — *4 Credits (6 ECTS Equiv)*
* **Category:** Data Management (3 hrs lecture, 3 hrs lab/wk)
* **Theory:** Relational algebra, tuple relational calculus, ER modeling, functional dependencies, normal forms (1NF, 2NF, 3NF, BCNF).
* **Transactions:** ACID properties, serializability, two-phase locking (2PL), deadlock detection, write-ahead logging (WAL), crash recovery.
* **Implementation:** Advanced SQL, indexing structures (B+ Trees, Hash indexes), query execution plans, PostgreSQL and MySQL implementations.

### **Computer Networks and Data Communications (CoSc 3032)** — *4 Credits (6 ECTS Equiv)*
* **Category:** Networking & Telecommunications (3 hrs lecture, 2 hrs lab/wk)
* **Layer Architectures:** OSI and TCP/IP models, framing, error detection (CRC), flow control, ARQ protocols (Go-Back-N, Selective Repeat).
* **Network & Transport:** IPv4/IPv6 addressing, subnetting, CIDR, routing algorithms (Dijkstra, distance vector, BGP, OSPF), TCP congestion control (AIMD, slow start), flow control, UDP sockets.
* **Application Layer:** DNS, HTTP/HTTPS, TLS handshake, SMTP, SSH, network security fundamentals.

---

## 3. Mathematics & Quantitative Foundations

* **Calculus for Computer Science (Math 1011):** Limits, continuity, derivative techniques, Mean Value Theorem, Taylor series, Riemann integration, multivariate partial derivatives, gradients, and optimization. (4 Credits / 6 ECTS)
* **Discrete Mathematics (Math 1022):** Mathematical logic, propositional and predicate calculus, proof methods (induction, contradiction), set theory, relations, combinatorics, recurrence relations, Boolean algebra. (3 Credits / 5 ECTS)
* **Linear Algebra (Math 2011):** Vector spaces, subspaces, linear independence, basis and dimension, matrices, determinants, Gaussian elimination, eigenvalues, eigenvectors, diagonalization, Gram-Schmidt orthogonalization. (3 Credits / 5 ECTS)
* **Probability and Statistics for Computing (Stat 2022):** Probability axioms, Bayes’ theorem, discrete and continuous random variables, expectation, variance, Law of Large Numbers, Central Limit Theorem, hypothesis testing, regression. (3 Credits / 5 ECTS)

---

## 4. Senior Undergraduate Capstone Project

### **Senior Capstone Research Project (CoSc 4032)** — *4 Credits (8 ECTS Equiv)*
* **Grade:** A (Excellent) | Full Final Academic Year
* **Title:** *Design and Implementation of a High-Concurrency Fault-Tolerant Distributed Data Synchronization Protocol*
* **Abstract & Methodology:** Architected a lightweight state-synchronization protocol across distributed nodes using Python AsyncIO and Go. Engineered delta-encoded state serialization to minimize bandwidth consumption across high-latency networks. Implemented heartbeats, leader election routines, and thread-safe lock-free memory rings for high-throughput concurrent I/O.
