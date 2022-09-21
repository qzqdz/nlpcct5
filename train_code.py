'''
python ./examples/run_glue.py     --model_type bert     --model_name_or_path D:/study/model/nlpcc_base_bert     --task_name nlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=8       --per_gpu_train_batch_size=8       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir ./output_dir/nlpcct5/


python ./examples/run_glue.py     --model_type bert     --model_name_or_path D:/study/transformers_280nlpcc/output_dir/nlpcct5/checkpoint-24500     --task_name nlpcct5   --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=8       --per_gpu_train_batch_size=8       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir ./output_dir/nlpcct5/checkpoint-24500/

'''