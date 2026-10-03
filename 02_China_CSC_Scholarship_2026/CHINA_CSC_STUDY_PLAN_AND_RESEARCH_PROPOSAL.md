# Academic Study Plan and Research Proposal for Master's Degree
**Applicant:** Fuad Ahmed  
**Nationality:** Ethiopian  
**Undergraduate Degree:** Bachelor of Science in Computer Science (St. Mary's University, Addis Ababa)  
**Cumulative Major GPA:** 3.20 / 4.00  
**Target Degree Level:** Master of Science (MSc) in Computer Science and Technology / Software Engineering  
**Funding Scheme:** Chinese Government Scholarship (CSC Type B - High-Level Postgraduate Program) / University Presidential Fellowship  
**Target Institutions:** Harbin Institute of Technology (HIT), Beijing Institute of Technology (BIT), University of Science and Technology of China (USTC)  

---

## Proposed Research Title
### **Distributed Cloud-Edge Architectures and High-Concurrency Transaction Systems for Scalable Mobile Infrastructure in Emerging Markets**

---

## 1. Abstract
The rapid ubiquity of mobile services and cashless transaction ecosystems across developing economies requires digital architectures capable of operating reliably under severe constraints: fluctuating network bandwidth, device heterogeneity, and sudden transaction spikes. This research proposal outlines a focused study plan to investigate hybrid cloud-edge computing models, atomic concurrency control mechanisms, and distributed ledger consistency. By combining rigorous academic research at leading Chinese computational laboratories with my applied engineering background in full-stack backend design and mobile software development, this study aims to develop fault-tolerant, low-latency computational frameworks suited for high-density, resource-constrained mobile environments.

---

## 2. Academic Background & Applied Engineering Foundation
I completed my Bachelor of Science in Computer Science at St. Mary’s University in Addis Ababa, earning a 3.20 Major GPA. My undergraduate coursework provided comprehensive mathematical and architectural foundations, with top academic marks in:
* **Advanced Object-Oriented Programming (A+)**
* **Database Systems & Relational Architecture (A)**
* **Web & Internet Application Programming (A/A)**
* **Data Structures and Algorithms (B+)**
* **Senior Capstone Software Engineering Project (A/A+)**

To complement my core computing curriculum with domain-specific rigor in financial transactions and asset exchange mechanisms, I completed a 50-hour professional training program in *Fundamentals of Capital Markets and Securities Analysis* at the Addis Ababa University School of Commerce. This interdisciplinary foundation reinforced the necessity of strict ACID transaction semantics, mathematical determinism, and data integrity in large-scale software systems.

Over the past three years, I have translated academic principles into production-grade software implementations:
1. **High-Concurrency Ledger Architecture (*LuckyDraw*):** Engineered a high-throughput transaction and mini-app gaming engine. To eliminate race conditions and financial double-spending risks under concurrent access, I implemented pessimistic row-locking (`DB::transaction` with `lockForUpdate`), idempotent API endpoints, and integer-cent currency handling to avoid IEEE-754 floating-point rounding errors. Automated test suites validated system stability under simulated deadlock and burst traffic scenarios.
2. **Geospatial Mobile Systems & Offline Synchronization (*Addis Condo Finder*):** Architected a cross-platform mobile client (Flutter) and RESTful API backend (Laravel/MySQL) providing crowdsourced geospatial mapping for residential developments. The system incorporates viewport bounding-box queries, offline-first local caching (SQLite), and a multi-agent consensus protocol to verify geospatial coordinate accuracy before committing records to the public registry.
3. **Android Lifecycle & Persistent System Services:** Engineered persistent background workers, inter-process communication (IPC) routines, and low-level system services designed to maintain synchronization integrity across volatile cellular networks.

These engineering experiences highlighted a crucial technical challenge: conventional client-server architectures struggle with latency, packet drops, and server strain when deployed at scale in emerging digital infrastructures.

---

## 3. Problem Statement & Research Motivation
In rapidly growing economies across Africa and Asia, mobile smartphones serve as the primary gateway for banking, commerce, logistics, and governance. However, existing cloud-centric backends face significant bottlenecks:
1. **Network Volatility & High Latency:** Long round-trip times (RTT) between edge mobile clients and centralized data centers degrade user experience and cause transaction timeouts.
2. **Consistency vs. Availability Trade-offs:** In distributed transactional environments, traditional distributed consensus algorithms (e.g., Raft, Paxos) incur substantial latency overhead when network partitions occur.
3. **Resource Heterogeneity:** Edge devices exhibit vastly different computational, memory, and battery capabilities, requiring intelligent workload offloading rather than uniform computing models.

China stands as the undisputed global pioneer in mobile payment infrastructure, hyper-scale distributed computing, and smart city architectures. Chinese universities and research laboratories—such as the Key Laboratory of Big Data Computing at Harbin Institute of Technology, the State Key Laboratory of Intelligent Technology and Systems, and advanced cloud research groups at BIT and USTC—have established world-class paradigms in large-scale distributed systems, edge intelligence, and transactional processing. Undertaking my master's research under the mentorship of leading Chinese researchers will provide the exact theoretical and infrastructural environment required to solve these challenges.

---

## 4. Research Objectives & Proposed Methodology

### Specific Research Objectives:
1. **Develop an Adaptive Cloud-Edge Workload Partitioning Algorithm:** Design a lightweight optimization model that dynamically decides whether transactional tasks, geospatial computations, or validation routines execute locally on edge devices or offload to cloud nodes, based on real-time channel state and computational load.
2. **Formulate a Resilient Distributed Concurrency Protocol:** Construct a fault-tolerant concurrency control mechanism tailored for high-frequency micro-transactions in intermittent network environments, minimizing distributed deadlock while ensuring strict serializability or causal consistency.
3. **Prototype and Benchmark on Realistic Field Workloads:** Build an experimental testbed utilizing distributed Docker containers and mobile device emulators to benchmark latency, throughput, energy efficiency, and recovery time against conventional cloud setups.

### Research Methodology:
* **Phase 1 (Literature Synthesis & Formal Modeling - Months 1–6):** Comprehensive review of recent advancements in edge-native computing, conflict-free replicated data types (CRDTs), and Byzantine fault tolerance. Mathematical modeling of latency-constrained offloading.
* **Phase 2 (Architecture Design & Algorithm Development - Months 7–12):** Designing the system architecture, event-driven messaging queues, and atomic state-synchronization protocols.
* **Phase 3 (Implementation & Empirical Evaluation - Months 13–18):** Developing a reference framework using modern distributed technologies (Go/Rust, gRPC, Redis, Kafka, and Flutter/Android edge testbeds). Conducting stress-testing under simulated network drops and high concurrency.
* **Phase 4 (Thesis Writing & Peer-Reviewed Publication - Months 19–24):** Synthesizing experimental findings, preparing peer-reviewed conference/journal papers (IEEE/ACM), and writing the Master's dissertation.

---

## 5. Coursework & Study Plan (2-Year Master's Program)

### Year 1: Rigorous Coursework & Research Formulation
* **Semester 1 (Autumn):**
  * Advanced Computer Architecture & Distributed Systems
  * Advanced Algorithms & Computational Complexity
  * Advanced Database Systems & Transaction Processing
  * Chinese Language and Cultural Studies (Basic HSK 1–2)
  * Establishing faculty advisor meetings and defining the definitive thesis topic.
* **Semester 2 (Spring):**
  * Cloud Computing & Edge Intelligence Systems
  * Network Security & Distributed Cryptographic Protocols
  * Software Engineering Methodology & Formal Verification
  * Comprehensive Literature Survey & Thesis Proposal Defense.

### Year 2: Experimental Research & Master's Thesis
* **Semester 3 (Autumn):**
  * Full-time laboratory research, prototype implementation, and benchmarking.
  * Drafting research papers for international academic publication.
  * Mid-term thesis progress defense.
* **Semester 4 (Spring):**
  * Finalizing experimental validation and performance analysis.
  * Writing, reviewing, and defending the Master's Thesis.
  * Graduation and academic dissemination.

---

## 6. Alignment with Host University & Faculty Mentorship
My research trajectory directly aligns with ongoing technical initiatives at China’s top institutions:
* **Harbin Institute of Technology (HIT):** Renowned for its excellence in computer networks, distributed software engineering, and database systems. Mentorship within the Faculty of Computing would provide direct access to large-scale benchmarking clusters.
* **Beijing Institute of Technology (BIT):** Strong research groups in software engineering, intelligent information systems, and mobile computing.
* **University of Science and Technology of China (USTC):** A C9 League institution celebrated for theoretical rigor, high-performance computing, and systems engineering.

I am dedicated to integrating actively into the host professor’s research team, contributing both theoretical rigor and hands-on systems development capabilities to joint laboratory projects.

---

## 7. Career Vision & Long-Term Impact
Upon completing my Master's Degree in Computer Science in China, my long-term objective is twofold:
1. **Industrial Leadership:** Serve as a Lead Systems Architect designing fault-tolerant digital public infrastructure, fintech clearing systems, and scalable enterprise networks in East Africa.
2. **Academic & Bilateral Technology Transfer:** Establish technical collaborations and academic bridges between Ethiopian universities and Chinese engineering faculties, contributing to the shared growth envisioned under the Belt and Road Initiative and South-South technological cooperation.

I am fully prepared to devote my complete energy, discipline, and intellectual commitment to achieving academic excellence under the Chinese Government Scholarship.
