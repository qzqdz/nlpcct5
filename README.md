<h3 align="center">
<p>State-of-the-art Natural Language Processing for TensorFlow 2.0 and PyTorch
</h3>
<p></p>
说明：

<p><h4>2022/9/21</h4></p>
<p>1. src/transformers/data/processors/glue.py </p>
<p>添加了一个nlpcct5的processor 我实验暂时只使用了level1的标签</p>
<p>2. src/transformers/modeling_bert.py </p>
<p>这里面添加了多标签分类的bert实现 修改了loss</p>
<p>3.data为直接读取的json文件，但是需要改名为train_set.json和val_set.json</p>

<p><h4>2022/9/25</h4></p>
<p>4.src/transformers/data/processors/glue.py </p>
<p>添加了一个allnlpcct5的processor 使用了levels的全量标签</p>

<p>5.src\transformers\data\metrics\__init__.py</p>
<p>添加了一个新的metric，allnlpcct5，其作用和nlpcct5一样</p>
<p>metrics将结果写入了记事本中，绝对路径</p>
<p>6. src\transformers\modeling_xlnet.py </p>
<p>添加标记点“动刀处”，方便索引</p>
<p>7.src\transformers\data\processors\nlpcct5_all_label.txt </p>
<p>把1530个列标签写入了txt中，在metric和processors中使用的是绝对路径！！！</p>
<p>8.train_code.py </p>
<p>记录训练命令的地方</p>
<p>9.eval_res </p>
<p>存预测结果标签的地方</p>

<p><h4>2022/9/26</h4></p>
<p>10.src\transformers\data\processors\label_dir </p>
<p>添加label文件夹，里面放规定好顺序的label1~label3</p>
<p>10.src\transformers\data\processors\glue.py </p>
<p>添加make_label函数，该函数根据label（1,2,3）文件中的标签顺序对某条训练数据的标签进行one-hot处理，并返回01list</p>
<p>11.src\transformers\data\processors\glue.py </p>
<p>添加read_label函数，读入label（1,2,3）中的标签list</p>

<p><h4>2022/9/27</h4></p>
<p>重新处理了代码，训练和测试的结果能对上了</p>


<p><h4>2022/10/2</h4></p>
<p>12.src\transformers\modeling_bert.py</p>
<p>在BertForSequenceClassification中添加compute_kl_loss方法，计算结果的kl散度</p>
<p>后面的output全部复制粘贴一份</p>
<p>loss的计算方法为两loss求和/2+5*kl</p>

<p><h4>2022/10/4</h4></p>
<p>13.src\transformers\modeling_bert.py</p>
<p>现在bert和backup bert 不重叠了</p>
<p>14.加入了ruters数据集</p>
<p>15.规范化bert的权重加和</p>
<p>16.写结果分析脚本</p>
<p> </p>
<p> --------- </p>
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

