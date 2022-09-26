'''
bert
python ./examples/run_glue.py     --model_type bert     --model_name_or_path D:/study/model/nlpcc_base_bert     --task_name nlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=8       --per_gpu_train_batch_size=8       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir ./output_dir/nlpcct5/

bert
python ./examples/run_glue.py     --model_type bert     --model_name_or_path E:/model/nlpcc_base_bert     --task_name nlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=8       --per_gpu_train_batch_size=8       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir E:/model/output_dir/

1.全标签
all_label bert with upan
python ./examples/run_glue.py     --model_type bert     --model_name_or_path E:/model/nlpcc_base_bert_all     --task_name allnlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=8       --per_gpu_train_batch_size=8       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir E:/model/nlpcc_base_bert_all/output_dir/

all_label xlnet with upan
python ./examples/run_glue.py     --model_type xlnet     --model_name_or_path E:/model/nlpcc_base_xlnet_all     --task_name allnlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=4       --per_gpu_train_batch_size=4       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir E:/model/nlpcc_base_xlnet_all/output_dir/

all_label roberta with upan
python ./examples/run_glue.py     --model_type roberta     --model_name_or_path E:/model/nlpcc_base_roberta_all     --task_name allnlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=8       --per_gpu_train_batch_size=8       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir E:/model/nlpcc_base_roberta_all/output_dir/



python ./examples/run_glue.py     --model_type bert     --model_name_or_path D:/study/model/nlpcc_base_bert     --task_name nlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=8       --per_gpu_train_batch_size=8       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir ./output_dir/nlpcct5/


bert test
python ./examples/run_glue.py     --model_type bert     --model_name_or_path  E:/model/nlpcc_base_bert_all/output_dir/checkpoint-33500     --task_name allnlpcct5     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=8       --per_gpu_train_batch_size=8       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir  E:/model/nlpcc_base_bert_all/output_dir/



'''

'''
电脑2

all_label xlnet with upan
python ./examples/run_glue.py     --model_type xlnet     --model_name_or_path D:/model/nlpcc_base_xlnet_all     --task_name allnlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/data/nlpcct5/training_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=2       --per_gpu_train_batch_size=2       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir D:/model/nlpcc_base_xlnet_all/output_dir/


'''
