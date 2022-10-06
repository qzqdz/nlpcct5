import torch
import evaluate
print(torch.cuda.is_available())

pred = [1,0,1,0,1,1,1,1,0]
label = [0,1,1,0,0,0,0,0,0]

metric = evaluate.load('precision')
metric.add_batch(
    predictions=pred,
    references=label
)
x = metric.compute()
print(x)
