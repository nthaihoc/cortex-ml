from typing import Any, Dict, Optional
from loguru import logger
from pydantic import ValidationError, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class ParserConfig(BaseModel):
    data_path: str = ""
    output_dir: Optional[str] = None
    split_ratios: list[float] = [0.8, 0.1, 0.1] 
    random_seed: int = 42
    stratified_split: bool = True
    force_resplit: bool = False

class TrainConfig(BaseModel):
    model_name: Optional[str] = None 
    freeze_encoder: bool = True
    num_workers: int = 4
    batch_size: int = 32
    learning_rate: float = 1e-4
    weight_decay: Optional[float] = None
    warmup_ratio: Optional[float] = None
    max_grad_norm: Optional[float] = None
    grad_accum_step: Optional[int] = None
    num_epoch: int = 10
    patience: int = 10
    delta: float = 0.0005
    mode: str = "min"
    monitor: str = "val_loss"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        extra="ignore",
        env_nested_delimiter="__"
    )

    run_id: Optional[str] = None
    experiment_name: str = "CortexML"
    run_name: str = "ctx_epr01"
    tags: Dict[str, Any] = {
        "version": 1
    }
    description: str = "Cortex is ML Platform support custom, train, test model."
    log_system_metrics: Optional[bool] = True

    parser: ParserConfig = ParserConfig()
    train: TrainConfig = TrainConfig()

    @classmethod
    def load_settings(cls, **kwargs):
        try:
            return cls(**kwargs)
        except ValidationError as e:
            raise
        except Exception as e:
            raise

settings = Settings.load_settings()