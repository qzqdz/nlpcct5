'''


1.全标签
all_label bert with upan
python ./examples/run_glue.py     --model_type bert     --model_name_or_path E:/model/nlpcc_base_bert_all     --task_name allnlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=8       --per_gpu_train_batch_size=8       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir E:/model/nlpcc_base_bert_all/output_dir/

all_label xlnet with upan
python ./examples/run_glue.py     --model_type xlnet     --model_name_or_path F:/model1/nlpcc_base_xlnet_all     --task_name allnlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=4       --per_gpu_train_batch_size=4       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir F:/model1/nlpcc_base_xlnet_all/output_dir/

all_label xlnet with upan test
python ./examples/run_glue.py     --model_type xlnet     --model_name_or_path F:/model1/nlpcc_base_xlnet_all/output_dir/checkpoint-67500     --task_name allnlpcct5    --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=4       --per_gpu_train_batch_size=4       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir F:/model1/nlpcc_base_xlnet_all/output_dir/checkpoint-67500/test


all_label roberta with upan
python ./examples/run_glue.py     --model_type roberta     --model_name_or_path F:/model1/nlpcc_base_roberta_all     --task_name allnlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=8       --per_gpu_train_batch_size=8       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir F:/model1/nlpcc_base_roberta_all/output_dir/

all_label rpberta test



2.level1标签
bert train
python ./examples/run_glue.py     --model_type bert     --model_name_or_path E:/model/nlpcc_base_bert     --task_name nlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=8       --per_gpu_train_batch_size=8       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir E:/model/nlpcc_base_bert/output_dir/
bert test
python ./examples/run_glue.py     --model_type bert     --model_name_or_path E:/model/nlpcc_base_bert/epcoh3_21_title    --task_name nlpcct5level1     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=8       --per_gpu_train_batch_size=8       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir E:/model/nlpcc_base_bert/epcoh3_21_title
acc = 0.7141619047619048
macro_f1 = 0.08724486698894099
micro_f1 = 0.11463464998967521

acc = 0.9255142857142857
macro_f1 = 0.7178801980374249
micro_f1 = 0.7692852296527921

roberta test
python ./examples/run_glue.py     --model_type roberta     --model_name_or_path  E:/model/nlpcc_base_roberta/output_dir/checkpoint-33500     --task_name nlpcct5level1     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=8       --per_gpu_train_batch_size=8       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir  E:/model/nlpcc_base_roberta/output_dir/checkpoint-33500/
acc = 0.7155238095238096
marcof1 = 0.08502234790493579
microf1 = 0.11364985163204747

acc = 0.9248761904761905
macro_f1 = 0.7187208026792506
micro_f1 = 0.7659347181008901

xlnet train
python ./examples/run_glue.py     --model_type xlnet     --model_name_or_path  E:/model/nlpcc_base_xlnet/output_dir/checkpoint-54000     --task_name nlpcct5level1    --do_train    --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=4       --per_gpu_train_batch_size=4       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir  E:/model/nlpcc_base_xlnet/output_dir/54000_more


xlnet test
python ./examples/run_glue.py     --model_type xlnet     --model_name_or_path  E:/model/nlpcc_base_xlnet/output_dir/checkpoint-54000     --task_name nlpcct5level1     --do_eval     --do_lower_case     --data_dir D:/study/nlpcc/traning_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=4       --per_gpu_train_batch_size=4       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir  E:/model/nlpcc_base_xlnet/
acc = 0.7144952380952381
macro_f1 = 0.08397597255236608
micro_f1 = 0.11402056980730582

acc =





'''

'''
电脑2

all_label xlnet
python ./examples/run_glue.py     --model_type xlnet     --model_name_or_path D:/model/nlpcc_base_xlnet_all     --task_name allnlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/data/nlpcct5/training_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=2       --per_gpu_train_batch_size=2       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir D:/model/nlpcc_base_xlnet_all/output_dir/

all_label xlnet test 
python ./examples/run_glue.py     --model_type xlnet     --model_name_or_path D:/model/nlpcc_base_xlnet_all     --task_name allnlpcct5    --do_eval     --do_lower_case     --data_dir D:/data/nlpcct5/training_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=2       --per_gpu_train_batch_size=2       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir D:/model/nlpcc_base_xlnet_all/

notrain xlnet test
python ./examples/run_glue.py     --model_type xlnet     --model_name_or_path D:/model/nlpcc_base_xlnet_all     --task_name allnlpcct5    --do_eval     --do_lower_case     --data_dir D:/data/nlpcct5/training_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=2       --per_gpu_train_batch_size=2       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir D:/model/nlpcc_base_xlnet_all/


python ./examples/run_glue.py     --model_type roberta     --model_name_or_path D:/model/nlpcc_roberta_base_all     --task_name allnlpcct5    --do_train     --do_eval     --do_lower_case     --data_dir D:/data/nlpcct5/training_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=2       --per_gpu_train_batch_size=2       --learning_rate 1e-5     --num_train_epochs 3.0     --output_dir D:/model/nlpcc_roberta_base_all/output_dir/



lavel1_label xlnet
python ./examples/run_glue.py     --model_type xlnet     --model_name_or_path D:/model/nlpcc_base_xlnet     --task_name nlpcct5level1     --do_train   --do_eval     --do_lower_case     --data_dir D:/data/nlpcct5/training_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=2       --per_gpu_train_batch_size=2       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir D:/model/nlpcc_base_xlnet/output_dir1/

lavel1_label xlnet test
python ./examples/run_glue.py     --model_type xlnet     --model_name_or_path D:/model/nlpcc_base_xlnet/output_dir/checkpoint-54000     --task_name nlpcct5level1     --do_eval     --do_lower_case     --data_dir D:/data/nlpcct5/training_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=2       --per_gpu_train_batch_size=2       --learning_rate 2e-5     --num_train_epochs 3.0     --output_dir D:/model/nlpcc_base_xlnet/output_dir/checkpoint-54000/

lavel1_label bert 
python ./examples/run_glue.py     --model_type bert     --model_name_or_path D:/model/nlpcc_bert_base     --task_name nlpcct5level1    --do_train     --do_eval     --do_lower_case     --data_dir D:/data/nlpcct5/training_datasets     --max_seq_length 512     --per_gpu_eval_batch_size=4       --per_gpu_train_batch_size=4       --learning_rate 1e-5     --num_train_epochs 3.0     --output_dir D:/model/nlpcct5_base_bert/output_dir/

'''
