# Google - Isolated Sign Language Recognition (Kaggle Competition) 🥈
My Silver Medal solution in [Google - Isolated Sign Language Recognition Kaggle competition](https://www.kaggle.com/competitions/asl-signs/leaderboard)
- - -
## Data Preparation
Download kaggle dataset below link \
[Kaggle Dataset](https://www.kaggle.com/competitions/asl-signs/data)
- - -
## Prerequisites
To use the repository, we provide a docker environment.
```bash
Make env
Make over
Make build
Make exec
```
- - -
## Our Method
- Transformer Architecture for time-series data
- Data Augmentation(Masking,Rotation,Flip)
- Self-Supervised Method (pretraining) - Masked Auto Encoder
- Ensemble
- Change Dropout Rate during training for moodel generalization
- Optuna for hyper-parameter tunnings
- Stochastic Weight Averaging for model generalizaiton 
- - -


