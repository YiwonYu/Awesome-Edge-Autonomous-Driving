# Awesome Edge Autonomous Driving

A curated research list for autonomous cars with limited onboard compute: **Raspberry Pi, NVIDIA Jetson, Coral / Edge TPU, Hailo and microcontrollers**.

**Coverage:** 2020–2026, searched through **2026-09-28**; selected older foundations are separate. This is a broad curated bibliography, not a claim that every relevant publication has been found. No future 2026 publications are inferred.

**Selection:** Prioritize major robotics conferences and journals with verifiable Q1/Q2 evidence. Distinguish real-vehicle driving, simulation, offboard computation and perception-only experiments. Conferences are not assigned a Journal Impact Factor; journal quartiles depend on the metric and year.

- [Venue quality and ranking evidence](VENUES.md)
- [Sources, verification and exclusions](VERIFICATION.md)
- [Machine-readable catalog](catalog.json)
- [Link-check results](link-checks.json)
- [Source-focused search log](SEARCH_LOG.md)
- [Contributing](CONTRIBUTING.md)

## Reading guide

Start with **DIRL (RA-L)** and **Nigel (TMECH)** for physical embedded cars; **DeepPicarMicro** for MCU inference; **TimelyNet** for embedded timing. The model-optimization RA-L paper is a simulation reference. ForzaETH uses onboard x86 and is an adjacent platform, not a Jetson result.

Training hardware and inference hardware are different. “Real” means the authors report physical vehicle experiments, not that this list has reproduced them. “Not identified” means a public implementation was not verified, not that none exists. A shared platform repository is not necessarily the implementation of every associated paper. Device uncertainty is explicit.

**Ordering:** Newest publication year first, both in the chronological index and within each section. Same-year entries are alphabetical. Preprint and issue-year differences are recorded in the evidence notes.

## Contents

- [Chronological index](#chronological-index)
- [Priority papers](#priority-papers)
- [Specialist and additional papers](#specialist-and-additional-papers)
- [Recent preprints](#recent-preprints)
- [Perception and supporting systems](#perception-and-supporting-systems)
- [Simulation and offboard-control references](#simulation-and-offboard-control-references)
- [Open-source projects](#open-source-projects)
- [Surveys](#surveys)
- [Foundations and legacy platforms](#foundations-and-legacy-platforms)

## Chronological index

| Year | Paper / Project | Category |
|---|---|---|
| 2026 | [A Serverless Edge-Native Data Processing Architecture for Autonomous Driving Training](https://arxiv.org/abs/2601.22919) | Perception and supporting systems |
| 2026 | [AROLA: A Modular Layered Architecture for Scaled Autonomous Racing](https://arxiv.org/abs/2602.02730) | Recent preprints |
| 2026 | [EdgeVTP: Exploration of Latency-efficient Trajectory Prediction for Edge-based Embedded Vision Applications](https://openaccess.thecvf.com/content/CVPR2026W/EVW/html/Kim_EdgeVTP_Exploration_of_Latency-efficient_Trajectory_Prediction_for_Edge-based_Embedded_Vision_CVPRW_2026_paper.html) | Perception and supporting systems |
| 2026 | [Efficient Real-World Autonomous Racing via Attenuated Residual Policy Optimization](https://arxiv.org/abs/2603.12960) | Recent preprints |
| 2026 | [NeoRacer: An Open, Standardized 1:12 Scale Autonomous Race Car for Benchmarking and Education](https://arxiv.org/abs/2607.26855) | Recent preprints |
| 2026 | [Pocket Racer: An accessible autonomous racing educational platform](https://www.nature.com/articles/s41598-026-49690-x) | Priority papers |
| 2025 | [A Comparative Study of Scaled Autonomous Vehicle Platforms for Research and Education](https://ieeexplore.ieee.org/document/11086476/) | Surveys |
| 2025 | [Efficient On-Chip Implementation of 4D Radar-Based 3D Object Detection on Hailo-8L](https://arxiv.org/abs/2505.00757) | Perception and supporting systems |
| 2025 | [Enhancing Safety in Autonomous Racing With Constrained Reinforcement Learning](https://ieeexplore.ieee.org/document/10982032/) | Priority papers |
| 2025 | [Learning-Based On-Track System Identification for Scaled Autonomous Racing in Under a Minute](https://arxiv.org/abs/2411.17508) | Priority papers |
| 2025 | [ResAwareWoR](https://github.com/CSL-KU/ResAwareWoR) | Open-source projects |
| 2025 | [Route-centric ant-inspired memories enable panoramic route-following in a car-like robot](https://www.nature.com/articles/s41467-025-62327-3) | Priority papers |
| 2025 | [Tackling Snow-Induced Challenges: Safe Autonomous Lane-Keeping with Robust Reinforcement Learning](https://arxiv.org/abs/2512.12987) | Recent preprints |
| 2025 | [TimelyNet: Adaptive Neural Architecture for Autonomous Driving with Dynamic Deadline](https://doi.org/10.1145/3762652) | Specialist and additional papers |
| 2025 | [Towards Accurate and Efficient 3D Object Detection for Autonomous Driving: A Mixture of Experts Computing System on Edge](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Towards_Accurate_and_Efficient_3D_Object_Detection_for_Autonomous_Driving_ICCV_2025_paper.html) | Perception and supporting systems |
| 2025 | [VLDrive: Vision-Augmented Lightweight MLLMs for Efficient Language-grounded Autonomous Driving](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_VLDrive_Vision-Augmented_Lightweight_MLLMs_for_Efficient_Language-grounded_Autonomous_Driving_ICCV_2025_paper.html) | Simulation and offboard-control references |
| 2024 | [A platform-agnostic deep reinforcement learning framework for effective Sim2Real transfer towards autonomous driving](https://www.nature.com/articles/s44172-024-00292-3) | Priority papers |
| 2024 | [Autonomous Driving Small-Scale Cars: A Survey of Recent Development](https://arxiv.org/abs/2404.06229) | Surveys |
| 2024 | [Development and Control of an Autonomous RC Racing Car](https://www.sciencedirect.com/science/article/pii/S2405896325000448) | Simulation and offboard-control references |
| 2024 | [ForzaETH Race Stack—Scaled Autonomous Head-to-Head Racing on Fully Commercial Off-the-Shelf Hardware](https://arxiv.org/abs/2403.11784) | Priority papers |
| 2024 | [HARD: Hardware-Aware Lightweight Real-Time Semantic Segmentation Model Deployable from Edge to GPU](https://openaccess.thecvf.com/content/ACCV2024/html/Kwon_HARD__Hardware-Aware_lightweight_Real-time_semantic_segmentation_model_Deployable_from_ACCV_2024_paper.html) | Perception and supporting systems |
| 2024 | [Model Optimization in Deep Learning Based Robot Control for Autonomous Driving](https://roboticslaburjc.github.io/publications/2023/model_optimization_in_deep_learning_based_robot_control_for_autonomous_driving) | Priority papers |
| 2024 | [Nigel—Mechatronic Design and Robust Sim2Real Control of an Overactuated Autonomous Vehicle](https://arxiv.org/abs/2401.11542) | Priority papers |
| 2024 | [Real-Time 3D Object Detection Using InnovizOne LiDAR and Low-Power Hailo-8 AI Accelerator](https://arxiv.org/abs/2412.05594) | Perception and supporting systems |
| 2024 | [The Effects of Speed and Delays on Test-Time Performance of End-to-End Self-Driving](https://www.mdpi.com/1424-8220/24/6/1963) | Specialist and additional papers |
| 2024 | [TinyLidarNet: 2D LiDAR-based End-to-End Deep Learning Model for F1TENTH Autonomous Racing](https://arxiv.org/abs/2410.07447) | Priority papers |
| 2024 | [Unifying F1TENTH Autonomous Racing: Survey, Methods and Benchmarks](https://arxiv.org/abs/2402.18558) | Surveys |
| 2023 | [A Survey on Approximate Edge AI for Energy Efficient Autonomous Driving Services](https://arxiv.org/abs/2304.14271) | Surveys |
| 2023 | [AutoDRIVE: A Comprehensive, Flexible and Integrated Digital Twin Ecosystem for Autonomous Driving Research & Education](https://www.mdpi.com/2218-6581/12/3/77) | Specialist and additional papers |
| 2023 | [Bypassing the Simulation-to-Reality Gap: Online Reinforcement Learning Using a Supervisor](https://arxiv.org/abs/2209.11082) | Specialist and additional papers |
| 2023 | [Chronos and CRS: Design of a Miniature Car-Like Robot and a Software Framework for Single and Multi-Agent Robotics and Control](https://arxiv.org/abs/2209.12048) | Simulation and offboard-control references |
| 2023 | [ES3Net: Accurate and Efficient Edge-Based Self-Supervised Stereo Matching Network](https://openaccess.thecvf.com/content/CVPR2023W/EVW/html/Fang_ES3Net_Accurate_and_Efficient_Edge-Based_Self-Supervised_Stereo_Matching_Network_CVPRW_2023_paper.html) | Perception and supporting systems |
| 2023 | [High-Speed Autonomous Racing Using Trajectory-Aided Deep Reinforcement Learning](https://arxiv.org/abs/2306.07003) | Simulation and offboard-control references |
| 2023 | [Neural Network Models for Driving Control of Indoor Autonomous Vehicles in Mobile Edge Computing](https://www.mdpi.com/1424-8220/23/5/2575) | Specialist and additional papers |
| 2023 | [Run Your 3D Object Detector on NVIDIA Jetson Platforms: A Benchmark Analysis](https://www.mdpi.com/1424-8220/23/8/4005) | Perception and supporting systems |
| 2023 | [Towards Safety Assured End-to-End Vision-Based Control for Autonomous Racing](https://arxiv.org/abs/2303.02267) | Specialist and additional papers |
| 2023 | [VAD: Vectorized Scene Representation for Efficient Autonomous Driving](https://openaccess.thecvf.com/content/ICCV2023/html/Jiang_VAD_Vectorized_Scene_Representation_for_Efficient_Autonomous_Driving_ICCV_2023_paper.html) | Simulation and offboard-control references |
| 2022 | [Autonomous Vehicles on the Edge: A Survey on Autonomous Vehicle Racing](https://arxiv.org/abs/2202.07008) | Surveys |
| 2022 | [DeepPicar-v3](https://github.com/CSL-KU/DeepPicar-v3) | Open-source projects |
| 2022 | [DeepPicarMicro: Applying TinyML to Autonomous Cyber Physical Systems](https://ittc.ku.edu/~heechul/papers/DeepPicarMicro-rtcsa2022-camera.pdf) | Specialist and additional papers |
| 2022 | [Latent Imagination Facilitates Zero-Shot Transfer in Autonomous Racing](https://arxiv.org/abs/2103.04909) | Priority papers |
| 2022 | [Learning to drive fast on a DuckieTown highway](https://doi.org/10.1007/978-3-030-95892-3_14) | Specialist and additional papers |
| 2022 | [Miniature Autonomy as Means to Find New Approaches in Reliable Autonomous Driving AI Method Design](https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2022.846355/full) | Specialist and additional papers |
| 2021 | [An Efficient and Scalable Simulation Model for Autonomous Vehicles With Economical Hardware](https://doi.org/10.1109/TITS.2020.2980855) | Priority papers |
| 2021 | [ProAI: An Efficient Embedded AI Hardware for Automotive Applications — A Benchmark Study](https://arxiv.org/abs/2108.05170) | Perception and supporting systems |
| 2021 | [Vision-Based Autonomous Car Racing Using Deep Imitative Reinforcement Learning](https://arxiv.org/abs/2107.08325) | Priority papers |
| 2020 | [F1TENTH: An Open-source Evaluation Environment for Continuous Control and Reinforcement Learning](https://proceedings.mlr.press/v123/o-kelly20a.html) | Priority papers |
| 2020 | [Go-CHART: A Miniature Remotely Accessible Self-Driving Car Robot](https://par.nsf.gov/servlets/purl/10277361) | Simulation and offboard-control references |
| 2019 | [DeepPiCar](https://github.com/dctian/DeepPiCar) | Foundations and legacy platforms |
| 2019 | [JetRacer](https://github.com/NVIDIA-AI-IOT/jetracer) | Foundations and legacy platforms |
| 2018 | [DeepPicar: A Low-cost Deep Neural Network-based Autonomous Car](https://doi.org/10.1109/RTCSA.2018.00011) | Foundations and legacy platforms |
| 2016 | [DonkeyCar](https://github.com/autorope/donkeycar) | Foundations and legacy platforms |

## Priority papers

| Year | Paper / Project | Device | Model / Method | Task | Venue | Code / GitHub | Real / Simulation |
|---|---|---|---|---|---|---|---|
| 2026 | [Pocket Racer: An accessible autonomous racing educational platform](https://www.nature.com/articles/s41598-026-49690-x) ([E33](VERIFICATION.md#e33)) | Raspberry Pi Zero 2 W; 1:28 vehicle | Behavior cloning; CNN, 3D CNN, LRCN and ViT benchmarks | Indoor head-to-head racing and overtaking | Scientific Reports 16:19899; DOI 10.1038/s41598-026-49690-x | [Resource](https://github.com/PocketRacers/PocketRacerRepo) | Real vehicle |
| 2025 | [Enhancing Safety in Autonomous Racing With Constrained Reinforcement Learning](https://ieeexplore.ieee.org/document/10982032/) ([E36](VERIFICATION.md#e36)) | Real 1:10 racecar; exact onboard processor not verified | Constrained RL; rollover-dynamics shielding | Collision reduction in autonomous racing | IEEE RA-L 10(6):6448–6455; DOI 10.1109/LRA.2025.3566591 | Not identified | Real + F1TENTH simulation |
| 2025 | [Learning-Based On-Track System Identification for Scaled Autonomous Racing in Under a Minute](https://arxiv.org/abs/2411.17508) ([E05](VERIFICATION.md#e05)) | Scaled ForzaETH vehicle; exact compute not independently verified | Residual neural system identification | Rapid dynamics adaptation | IEEE RA-L 10(2); DOI 10.1109/LRA.2025.3527336 | [Resource](https://github.com/ForzaETH/race_stack) | Real vehicle |
| 2025 | [Route-centric ant-inspired memories enable panoramic route-following in a car-like robot](https://www.nature.com/articles/s41467-025-62327-3) ([E34](VERIFICATION.md#e34)) | Raspberry Pi 4 Model B; panoramic camera | Insect mushroom-body-inspired visual memory; self-supervised route learning | Outdoor visual route following | Nature Communications; DOI 10.1038/s41467-025-62327-3 | [Resource](https://doi.org/10.5281/zenodo.15783472) | Real vehicle |
| 2024 | [A platform-agnostic deep reinforcement learning framework for effective Sim2Real transfer towards autonomous driving](https://www.nature.com/articles/s44172-024-00292-3) ([E07](VERIFICATION.md#e07)) | Raspberry Pi 3B (DB19); Jetson Nano 2GB (DB21) | Affordance perception + recurrent DRL | Lane following and overtaking | Communications Engineering 3:147 | [Resource](https://github.com/DailyL/Sim2Real_autonomous_vehicle) | Real + simulation |
| 2024 | [ForzaETH Race Stack—Scaled Autonomous Head-to-Head Racing on Fully Commercial Off-the-Shelf Hardware](https://arxiv.org/abs/2403.11784) ([E04](VERIFICATION.md#e04)) | Intel Core i7-8850U; onboard x86, no GPU | Modular localization, planning and control | 1:10 head-to-head racing | Journal of Field Robotics; DOI 10.1002/rob.22429 | [Resource](https://github.com/ForzaETH/race_stack) | Real + simulation |
| 2024 | [Model Optimization in Deep Learning Based Robot Control for Autonomous Driving](https://roboticslaburjc.github.io/publications/2023/model_optimization_in_deep_learning_based_robot_control_for_autonomous_driving) ([E03](VERIFICATION.md#e03)) | Constrained-compute evaluation; exact board not verified | PilotNet pruning, quantization, clustering, TensorRT | Visual lane following | IEEE RA-L 9(1); DOI 10.1109/LRA.2023.3336244 | [Resource](https://github.com/JdeRobot/DeepLearningStudio) | CARLA simulation |
| 2024 | [Nigel—Mechatronic Design and Robust Sim2Real Control of an Overactuated Autonomous Vehicle](https://arxiv.org/abs/2401.11542) ([E02](VERIFICATION.md#e02)) | Jetson Orin Nano + Arduino Mega | Robust multi-model control; 4WD/4WS | Sim2real vehicle control | IEEE/ASME TMECH 29(4); DOI 10.1109/TMECH.2024.3401077 | [Resource](https://github.com/Tinker-Twins/AutoDRIVE) | Real + simulation |
| 2024 | [TinyLidarNet: 2D LiDAR-based End-to-End Deep Learning Model for F1TENTH Autonomous Racing](https://arxiv.org/abs/2410.07447) ([E35](VERIFICATION.md#e35)) | Jetson NX; ESP32-S3 and Raspberry Pi Pico inference ports | 1D CNN; behavior cloning; INT8 TFLite Micro | LiDAR-to-steering/throttle racing | IEEE IROS 2024, 2878–2884; DOI 10.1109/IROS58592.2024.10801430 | [Resource](https://github.com/CSL-KU/TinyLidarNet) | Real + simulation; additional MCU inference benchmarks |
| 2022 | [Latent Imagination Facilitates Zero-Shot Transfer in Autonomous Racing](https://arxiv.org/abs/2103.04909) ([E43](VERIFICATION.md#e43)) | Jetson TX2; F1TENTH and Hokuyo LiDAR | Dreamer world models; latent-space policy learning | Zero-shot sim2real racing | IEEE ICRA 2022:7513–7520; DOI 10.1109/ICRA46639.2022.9811650 | [Resource](https://github.com/CPS-TUWien/racing_dreamer) | Real + simulation |
| 2021 | [An Efficient and Scalable Simulation Model for Autonomous Vehicles With Economical Hardware](https://doi.org/10.1109/TITS.2020.2980855) ([E37](VERIFICATION.md#e37)) | Single Raspberry Pi; exact revision not verified | Lightweight deep learning; camera and ultrasonic sensing | Track following, traffic signs and obstacle avoidance | IEEE T-ITS 22(3):1718–1732 | Not identified | Physical model car |
| 2021 | [Vision-Based Autonomous Car Racing Using Deep Imitative Reinforcement Learning](https://arxiv.org/abs/2107.08325) ([E01](VERIFICATION.md#e01)) | Jetson Nano; miniature RC car | Imitation learning + model-based RL | Vision racing | IEEE RA-L 6(4); DOI 10.1109/LRA.2021.3097345 | [Resource](https://caipeide.github.io/autorace-dirl/) | Real + simulation |
| 2020 | [F1TENTH: An Open-source Evaluation Environment for Continuous Control and Reinforcement Learning](https://proceedings.mlr.press/v123/o-kelly20a.html) ([E06](VERIFICATION.md#e06)) | Jetson TX2; Xavier/Nano variants supported | Open platform and continuous-control benchmark | 1:10 autonomous racing | PMLR 123; NeurIPS 2019 Competition & Demonstration Track | [Resource](https://github.com/f1tenth/f1tenth_gym) | Real platform + simulation |

## Specialist and additional papers

| Year | Paper / Project | Device | Model / Method | Task | Venue | Code / GitHub | Real / Simulation |
|---|---|---|---|---|---|---|---|
| 2025 | [TimelyNet: Adaptive Neural Architecture for Autonomous Driving with Dynamic Deadline](https://doi.org/10.1145/3762652) ([E09](VERIFICATION.md#e09)) | Jetson AGX Orin | Runtime architecture adaptation; InterFuser | Deadline-aware driving pipeline | ACM TECS / EMSOFT 2025 | [Resource](https://doi.org/10.5281/zenodo.16251024) | CARLA + embedded hardware evaluation |
| 2024 | [The Effects of Speed and Delays on Test-Time Performance of End-to-End Self-Driving](https://www.mdpi.com/1424-8220/24/6/1963) ([E10](VERIFICATION.md#e10)) | Raspberry Pi 4B / Donkey S1 | Time-shifted target commands; end-to-end learning | Delay-aware lane driving | Sensors 24(6):1963 | Not identified | Real vehicle |
| 2023 | [AutoDRIVE: A Comprehensive, Flexible and Integrated Digital Twin Ecosystem for Autonomous Driving Research & Education](https://www.mdpi.com/2218-6581/12/3/77) ([E12](VERIFICATION.md#e12)) | Jetson-based miniature vehicle; generation-dependent hardware | Digital twins, perception and control tooling | Autonomy research platform | Robotics 12(3):77 | [Resource](https://github.com/Tinker-Twins/AutoDRIVE) | Real + simulation |
| 2023 | [Bypassing the Simulation-to-Reality Gap: Online Reinforcement Learning Using a Supervisor](https://arxiv.org/abs/2209.11082) ([E44](VERIFICATION.md#e44)) | Jetson NX as described in manuscript; 1:10 F1TENTH | DRL with model-based safety supervisor | Online learning on physical racing car | IEEE ICAR 2023:325–331; DOI 10.1109/ICAR58858.2023.10406465 | Not identified | Real + simulation |
| 2023 | [Neural Network Models for Driving Control of Indoor Autonomous Vehicles in Mobile Edge Computing](https://www.mdpi.com/1424-8220/23/5/2575) ([E11](VERIFICATION.md#e11)) | Raspberry Pi + LiDAR; exact board not verified | Neural driving-command classification | Indoor vehicle control | Sensors 23(5):2575 | Not identified | Real vehicle |
| 2023 | [Towards Safety Assured End-to-End Vision-Based Control for Autonomous Racing](https://arxiv.org/abs/2303.02267) ([E38](VERIFICATION.md#e38)) | Jetson TX2, 8GB; twin ZED camera; 1:10 RC car | Imitation learning and state prediction with control barrier functions | Safety-filtered visual racing | IFAC World Congress 2023 | Not identified | Real + CARLA simulation |
| 2022 | [DeepPicarMicro: Applying TinyML to Autonomous Cyber Physical Systems](https://ittc.ku.edu/~heechul/papers/DeepPicarMicro-rtcsa2022-camera.pdf) ([E08](VERIFICATION.md#e08)) | Raspberry Pi Pico / RP2040, 264KB SRAM | TFLite Micro; quantized and optimized PilotNet | End-to-end miniature car steering | IEEE RTCSA 2022 | [Resource](https://github.com/CSL-KU/DeepPicarMicro) | Real + simulation-based model evaluation |
| 2022 | [Learning to drive fast on a DuckieTown highway](https://doi.org/10.1007/978-3-030-95892-3_14) ([E39](VERIFICATION.md#e39)) | NVIDIA JetRacer / Jetson Nano platform | PPO; simulator-to-real transfer | Visual lane following at different speeds | Intelligent Autonomous Systems 16; LNNS 412:183–194 | Not identified | Real + simulation |
| 2022 | [Miniature Autonomy as Means to Find New Approaches in Reliable Autonomous Driving AI Method Design](https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2022.846355/full) ([E13](VERIFICATION.md#e13)) | Raspberry Pi Compute Module 4 + Coral Edge TPU | Detection and path tracking; pure pursuit / TEB | 1:87 miniature truck autonomy | Frontiers in Neurorobotics 16:846355 | Not identified | Real + simulation |

## Recent preprints

| Year | Paper / Project | Device | Model / Method | Task | Venue | Code / GitHub | Real / Simulation |
|---|---|---|---|---|---|---|---|
| 2026 | [AROLA: A Modular Layered Architecture for Scaled Autonomous Racing](https://arxiv.org/abs/2602.02730) ([E45](VERIFICATION.md#e45)) | NVIDIA Jetson; exact variant not specified in reviewed hardware passage | Modular ROS 2 layers; Race Monitor | Scaled racing and runtime evaluation | arXiv preprint | [Resource](https://github.com/GIU-F1Tenth/minimal_sofware_example) | Real + simulation |
| 2026 | [Efficient Real-World Autonomous Racing via Attenuated Residual Policy Optimization](https://arxiv.org/abs/2603.12960) ([E42](VERIFICATION.md#e42)) | Jetson Orin Nano Super | Attenuated residual policy optimization (alpha-RPO), PPO | Zero-shot sim2real LiDAR racing | arXiv preprint; submitted 13 March 2026 | [Resource](https://github.com/raphajaner/arpo_racing) | Real + simulation |
| 2026 | [NeoRacer: An Open, Standardized 1:12 Scale Autonomous Race Car for Benchmarking and Education](https://arxiv.org/abs/2607.26855) ([E41](VERIFICATION.md#e41)) | Jetson Orin Nano; LiDAR, global-shutter camera and IMU | Open hardware and ROS 2 platform | Standardized scaled racing and education | arXiv preprint; submitted 29 July 2026 | [Resource](https://github.com/Neobotics-Foundation-Inc/) | Physical platform and pilot deployments |
| 2025 | [Tackling Snow-Induced Challenges: Safe Autonomous Lane-Keeping with Robust Reinforcement Learning](https://arxiv.org/abs/2512.12987) ([E46](VERIFICATION.md#e46)) | Jetson Nano / JetRacer; RealSense T265 | AR-RDPG and attention-based AR-CADPG | Robust lane keeping | arXiv preprint | Not identified | Real robotic car + CARLA simulation |

## Perception and supporting systems

| Year | Paper / Project | Device | Model / Method | Task | Venue | Code / GitHub | Real / Simulation |
|---|---|---|---|---|---|---|---|
| 2026 | [A Serverless Edge-Native Data Processing Architecture for Autonomous Driving Training](https://arxiv.org/abs/2601.22919) ([E19](VERIFICATION.md#e19)) | Jetson Orin Nano | Serverless processing and ROS 2 comparison | Training-data infrastructure | arXiv preprint | [Resource](https://github.com/LASFAS/jblambda) | Edge data-system evaluation |
| 2026 | [EdgeVTP: Exploration of Latency-efficient Trajectory Prediction for Edge-based Embedded Vision Applications](https://openaccess.thecvf.com/content/CVPR2026W/EVW/html/Kim_EdgeVTP_Exploration_of_Latency-efficient_Trajectory_Prediction_for_Edge-based_Embedded_Vision_CVPRW_2026_paper.html) ([E47](VERIFICATION.md#e47)) | Jetson Nano (10W) and Xavier NX (20W) | Bounded interaction graph; lightweight temporal model; one-shot curve decoding | Vehicle trajectory prediction | IEEE/CVF CVPR Workshops 2026 (EVW) | [Resource](https://github.com/SeungjinStevenKim/EdgeVTP) | Dataset + embedded inference benchmarks |
| 2025 | [Efficient On-Chip Implementation of 4D Radar-Based 3D Object Detection on Hailo-8L](https://arxiv.org/abs/2505.00757) ([E18](VERIFICATION.md#e18)) | Hailo-8L | Reshaped radar neural-network operations for accelerator compatibility | Radar 3D detection | arXiv preprint | Not identified | Embedded benchmark; perception only |
| 2025 | [Towards Accurate and Efficient 3D Object Detection for Autonomous Driving: A Mixture of Experts Computing System on Edge](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Towards_Accurate_and_Efficient_3D_Object_Detection_for_Autonomous_Driving_ICCV_2025_paper.html) ([E48](VERIFICATION.md#e48)) | Jetson AGX Orin | EMC2 multimodal mixture of experts; routing and graph/memory optimization | LiDAR-camera 3D detection | IEEE/CVF ICCV 2025:25903–25913; DOI 10.1109/ICCV51701.2025.02403 | [Resource](https://github.com/LinshenLiu622/EMC2) | KITTI/nuScenes + embedded inference; perception only |
| 2024 | [HARD: Hardware-Aware Lightweight Real-Time Semantic Segmentation Model Deployable from Edge to GPU](https://openaccess.thecvf.com/content/ACCV2024/html/Kwon_HARD__Hardware-Aware_lightweight_Real-time_semantic_segmentation_model_Deployable_from_ACCV_2024_paper.html) ([E49](VERIFICATION.md#e49)) | Jetson Orin NX 16GB; STM32F746NG / Cortex-M7 | Hardware-scaled segmentation variants; dual atrous pooling | Road-scene semantic segmentation | ACCV 2024:3552–3569 | Not identified | Cityscapes/CamVid/COCO-Stuff + hardware inference |
| 2024 | [Real-Time 3D Object Detection Using InnovizOne LiDAR and Low-Power Hailo-8 AI Accelerator](https://arxiv.org/abs/2412.05594) ([E17](VERIFICATION.md#e17)) | Hailo-8 + InnovizOne LiDAR | PointPillars accelerator deployment | 3D object detection | arXiv preprint | [Resource](https://github.com/AIROTAU/PointPillarsHailoInnoviz) | Hardware perception demonstration |
| 2023 | [ES3Net: Accurate and Efficient Edge-Based Self-Supervised Stereo Matching Network](https://openaccess.thecvf.com/content/CVPR2023W/EVW/html/Fang_ES3Net_Accurate_and_Efficient_Edge-Based_Self-Supervised_Stereo_Matching_Network_CVPRW_2023_paper.html) ([E50](VERIFICATION.md#e50)) | Jetson TX2 | Self-supervised stereo; dual-disparity learning | Metric depth perception | IEEE/CVF CVPR Workshops 2023 (EVW) | [Resource](https://github.com/IShengFang/ES3Net) | Depth dataset and edge inference evaluation |
| 2023 | [Run Your 3D Object Detector on NVIDIA Jetson Platforms: A Benchmark Analysis](https://www.mdpi.com/1424-8220/23/8/4005) ([E16](VERIFICATION.md#e16)) | Jetson Nano, TX2, Xavier NX and AGX-family boards | 3D object-detector deployment benchmarks | Perception and embedded latency | Sensors 23(8):4005 | Not identified | Embedded hardware; perception only |
| 2021 | [ProAI: An Efficient Embedded AI Hardware for Automotive Applications — A Benchmark Study](https://arxiv.org/abs/2108.05170) ([E51](VERIFICATION.md#e51)) | ZF ProAI and Jetson Nano; workstation baseline | Multitask-CenterNet; latency and power benchmarking | Automotive perception hardware comparison | IEEE/CVF ICCV Workshops 2021 (ERCVAD) | Not identified | Embedded hardware benchmark |

## Simulation and offboard-control references

| Year | Paper / Project | Device | Model / Method | Task | Venue | Code / GitHub | Real / Simulation |
|---|---|---|---|---|---|---|---|
| 2025 | [VLDrive: Vision-Augmented Lightweight MLLMs for Efficient Language-grounded Autonomous Driving](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_VLDrive_Vision-Augmented_Lightweight_MLLMs_for_Efficient_Language-grounded_Autonomous_Driving_ICCV_2025_paper.html) ([E52](VERIFICATION.md#e52)) | No Pi/Jetson deployment verified | 1.3B-parameter MLLM; visual-token pruning and memory aggregation | Language-conditioned driving | IEEE/CVF ICCV 2025:5923–5933 | [Resource](https://github.com/ReaFly/VLDrive) | CARLA closed-loop simulation |
| 2024 | [Development and Control of an Autonomous RC Racing Car](https://www.sciencedirect.com/science/article/pii/S2405896325000448) ([E40](VERIFICATION.md#e40)) | Jetson Nano onboard; longitudinal speed command from host | Identified vehicle model; PID, MPC and LQR comparison | Lateral control on a marked track | IFAC-PapersOnLine 58(28):678–683; DOI 10.1016/j.ifacol.2025.01.044 | Not identified | Real vehicle; external speed command |
| 2023 | [Chronos and CRS: Design of a Miniature Car-Like Robot and a Software Framework for Single and Multi-Agent Robotics and Control](https://arxiv.org/abs/2209.12048) ([E20](VERIFICATION.md#e20)) | ESP32-WROOM32D onboard; CRS communicates over Wi-Fi | Low-level MCU control; MPC and safety-filter framework | Miniature racing and multi-agent control | IEEE ICRA 2023 | [Resource](https://gitlab.ethz.ch/ics/crs) | Real + simulation; offboard high-level pipeline |
| 2023 | [High-Speed Autonomous Racing Using Trajectory-Aided Deep Reinforcement Learning](https://arxiv.org/abs/2306.07003) ([E22](VERIFICATION.md#e22)) | No onboard device verified | TD3 with trajectory-derived reward | F1TENTH racing | IEEE RA-L 8(9); DOI 10.1109/LRA.2023.3295252 | [Resource](https://github.com/BDEvan5/TrajectoryAidedLearning) | Simulation |
| 2023 | [VAD: Vectorized Scene Representation for Efficient Autonomous Driving](https://openaccess.thecvf.com/content/ICCV2023/html/Jiang_VAD_Vectorized_Scene_Representation_for_Efficient_Autonomous_Driving_ICCV_2023_paper.html) ([E53](VERIFICATION.md#e53)) | No Pi/Jetson deployment verified | Vectorized scene representation; VAD-Base and VAD-Tiny | End-to-end motion planning | IEEE/CVF ICCV 2023:8340–8350 | [Resource](https://github.com/hustvl/VAD) | nuScenes dataset evaluation |
| 2020 | [Go-CHART: A Miniature Remotely Accessible Self-Driving Car Robot](https://par.nsf.gov/servlets/purl/10277361) ([E21](VERIFICATION.md#e21)) | Pi 3B, Pi Zero and Teensy; external Jetson TX2 | Distributed sensing and offloaded processing | Miniature self-driving research | IEEE IROS 2020; DOI 10.1109/IROS45743.2020.9341770 | Not identified | Real; external GPU involved |

## Open-source projects

| Year | Paper / Project | Device | Model / Method | Task | Venue | Code / GitHub | Real / Simulation |
|---|---|---|---|---|---|---|---|
| 2025 | [ResAwareWoR](https://github.com/CSL-KU/ResAwareWoR) ([E24](VERIFICATION.md#e24)) | Target hardware must be checked per experiment | Resource-aware multi-resolution driving models | Compute/accuracy tradeoffs | Project; repository created 2025 | [Resource](https://github.com/CSL-KU/ResAwareWoR) | Experiment-dependent; not independently reproduced |
| 2022 | [DeepPicar-v3](https://github.com/CSL-KU/DeepPicar-v3) ([E23](VERIFICATION.md#e23)) | Raspberry Pi | DAVE-2/PilotNet-style CNN, TFLite | Camera-to-steering | Project; repository created 2022 | [Resource](https://github.com/CSL-KU/DeepPicar-v3) | Real vehicle |

## Surveys

| Year | Paper / Project | Device | Model / Method | Task | Venue | Code / GitHub | Real / Simulation |
|---|---|---|---|---|---|---|---|
| 2025 | [A Comparative Study of Scaled Autonomous Vehicle Platforms for Research and Education](https://ieeexplore.ieee.org/document/11086476/) ([E54](VERIFICATION.md#e54)) | Quanser QCar; MIT RACECAR; SunFounder PiCar | Hardware, sensor and compute comparison | Platform selection for research and education | IEEE MHTC 2025; DOI 10.1109/MHTC65808.2025.11086476 | Not identified | Comparative study |
| 2024 | [Autonomous Driving Small-Scale Cars: A Survey of Recent Development](https://arxiv.org/abs/2404.06229) ([E26](VERIFICATION.md#e26)) | Pi, Jetson and other scaled-car platforms | Platform and autonomy-method survey | Small-scale driving | arXiv version reviewed | N/A | Survey |
| 2024 | [Unifying F1TENTH Autonomous Racing: Survey, Methods and Benchmarks](https://arxiv.org/abs/2402.18558) ([E27](VERIFICATION.md#e27)) | F1TENTH ecosystem | Racing methods and benchmark survey | Scaled racing | arXiv version reviewed | N/A | Survey + simulation benchmarks |
| 2023 | [A Survey on Approximate Edge AI for Energy Efficient Autonomous Driving Services](https://arxiv.org/abs/2304.14271) ([E25](VERIFICATION.md#e25)) | Multiple edge platforms | Approximation and efficient inference survey | Energy-efficient driving services | IEEE Communications Surveys & Tutorials 25(4); DOI 10.1109/COMST.2023.3302474 | N/A | Survey |
| 2022 | [Autonomous Vehicles on the Edge: A Survey on Autonomous Vehicle Racing](https://arxiv.org/abs/2202.07008) ([E28](VERIFICATION.md#e28)) | Multiple racing platforms | Autonomous-racing survey | Racing | IEEE Open Journal of Intelligent Transportation Systems | N/A | Survey |

## Foundations and legacy platforms

| Year | Paper / Project | Device | Model / Method | Task | Venue | Code / GitHub | Real / Simulation |
|---|---|---|---|---|---|---|---|
| 2019 | [DeepPiCar](https://github.com/dctian/DeepPiCar) ([E32](VERIFICATION.md#e32)) | Raspberry Pi + Coral Edge TPU | OpenCV lane following and TensorFlow perception | Lane and traffic-object tasks | Open-source tutorial project; origin 2019 | [Resource](https://github.com/dctian/DeepPiCar) | Real vehicle |
| 2019 | [JetRacer](https://github.com/NVIDIA-AI-IOT/jetracer) ([E31](VERIFICATION.md#e31)) | Jetson Nano | PyTorch CNN; TensorRT deployment | Vision-based RC racing | NVIDIA project; origin 2019 | [Resource](https://github.com/NVIDIA-AI-IOT/jetracer) | Real vehicle |
| 2018 | [DeepPicar: A Low-cost Deep Neural Network-based Autonomous Car](https://doi.org/10.1109/RTCSA.2018.00011) ([E29](VERIFICATION.md#e29)) | Raspberry Pi 3 | NVIDIA DAVE-2-style CNN | End-to-end RC driving | IEEE RTCSA 2018 | [Resource](https://github.com/mbechtel2/DeepPicar-v2) | Real vehicle |
| 2016 | [DonkeyCar](https://github.com/autorope/donkeycar) ([E30](VERIFICATION.md#e30)) | Raspberry Pi / supported Jetson configurations | Behavior cloning and vehicle-control framework | RC-car autonomy | Open-source platform; origin 2016 | [Resource](https://github.com/autorope/donkeycar) | Real + simulator integrations |

## Reuse

Original curation is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Papers, code and data retain their own licenses. This repository does not redistribute paper PDFs.
