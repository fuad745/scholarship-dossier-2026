# FUAD AHMED
**Full-Stack Software Engineer & Computer Systems Researcher**  
Addis Ababa, Ethiopia | `fuadahmedt@gmail.com` | `+251 925 278 350`  
**Portfolio:** [fuad-portfolio-rose.vercel.app](https://fuad-portfolio-rose.vercel.app) | **GitHub:** [github.com/fuad745](https://github.com/fuad745) | **LinkedIn:** [linkedin.com/in/fuad-ahmed745](https://linkedin.com/in/fuad-ahmed745)

---

## 🎯 ACADEMIC & RESEARCH PROFILE
Results-driven Computer Science graduate and Systems Engineer with a **3.20 Major GPA** and proven experience designing high-concurrency backend architectures, reactive cross-platform mobile systems, and geospatial engines. Combines rigorous computational foundations (distributed systems, database internals, and concurrency algorithms) with practical engineering leadership in multi-stakeholder and operational environments. Seeking admission to a **Master of Science (M1/M2) in Computer Science / Software Architecture & Distributed Systems** in France, with eligibility for the **France Excellence Eiffel Scholarship**.

---

## 🎓 EDUCATION & ACADEMIC ACHIEVEMENTS

### **Bachelor of Science in Computer Science**
**St. Mary’s University**, Addis Ababa, Ethiopia  
*Graduated: July 2022 | Medium of Instruction: 100% English*  
* **Major GPA:** **3.20 / 4.00** | **Cumulative GPA:** 3.04 / 4.00  
* **Core Computational Coursework:**  
  * Data Structures & Algorithms (Advanced Algorithmic Complexity, Graph Algorithms, Sorting & Searching)
  * Database Systems & Architecture (Relational Normalization, Indexing, B-Trees, Query Optimization, ACID Properties)
  * Operating Systems & Systems Programming (Process Scheduling, Thread Synchronization, Memory Hierarchy, IPC)
  * Computer Networks & Distributed Communication (TCP/IP Protocols, Sockets, Network Topology, Security)
  * Object-Oriented Analysis & Design (Design Patterns, SOLID Principles, UML Architectural Modeling)
  * Software Engineering & Quality Assurance (Testing Methodologies, SDLC, CI/CD Fundamentals)
* **BSc Capstone Project:** Multi-tiered web and database management system with role-based access control (RBAC), transactional consistency, and normalized MySQL schemas.

### **Executive Certification: Capital Markets & Securities Analysis**
**Addis Ababa University**, School of Commerce (in collaboration with Ethiopian Capital Market Authority)  
*Completed: September 2024 (50-hour intensive certification)*  
* **Focus Areas:** Financial market microstructure, equity valuation, clearing and settlement mechanisms, risk assessment models, and transactional integrity.

---

## 💻 SOFTWARE SYSTEMS & PRODUCTION PROJECTS

### **Addis Condo Finder — Geospatial Distributed Property & Mapping Platform**
*Architecture: Flutter (Dart), Laravel 11/13 REST API, PostgreSQL/MySQL, Filament Admin, OpenStreetMap*
* **Spatial Query Optimization:** Designed bounding-box spatial indexing algorithms (`bbox=minLat,minLng,maxLat,maxLng`) to serve viewport-constrained geospatial payloads, eliminating server memory overhead.
* **Token-Matching Search Engine:** Engineered an any-order multi-token search pipeline indexing condominium names, project IDs, and block numbers with sub-50ms query response times.
* **Consensus Verification & Security:** Implemented a multi-user crowdsourced verification engine with client write rate-limiting (20 requests/minute per user) and atomic database unique-constraint handling to prevent verification races.

### **LuckyDraw Engine — High-Concurrency Financial Gaming & Ledger Architecture**
*Architecture: Laravel 13, Livewire 4, MySQL (InnoDB), Telegram Mini App API, REST Webhooks*
* **Atomic Concurrency Guards:** Implemented strict pessimistic row-level locking (`lockForUpdate`) on draw execution and prize distribution, mathematically guaranteeing zero double-payouts and single-draw dispatch under concurrent client traffic.
* **Integer-Cent Exact Accounting:** Formatted all currency balances and ticket prices into integer cents (`tests/Unit/MoneyTest.php`) to eradicate floating-point rounding errors across multi-tiered jackpot distributions.
* **Fail-Closed Payment Verification:** Integrated automated payment-verification webhooks for mobile money providers (Telebirr/CBE) with unique reference deduplication to prevent replay attacks.
* **Automated Testing Suite:** Developed a suite of 25+ automated feature, unit, and concurrency tests validated directly on production-grade MySQL engines.

### **Money Manager — Offline-First Reactive Personal Finance System**
*Architecture: Flutter, Dart, Riverpod 2.0, SQLite (sqflite), Material 3 Design System*
* **In-Memory Cache & Synchronous Reads:** Structured an `AppRepository` abstraction maintaining an in-memory state cache for instant UI rendering while persisting incremental row mutations asynchronously to SQLite.
* **Security & Biometrics:** Engineered biometric fingerprint/PIN authentication with failed-attempt lockout security and OS-level `FLAG_SECURE` window protections preventing app switcher data leakage.
* **Automated Scheduling:** Built background local notification schedulers and auto-posting engines for recurring debts, upcoming bills, and savings goal contributions.

---

## 💼 PROFESSIONAL EXPERIENCE

### **Full-Stack Software Engineer (Independent & Contract)**
*Addis Ababa, Ethiopia* | **Nov 2023 – Present**
* Architected, tested, and deployed end-to-end web and mobile applications using Flutter, Laravel, and relational database systems.
* Designed resilient Android background processing pipelines, leveraging Foreground Services, WorkManager, and battery-optimization bypass mechanisms for high-reliability field execution.
* Authored clean, maintainable documentation, schema migrations, and CI workflows across multiple open-source and proprietary codebases.

### **Web Developer & UI/UX Systems Specialist**
*Aduutech, Addis Ababa, Ethiopia* | **Feb 2023 – Nov 2023**
* Developed responsive enterprise web platforms and internal inventory management systems utilizing PHP, Laravel, and MySQL.
* Re-engineered inventory tracking workflows handling 1,000+ daily operational records, reducing order processing latency by 35%.
* Actively participated in weekly sprint planning, rigorous peer code reviews, and schema optimization sessions.

### **Operations & Systems Lead (Hospitality Management)**
*Addis Ababa, Ethiopia* | **Jan 2022 – Jan 2023**
* Supervised end-to-end property operations, front-desk hospitality management, guest reservations, and supplier logistics.
* Implemented digital POS and computerized booking systems, streamlining billing transparency and financial record-keeping.
* Demonstrated high leadership maturity, managing cross-functional service teams, resolving high-pressure client escalations, and optimizing resource allocation.

### **Database Design Intern**
*Ministry of Revenues, Addis Ababa, Ethiopia* | **Oct 2021 – Nov 2021**
* Designed normalized 3NF relational schemas for taxpayer agent registry and auditing modules.
* Collaborated with senior systems architects to write indexing strategies, foreign key constraints, and audit logging triggers.

---

## 🛠️ TECHNICAL COMPETENCIES

* **Programming Languages:** PHP (8.x), Dart, JavaScript (ES6+), Python, SQL, C++, Java/Kotlin basics
* **Frameworks & Libraries:** Laravel, Flutter, Riverpod, Livewire, Filament, Vue.js / React basics, Bootstrap, TailwindCSS
* **Databases & Storage:** MySQL, PostgreSQL, SQLite, Redis caching fundamentals
* **Architecture & Patterns:** Microservices & Modular Monoliths, RESTful API Design, MVC, Repository Pattern, Offline-First Architecture, Concurrency Control (Row Locking, ACID)
* **DevOps & Developer Tools:** Git, GitHub, Linux (Ubuntu/Debian, Bash scripting), Docker fundamentals, Apache/Nginx, cPanel
* **Testing & Quality Assurance:** PHPUnit, Pest PHP, Concurrency Test Suites, Flutter Test Harness

---

## 🌍 LANGUAGES & INTERCULTURAL COMPETENCIES

* **English:** Fluent (Full Professional & Academic Proficiency — Official Medium of Instruction Certified)
* **Amharic:** Native
* **Oromiffa:** Professional Working Proficiency
* **French:** Beginner / Elementary (A1 in-progress — actively acquiring French language and culture)
* **Intercultural Aptitude:** Proven capacity to collaborate in diverse, multi-lingual teams, high adaptability, and strong work ethic in rigorous academic environments.

---

## 📜 VERIFIABLE CREDENTIALS & REFERENCES
* **GitHub Repository:** [https://github.com/fuad745](https://github.com/fuad745)
* **Master Scholarship Dossier:** [https://github.com/fuad745/scholarship-dossier-2026](https://github.com/fuad745/scholarship-dossier-2026)
* Academic transcripts, official English Medium of Instruction certificate, and faculty recommendation letters from St. Mary's University available immediately.
