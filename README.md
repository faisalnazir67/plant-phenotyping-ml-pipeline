# Plant Phenotyping ML Pipeline

**Automated Plant Health Assessment and Leaf Analysis System**

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 🌱 Project Overview

An advanced computer vision pipeline for automated plant phenotyping that combines state-of-the-art deep learning models to analyze plant health, segment individual leaves, and extract comprehensive morphological and physiological traits. This system enables precise, non-invasive assessment of plant characteristics for agricultural research and practical farming applications.

**Supervisor:** Dr. Murtaza Taj  
**Team:** Mohammad Salman, Muhammad Faisal Nazir

## 🎯 Key Features

- **Automated Plant Detection**: Uses GroundingDINO for precise plant identification
- **Advanced Leaf Segmentation**: FastSAM and SAM integration for individual leaf isolation
- **Comprehensive Trait Analysis**: 15+ morphological and physiological measurements
- **Health Assessment**: Real-time plant health scoring and stress detection
- **Interactive Demo**: Streamlit web interface for easy testing
- **Professional Output**: JSON reports with detailed analysis results

## 🔧 Technical Architecture

### Core Pipeline Components

1. **Stage 1: Plant Detection**
   - GroundingDINO with SwinT backbone
   - Text-prompted plant detection ("green plant only without soil")
   - Precise bounding box generation

2. **Stage 2: Background Removal**
   - FastSAM-based segmentation
   - Intelligent background elimination
   - Clean plant isolation

3. **Stage 3: Leaf Segmentation & Analysis**
   - Individual leaf extraction
   - Advanced filtering algorithms (area-based, IoU-based)
   - Comprehensive trait measurement

### Measured Traits

#### Morphological Analysis
- **Leaf Area**: Total surface area for photosynthetic capacity assessment
- **Shape Features**: Circularity, symmetry, and geometric properties
- **Size Metrics**: Length, width, and aspect ratios

#### Color & Health Analysis
- **Green Intensity**: Chlorophyll content estimation
- **DGCI (Dark Green Color Index)**: Plant health indicator
- **Color Uniformity**: Disease and stress detection
- **Vegetation Indices**: Multiple health scoring methods

#### Advanced Features
- **Texture Analysis**: Surface characteristics and patterns
- **Vigor Index**: Combined health assessment score
- **Stress Indicators**: Early warning system for plant problems

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- CUDA-compatible GPU (recommended)
- 8GB+ RAM

### Quick Start

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/plant-phenotyping-ml-pipeline.git
cd plant-phenotyping-ml-pipeline
```

2. **Set up Virtual Environment**
```bash
# Create virtual environment
python -m venv plant_env

# Activate environment
# Windows:
plant_env\Scripts\activate
# macOS/Linux:
source plant_env/bin/activate
```

3. **Install Dependencies**
```bash
# Clone required models
git clone https://github.com/IDEA-Research/GroundingDINO.git
git clone https://github.com/CASIA-IVA-Lab/FastSAM.git

# Install requirements
pip install -r GroundingDINO/requirements.txt
pip install -r FastSAM/requirements.txt
pip install streamlit matplotlib seaborn plotly pandas
```

4. **Download Model Weights**
   - Download GroundingDINO weights from [official repo](https://github.com/IDEA-Research/GroundingDINO)
   - Download FastSAM weights from [official repo](https://github.com/CASIA-IVA-Lab/FastSAM)
   - Place weights in respective model directories

5. **Run the Demo**
```bash
streamlit run app.py
```

## 📊 Usage

### Command Line Interface
```python
from plant_pipeline import PlantAnalyzer

analyzer = PlantAnalyzer()
results = analyzer.analyze_plant("path/to/plant_image.jpg")
print(results['health_score'])
```

### Web Interface
1. Launch the Streamlit app: `streamlit run app.py`
2. Upload plant image or enter image filename
3. View comprehensive analysis results
4. Download detailed JSON report

### Sample Images
Test with provided sample images:
- `test.jpeg` - Healthy plant specimen
- `lumsimage1.jpeg` - Multi-leaf analysis example

## 📈 Output Examples

The system generates:
- **Visual Segmentation**: Individual leaf boundaries and masks
- **Trait Measurements**: Detailed numerical analysis
- **Health Reports**: Comprehensive JSON output with all metrics
- **Visualization**: Interactive plots and charts

## 🔬 Scientific Foundation

Built on cutting-edge research:
- **GroundingDINO**: [Grounding DINO Paper](https://arxiv.org/abs/2303.05499)
- **FastSAM**: [Fast Segment Anything](https://arxiv.org/abs/2306.12156)
- **SAM**: [Segment Anything Model](https://arxiv.org/abs/2304.02643)

## 🌍 Applications

- **Agricultural Research**: Crop monitoring and yield prediction
- **Plant Breeding**: Phenotype selection and analysis
- **Disease Detection**: Early identification of plant stress
- **Educational**: Teaching plant biology and analysis techniques
- **Home Gardening**: Personal plant health monitoring

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dr. Murtaza Taj for supervision and guidance
- GroundingDINO, FastSAM, and SAM teams for open-source models
- Plant phenotyping research community


**⭐ Star this repository if you find it helpful!**
