<h3 align="center">
<p>State-of-the-art Natural Language Processing for TensorFlow 2.0 and PyTorch
</h3>
<p></p>
说明：

<p>2022/9/21</p>
<p>1. src/transformers/data/processors/glue.py </p>
<p>添加了一个nlpcct5的processor 我实验暂时只使用了level1的标签</p>
<p>2. src/transformers/modeling_bert.py </p>
<p>这里面添加了多标签分类的bert实现 修改了loss</p>
<p>3.data为直接读取的json文件，但是需要改名为train_set.json和val_set.json</p>


训练命令：
CUDA_VISIBLE_DEVICES=7 python ./examples/run_glue.py     
--model_type bert     
--model_name_or_path /apsarapangu/disk1/cj267166/models/bert-base-uncased     
--task_name nlpcct5    
--do_train     
--do_eval     
--do_lower_case     
--data_dir /apsarapangu/disk1/cj267166/nlpcct5     
--max_seq_length 512     
--per_gpu_eval_batch_size=8       
--per_gpu_train_batch_size=8       
--learning_rate 2e-5     
--num_train_epochs 3.0     
--output_dir ./output_dir/nlpcct5/

pip install -e .
我的训练命令：
python ./examples/run_glue.py     
--model_type bert     
--model_name_or_path D:/study/model/nlpcc_base_bert     
--task_name nlpcct5    
--do_train     
--do_eval     
--do_lower_case     
--data_dir D:/study/nlpcc/traning_datasets     
--max_seq_length 512     
--per_gpu_eval_batch_size=8       
--per_gpu_train_batch_size=8       
--learning_rate 2e-5     
--num_train_epochs 3.0     
--output_dir ./output_dir/nlpcct5/


paperwithcode中的开源多标签分类模型
https://paperswithcode.com/task/multi-label-text-classification