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
- Other Duckietown RL papers remain expansion candidates pending complete venue/code/hardware mapping. The snow-robust RL paper was subsequently reviewed and added as E46 with its preprint and experimental limitations explicit.
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

## Expansion audit — 2026-09-28

Added 10 papers after publisher, author-manuscript and institutional checks. Stable IDs are retained; gaps correspond to removed entries. Publication/volume year determines sorting, with draft and online-first dates noted. Latest-first chronological index spans all sections; each detailed table is also sorted newest-first. Newly included Nature-family and T-ITS journals are not automatically assigned a quartile.

Searches also surfaced robotics manipulation (Jetson-PI), future/embargoed theses and a deadline-aware demo without sufficient primary-source confirmation; these were not added.

### E42

**Efficient Real-World Autonomous Racing via Attenuated Residual Policy Optimization** — Manuscript identifies onboard compute and author code. Training progressively removes the base controller, leaving a standalone deployed neural policy. Reported latency includes preprocessing and ROS 2 publishing; not compared as a universal benchmark.

Primary record: https://arxiv.org/abs/2603.12960

### E41

**NeoRacer: An Open, Standardized 1:12 Scale Autonomous Race Car for Benchmarking and Education** — Author manuscript links an organization containing the resources, not one paper-specific repository. No peer-reviewed venue asserted. Platform demonstrations are not a comprehensive control-algorithm benchmark.

Primary record: https://arxiv.org/abs/2607.26855

### E33

**Pocket Racer: An accessible autonomous racing educational platform** — Published 29 April 2026. Publisher hardware and data-availability sections identify the board and code. Dataset is available upon request, not assumed freely downloadable. Quartile not independently verified.

Primary record: https://www.nature.com/articles/s41598-026-49690-x

### E36

**Enhancing Safety in Autonomous Racing With Constrained Reinforcement Learning** — Publisher abstract confirms zero-shot physical deployment. Included as a scaled-car study; no Pi/Jetson model or resource-efficiency claim is inferred.

Primary record: https://ieeexplore.ieee.org/document/10982032/

### E34

**Route-centric ant-inspired memories enable panoramic route-following in a car-like robot** — Published 24 September 2025. Methods identify Antcar onboard Pi 4; code availability links Zenodo. Low computational power figures must not be interpreted as whole-vehicle electrical power. Quartile not independently verified.

Primary record: https://www.nature.com/articles/s41467-025-62327-3

### E40

**Development and Control of an Autonomous RC Racing Car** — Publisher assigns volume year 2024 (MECC 2024), although DOI includes 2025. Onboard lateral control is not fully independent autonomy because the velocity command comes from a host over ROS.

Primary record: https://www.sciencedirect.com/science/article/pii/S2405896325000448

### E35

**TinyLidarNet: 2D LiDAR-based End-to-End Deep Learning Model for F1TENTH Autonomous Racing** — Author repository confirms IROS 2024 despite later indexing dates. Physical racing is distinguished from MCU inference timing. Author manuscript: https://ittc.ku.edu/~heechul/papers/tiny-iros2024-camera.pdf

Primary record: https://arxiv.org/abs/2410.07447

### E38

**Towards Safety Assured End-to-End Vision-Based Control for Autonomous Racing** — Manuscript section 5.2 identifies TX2 onboard. Venue confirmed by author lab: https://air.egr.uh.edu/research/high-performance-control-of-agile-robots/ . Do not label it ICRA solely because adjacent author publications appeared there.

Primary record: https://arxiv.org/abs/2303.02267

### E39

**Learning to drive fast on a DuckieTown highway** — Use 2022 proceedings year, not draft upload date. Author lab confirms April 2022: https://www.intelligentroboticslab.nl/robots/duckiebot/ ; manuscript: https://pure.uva.nl/ws/files/59613018/MCAS_paper_wiggers_v4.pdf

Primary record: https://doi.org/10.1007/978-3-030-95892-3_14

### E37

**An Efficient and Scalable Simulation Model for Autonomous Vehicles With Economical Hardware** — University publication record explicitly describes a physical car despite the title. Online-first 2020, issue March 2021; counted once. Primary institutional record: https://researchportal.tuni.fi/en/publications/an-efficient-and-scalable-simulation-model-for-autonomous-vehicle/

Primary record: https://doi.org/10.1109/TITS.2020.2980855

## Source-focused expansion — 2026-09-28

Added 12 nonduplicate records (E43–E54) using CVF, IEEE and arXiv records plus author-linked code. See [SEARCH_LOG.md](SEARCH_LOG.md) for query families and access limitations. Google Scholar was attempted but its direct search page was inaccessible; no claim of completed Scholar coverage or verified Scholar citation counts is made. CVF-hosted workshop papers remain labeled workshops. CVF-hosted ACCV is identified as ACCV, not CVPR/ICCV. Simulation-only efficient models remain outside physical edge-driving evidence.

### E43

**Latent Imagination Facilitates Zero-Shot Transfer in Autonomous Racing** — IEEE publication identity and arXiv v3 hardware setup confirm the venue and onboard TX2. Preprint 2021 / proceedings 2022, counted once. Authors include Axel Brunnbauer and Luigi Berducci; do not copy misattributed author lists from secondary platform indexes.

Primary record: https://arxiv.org/abs/2103.04909

### E44

**Bypassing the Simulation-to-Reality Gap: Online Reinforcement Learning Using a Supervisor** — arXiv v2 hardware description identifies the board; author proceedings PDF confirms ICAR 2023: https://f1tenth.github.io/publications/Simulation-to-Reality_Gap.pdf . Preprint 2022 and Xplore indexing 2024 do not change proceedings year. Onboard control does not establish that every training step is computed onboard.

Primary record: https://arxiv.org/abs/2209.11082

### E45

**AROLA: A Modular Layered Architecture for Scaled Autonomous Racing** — Section III-C identifies Jetson. Paper reports RoboRacer IV25 deployment. Linked code is the minimal example cited in the paper, not a claim that the entire architecture and Race Monitor are released. Hardware variant remains unknown.

Primary record: https://arxiv.org/abs/2602.02730

### E46

**Tackling Snow-Induced Challenges: Safe Autonomous Lane-Keeping with Robust Reinforcement Learning** — Section V identifies onboard hardware and real-platform fine-tuning. Snow scenarios are principally simulation evidence; do not infer a certified winter-road system or zero-shot transfer. No author code repository was identified.

Primary record: https://arxiv.org/abs/2512.12987

### E47

**EdgeVTP: Exploration of Latency-efficient Trajectory Prediction for Edge-based Embedded Vision Applications** — CVF paper and author repository agree on edge evaluation. Highway surveillance prediction is an adjacent supporting task, not ego-vehicle steering or physical autonomous driving. Repository H100 timing table must not be read as Jetson timing.

Primary record: https://openaccess.thecvf.com/content/CVPR2026W/EVW/html/Kim_EdgeVTP_Exploration_of_Latency-efficient_Trajectory_Prediction_for_Edge-based_Embedded_Vision_CVPRW_2026_paper.html

### E48

**Towards Accurate and Efficient 3D Object Detection for Autonomous Driving: A Mixture of Experts Computing System on Edge** — CVF PDF experiment section specifies AGX Orin and first-page footnote supplies code. IEEE indexing date is 2026, but conference year is 2025. Do not repeat the manuscript wording about a greater-than-100% latency reduction; reported speedups are not equivalent to such reductions. Potentially related EMOS TPAMI paper is held out pending overlap review.

Primary record: https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Towards_Accurate_and_Efficient_3D_Object_Detection_for_Autonomous_Driving_ICCV_2025_paper.html

### E49

**HARD: Hardware-Aware Lightweight Real-Time Semantic Segmentation Model Deployable from Edge to GPU** — CVF PDF sections 4.1 and 4.4 specify embedded boards. MCU variant and resolution differ from GPU variants; do not combine accuracy from one setting with FPS from another. No closed-loop vehicle demonstrated.

Primary record: https://openaccess.thecvf.com/content/ACCV2024/html/Kwon_HARD__Hardware-Aware_lightweight_Real-time_semantic_segmentation_model_Deployable_from_ACCV_2024_paper.html

### E50

**ES3Net: Accurate and Efficient Edge-Based Self-Supervised Stereo Matching Network** — CVF abstract identifies TX2 and repository confirms authorship. Relevant as a perception component; the paper also targets drones and is not a closed-loop road-driving demonstration. Workshop status is explicit.

Primary record: https://openaccess.thecvf.com/content/CVPR2023W/EVW/html/Fang_ES3Net_Accurate_and_Efficient_Edge-Based_Self-Supervised_Stereo_Matching_Network_CVPRW_2023_paper.html

### E51

**ProAI: An Efficient Embedded AI Hardware for Automotive Applications — A Benchmark Study** — Primary CVF paper: https://openaccess.thecvf.com/content/ICCV2021W/ERCVAD/papers/Mantowsky_ProAI_An_Efficient_Embedded_AI_Hardware_for_Automotive_Applications_-_ICCVW_2021_paper.pdf . ProAI is automotive compute, not a miniature car. Board-level inference/power comparison does not demonstrate complete autonomous control.

Primary record: https://arxiv.org/abs/2108.05170

### E52

**VLDrive: Vision-Augmented Lightweight MLLMs for Efficient Language-grounded Autonomous Driving** — Included only as an efficiency-oriented algorithmic comparison. CVF abstract links author code and reports simulator evaluation. Lightweight relative to a 7B model does not imply feasibility on Pi or a small Jetson.

Primary record: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_VLDrive_Vision-Augmented_Lightweight_MLLMs_for_Efficient_Language-grounded_Autonomous_Driving_ICCV_2025_paper.html

### E53

**VAD: Vectorized Scene Representation for Efficient Autonomous Driving** — CVF record confirms title, venue and code. Efficiency baseline only: open-loop planning metrics and relative speedup are not evidence of physical embedded closed-loop driving.

Primary record: https://openaccess.thecvf.com/content/ICCV2023/html/Jiang_VAD_Vectorized_Scene_Representation_for_Efficient_Autonomous_Driving_ICCV_2023_paper.html

### E54

**A Comparative Study of Scaled Autonomous Vehicle Platforms for Research and Education** — IEEE abstract and proceedings metadata verified. This is a platform comparison, not a new end-to-end driving model or an independent experiment for every reviewed platform. MHTC is not treated as ICRA/IROS-equivalent by association with IEEE.

Primary record: https://ieeexplore.ieee.org/document/11086476/
