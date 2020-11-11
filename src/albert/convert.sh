python convert_albert_tf_checkpoint_to_pytorch.py \
    --tf_checkpoint_path=./pretrain/tf/albert_base_zh \
    --bert_config_file=./configs/albert_config_base.json \
    --pytorch_dump_path=./pretrain/pytorch/albert_base_zh/pytorch_model.bin \
    --share_type=all
