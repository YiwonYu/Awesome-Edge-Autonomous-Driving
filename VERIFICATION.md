# Verification record

Snapshot: 2026-09-28. Sources were discovered through publisher pages, arXiv, author/university pages, platform repositories and backward references from small-scale-car surveys. Search families combined device names (Raspberry Pi, Jetson, Coral, Edge TPU, Hailo, Pico, MCU) with autonomous driving, racing, lane following, TinyML, sim2real and 2020–2026. Venue-focused searches included RA-L, TMECH, ICRA, IROS, JFR, RTCSA and EMSOFT. Search ranking and venue reputation alone do not establish deployment evidence.

## Inclusion and verification rules

1. Prefer publisher/DOI, author manuscript and author-owned code over secondary summaries.
2. Record explicit hardware; never convert a training GPU into an onboard device claim.
3. Separate closed-loop real vehicles, simulated control, hardware inference benchmarks and offboard control.
4. Merge preprint/final versions and conference presentations of the same article. Distinct papers sharing a platform remain separate.
5. Do not invent code links. “Resource” may be a project page, ecosystem or archived artifact; the per-entry notes explain this.
6. HTTP checks measure reachability, not scholarly truth. Publisher 403/429 and transport errors are inconclusive, not broken-link findings. A 200 response can still be a login/challenge page. Primary contents were also inspected during research; no experiments were reproduced.
7. This is a curated first release; no PRISMA-style systematic-review or exhaustive-coverage claim. Quartile-unverified sources remain visible when directly relevant.

## Corrections, duplicate handling and excluded candidates

- The RA-L optimization paper is one work: 2023 early publication, 2024 volume and ICRA presentation.
- TimelyNet is one TECS/EMSOFT work; the author-linked Zenodo artifact is preferred over an unconfirmed similarly titled GitHub repository.
- The speed/delay Sensors article and arXiv 2312.06670 are not separate papers.
- DeepPicar, DeepPicarMicro, DeepPicar-v3 and DeepPiCar are not interchangeable names.
- `wcharczuk/go-chart` is a plotting library and is excluded from Go-CHART robotics code.
- `MichaelBosello/self-driving-car` describes separate cars across a fleet (two Jetson Nano cars and one Pi car), not three computers installed together on one vehicle. It is omitted from the short pre-2020 section to keep that section focused.
- The Raspberry Pi 5 / Hailo ROS 2 community project discovered during search says closed-loop testing is pending; it is not included as proven autonomous driving.
- Snow-robust RL (arXiv 2512.12987), safety-assured vision racing (arXiv 2303.02267), and some Duckietown RL papers remain expansion candidates pending complete venue/code/hardware mapping. They are not counted as verified catalog records.
- Surveys, perception-only papers and generic projects are not counted as independent real-car demonstrations.

## Per-entry evidence notes

### E01

**Vision-Based Autonomous Car Racing Using Deep Imitative Reinforcement Learning** — Author project page; linked platform code must not be assumed to reproduce the full DIRL method.

Primary record: https://arxiv.org/abs/2107.08325

### E02

**Nigel—Mechatronic Design and Robust Sim2Real Control of an Overactuated Autonomous Vehicle** — Final journal version 2024; AutoDRIVE is the ecosystem hub, not a standalone paper reproduction package.

Primary record: https://arxiv.org/abs/2401.11542

### E03

**Model Optimization in Deep Learning Based Robot Control for Autonomous Driving** — 2023 online-first / 2024 issue and ICRA presentation are one work. No physical edge-car claim. Evaluation tool: https://github.com/JdeRobot/BehaviorMetrics

Primary record: https://roboticslaburjc.github.io/publications/2023/model_optimization_in_deep_learning_based_robot_control_for_autonomous_driving

### E04

**ForzaETH Race Stack—Scaled Autonomous Head-to-Head Racing on Fully Commercial Off-the-Shelf Hardware** — Adjacent small-vehicle x86 platform, not a Pi/Jetson experiment. Primary project: https://www.forzaeth.ch/blog/full_system_paper/

Primary record: https://arxiv.org/abs/2403.11784

### E05

**Learning-Based On-Track System Identification for Scaled Autonomous Racing in Under a Minute** — 2024 preprint, 2025 journal article. Shared ecosystem code; do not assume every branch reproduces this paper.

Primary record: https://arxiv.org/abs/2411.17508

### E06

**F1TENTH: An Open-source Evaluation Environment for Continuous Control and Reinforcement Learning** — Publication year 2020; competition track, not NeurIPS main track. Paper hardware section specifies TX2; gym link is simulator code.

Primary record: https://proceedings.mlr.press/v123/o-kelly20a.html

### E07

**A platform-agnostic deep reinforcement learning framework for effective Sim2Real transfer towards autonomous driving** — Paper and author page identify two Duckiebot hardware versions. Journal quartile not verified.

Primary record: https://www.nature.com/articles/s44172-024-00292-3

### E08

**DeepPicarMicro: Applying TinyML to Autonomous Cyber Physical Systems** — MCU runs inference onboard; offboard training is distinct. Author camera-ready and repository verified.

Primary record: https://ittc.ku.edu/~heechul/papers/DeepPicarMicro-rtcsa2022-camera.pdf

### E09

**TimelyNet: Adaptive Neural Architecture for Autonomous Driving with Dynamic Deadline** — Author PDF: https://tanrui.github.io/pub/TimelyNet-EMSOFT.pdf ; hardware evaluation is not evidence of physical road driving. Official archived artifact preferred over an unconfirmed GitHub match.

Primary record: https://doi.org/10.1145/3762652

### E10

**The Effects of Speed and Delays on Test-Time Performance of End-to-End Self-Driving** — DOI 10.3390/s24061963. Earlier arXiv 2312.06670 is the same work with a different title; supplementary data: https://doi.org/10.6084/m9.figshare.24948690

Primary record: https://www.mdpi.com/1424-8220/24/6/1963

### E11

**Neural Network Models for Driving Control of Indoor Autonomous Vehicles in Mobile Edge Computing** — DOI 10.3390/s23052575; open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC10007646/

Primary record: https://www.mdpi.com/1424-8220/23/5/2575

### E12

**AutoDRIVE: A Comprehensive, Flexible and Integrated Digital Twin Ecosystem for Autonomous Driving Research & Education** — DOI 10.3390/robotics12030077. Nigel/AutoDRIVE papers share infrastructure but address distinct contributions; do not count them as independent hardware platforms.

Primary record: https://www.mdpi.com/2218-6581/12/3/77

### E13

**Miniature Autonomy as Means to Find New Approaches in Reliable Autonomous Driving AI Method Design** — Road-vehicle part included; aerial-robot examples outside scope. Coral acceleration does not imply all control runs on TPU.

Primary record: https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2022.846355/full

### E16

**Run Your 3D Object Detector on NVIDIA Jetson Platforms: A Benchmark Analysis** — DOI 10.3390/s23084005. Does not establish closed-loop autonomous driving.

Primary record: https://www.mdpi.com/1424-8220/23/8/4005

### E17

**Real-Time 3D Object Detection Using InnovizOne LiDAR and Low-Power Hailo-8 AI Accelerator** — Preprint status; no physical closed-loop driving evidence. Canonical GitHub URL checked separately because paper text contains spacing artifacts.

Primary record: https://arxiv.org/abs/2412.05594

### E18

**Efficient On-Chip Implementation of 4D Radar-Based 3D Object Detection on Hailo-8L** — Do not equate accelerator throughput with end-to-end vehicle control frequency.

Primary record: https://arxiv.org/abs/2505.00757

### E19

**A Serverless Edge-Native Data Processing Architecture for Autonomous Driving Training** — Supporting infrastructure, not a demonstrated driving policy.

Primary record: https://arxiv.org/abs/2601.22919

### E20

**Chronos and CRS: Design of a Miniature Car-Like Robot and a Software Framework for Single and Multi-Agent Robotics and Control** — 2022 preprint / 2023 proceedings. ESP32 executes low-level loops; do not describe the complete MPC pipeline as onboard TinyML.

Primary record: https://arxiv.org/abs/2209.12048

### E21

**Go-CHART: A Miniature Remotely Accessible Self-Driving Car Robot** — Not a fully self-contained Pi-only autonomy demonstration. The similarly named wcharczuk/go-chart is unrelated plotting software.

Primary record: https://par.nsf.gov/servlets/purl/10277361

### E22

**High-Speed Autonomous Racing Using Trajectory-Aided Deep Reinforcement Learning** — Useful control baseline; excluded from physical embedded-deployment evidence.

Primary record: https://arxiv.org/abs/2306.07003

### E23

**DeepPicar-v3** — Offboard/Colab training; repository creation year is not a paper publication year.

Primary record: https://github.com/CSL-KU/DeepPicar-v3

### E24

**ResAwareWoR** — Publication venue not established; kept as project rather than peer-reviewed evidence.

Primary record: https://github.com/CSL-KU/ResAwareWoR

### E25

**A Survey on Approximate Edge AI for Energy Efficient Autonomous Driving Services** — Survey context, not a new hardware experiment.

Primary record: https://arxiv.org/abs/2304.14271

### E26

**Autonomous Driving Small-Scale Cars: A Survey of Recent Development** — Authors: Dianzhao Li, Paul Auerbach and Ostap Okhrin. Used for discovery; individual primary sources determine catalog claims.

Primary record: https://arxiv.org/abs/2404.06229

### E27

**Unifying F1TENTH Autonomous Racing: Survey, Methods and Benchmarks** — No uniform onboard deployment claim for all included algorithms.

Primary record: https://arxiv.org/abs/2402.18558

### E28

**Autonomous Vehicles on the Edge: A Survey on Autonomous Vehicle Racing** — “On the edge” includes limits of racing performance; title alone does not establish resource-constrained computing.

Primary record: https://arxiv.org/abs/2202.07008

### E29

**DeepPicar: A Low-cost Deep Neural Network-based Autonomous Car** — Pre-2020 foundation; distinct from dctian/DeepPiCar.

Primary record: https://doi.org/10.1109/RTCSA.2018.00011

### E30

**DonkeyCar** — Legacy platform used by 2020–2026 studies. Current device support depends on release; training may be offboard.

Primary record: https://github.com/autorope/donkeycar

### E31

**JetRacer** — Legacy ecosystem reference; repository age/activity is not a support guarantee.

Primary record: https://github.com/NVIDIA-AI-IOT/jetracer

### E32

**DeepPiCar** — Different project from DeepPicar; individual neural tasks can use Coral, not all control operations.

Primary record: https://github.com/dctian/DeepPiCar


## Link audit outcome

The draft DeepPicar link returned 404 and was replaced by the author-linked `mbechtel2/DeepPicar-v2` repository. Other publisher access challenges/timeouts are preserved in link-checks.json rather than misreported as dead links. GitHub API metadata is stored in [repository-checks.json](repository-checks.json); successful API reads confirm repository identity, not reproducibility.
